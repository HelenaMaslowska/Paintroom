#######################################
# Author: Helena Masłowska
# 30.07.2022
from __future__ import print_function
from operator import mod
from tokenize import String
from xml.dom.minicompat import EmptyNodeList
from PIL import Image, ImageOps, ImageEnhance, ImageDraw, ImageFilter, ImageColor
from PIL.ImageQt import ImageQt			#read and change picture
import sys
import pathlib
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QColorDialog, QDialogButtonBox, QDialog, QPushButton, QLabel, QVBoxLayout, QMessageBox		#show on the screen
from PySide2.QtGui import QPixmap, QColor, QImage, QIcon, QPalette
import numpy as np
import os
import subprocess
import numpy as np
import scipy
import scipy.misc
import scipy.cluster
import matplotlib.image as matimg
from numpy import apply_along_axis
from mainwindow import Ui_MainWindow

import binascii
import struct
FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')

# kompilacja qtcreatora po zapisaniu: pyside2-uic mainwindow.ui -o mainwindow.py

# qt - czyta i zapisuje obrazki
# pil - obrobka obrazu
# self.ui - wszystkie rzeczy związane z plikiem mainwindow
class MainWindow(QMainWindow):
	"""
	TODO
	JPG doesnt have to save as a photo idk why
	make triangle/dual useful
	"""
	def __init__(self) -> None:
		'''
		pixmap: image which is shown on the screen
		curr_image: this image will be edited
		image: image which is saved in RAM but not in folder on computer
		filename: where the original photo is, it is used to open a photo
		'''
		super(MainWindow, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.set_functions()
		self.pixmap: QPixmap = None
		self.image: Image = None
		self.curr_image: Image = None		
		self.filename: str = None
		self.filename_temp: str == None
		self.saving_filename: str = None
		self.filetype = ''			# type of file, e.g. '.jpg'
		self.background: Image = None

	def set_functions(self):

		#files from computer buttons
		self.ui.add_img_btn.clicked.connect(self.add_photo)

		#background
		self.ui.transparency_btn.clicked.connect(self.setup_transparency)
		self.ui.white_radiobtn.clicked.connect(self.change_background)
		self.ui.color_radiobtn.clicked.connect(self.change_background)
		self.ui.stripped_radiobtn.clicked.connect(self.change_background)
		self.ui.stripes_btn.clicked.connect(self.stripes_mode)
		self.ui.how_many_stripes.valueChanged.connect(self.change_background)		
		self.ui.squares_radiobtn.clicked.connect(self.change_background)
		self.ui.how_many_squares.valueChanged.connect(self.change_background)

		self.ui.picked_only_color.clicked.connect(self.one_color_picker)
		self.ui.picked_color1.clicked.connect(self.color_picker1)
		self.ui.picked_color2.clicked.connect(self.color_picker2)
		self.ui.swap_btn.clicked.connect(self.swap_colors)

		# basic filters
		self.ui.color_chbox.clicked.connect(self.set_color_checkbox)
		self.ui.color_slider.valueChanged.connect(self.change_color_spinbox)
		self.ui.color_spinbox.valueChanged.connect(self.change_color_slider)
		self.ui.light_chbox.clicked.connect(self.set_brightness_checkbox)
		self.ui.light_slider.valueChanged.connect(self.change_light_spinbox)
		self.ui.light_spinbox.valueChanged.connect(self.change_light_slider)
		self.ui.contrast_chbox.clicked.connect(self.set_contrast_checkbox)
		self.ui.contrast_slider.valueChanged.connect(self.change_contrast_spinbox)
		self.ui.contrast_spinbox.valueChanged.connect(self.change_contrast_slider)

		# advanced filters
		self.ui.invert_chbox.clicked.connect(self.invert_colors_checkbox)
		self.ui.gauss_chbox.clicked.connect(self.gauss_blur_checkbox)
		self.ui.gauss_value.valueChanged.connect(self.gauss_blur_checkbox)

		# color picker
		self.ui.color_from_image.clicked.connect(self.get_color)
		self.ui.first_color_effect.clicked.connect(self.color_modifier)

		#approve or decline buttons
		self.ui.default_btn.clicked.connect(self.set_default)
		self.ui.apply_btn.clicked.connect(self.apply)
		self.ui.cancel_btn.clicked.connect(self.cancel)
		self.ui.default_btn_2.clicked.connect(self.set_default)
		self.ui.apply_btn_2.clicked.connect(self.apply)
		self.ui.cancel_btn_2.clicked.connect(self.cancel)

	def save_temp_file(self):
		self.filename_temp= 'paintroom_temp_image' + str(self.filetype)
		try:
			# if(self.filetype == '.jpg'):
			# 	self.image.convert("RGBA").save(self.filename_temp)	#ten convert rgba szkodzi jpgom bo one nie mają kanału alpha, ale bez A też nie działa xd
			self.image.save(self.filename_temp)
		except IOError:
			print("can't save file", self.filename_temp)

	def scale(self, pixmap: QPixmap):
		''' scale pixmap '''
		w, h = self.ui.image_shower.width(), self.ui.image_shower.height()
		if (pixmap.width() >= w):
			pixmap = pixmap.scaledToWidth(w)
		if (pixmap.height() >= h):
			pixmap = pixmap.scaledToHeight(h)
		return pixmap
	
	def merge_images(self, foreground, background):
		''' image temporarily is saved on RAM: foreground for transparent images and background, so here you merge these 2 layers
		:return: merged image
		'''
		background.paste(foreground, (0, 0), foreground)
		return background

	def img_to_pix(self, image: Image):
		''' merge background on pixmap and convert from Image type to pixmap '''
		image = image.convert("RGBA")
		if(self.background):
			image = self.merge_images(image, self.background)
		r, g, b, a = image.split()
		data = Image.merge('RGBA', (b, g, r, a)).tobytes("raw", "RGBA")
		img = QImage(data, image.width, image.height, QImage.Format_ARGB32) 
		self.pixmap = QPixmap.fromImage(img) 
		self.pixmap = self.scale(self.pixmap)

	def set_all_filters(self):
		if self.filename:
			self.curr_image = self.image.copy()
			# basic filters
			self.set_color()
			self.set_brightness()
			self.set_contrast()
			# premium filters
			self.invert_colors()
			self.gauss_blur()
			# color picker

			# back filter
			self.change_background()
			self.update_image()

	def update_image(self):
		if self.filename:
			self.img_to_pix(self.curr_image)
			self.ui.image_shower.setPixmap(self.pixmap)
			self.ui.image_shower.repaint()

	def set_default(self):
		self.ui.color_slider.setValue(50)
		self.ui.light_slider.setValue(50)
		self.ui.contrast_slider.setValue(50)
		self.ui.color_chbox.setChecked(False)
		self.ui.light_chbox.setChecked(False)
		self.ui.contrast_chbox.setChecked(False)
		self.ui.color_spinbox.setValue(self.ui.color_slider.value())
		self.ui.light_spinbox.setValue(self.ui.light_slider.value())
		self.ui.contrast_spinbox.setValue(self.ui.contrast_slider.value())
		self.ui.invert_chbox.setChecked(False)
		self.ui.gauss_chbox.setChecked(False)
		self.set_all_filters()
		return

	def apply(self):
		self.image = self.curr_image.copy()
		if(self.background):
			self.image = self.merge_images(self.image, self.background)
		self.save_temp_file()
		self.update_image()
		print("applied!")

	def cancel(self):
		self.curr_image = self.image.copy()
		self.save_temp_file()
		self.update_image()
		print("cancelled!")

	def save_as(self):			
		'''TODO
		JPG DOESN'T WORK YET xd useless function, apply make new image better
		change type to self.type
		'''
		self.apply()
		filepath, _ = QFileDialog.getSaveFileName(parent = self, caption='Save me! Just do it!', filter="Image files (*.png *.jpg)")
		self.image = self.image.save(filepath)

	def add_photo(self):
		''' add/replace new photo to main screen and show it scaled on image_shower '''
		self.filename, _ = QFileDialog.getOpenFileName( parent=self, caption='Open me!!!', filter="Image files (*.png *.jpg)" )	
		if self.filename != '':
			self.image = Image.open(self.filename)
			self.curr_image = Image.open(self.filename)
			self.filetype = pathlib.Path(self.filename).suffix
			self.get_color()
			self.set_all_filters()
			self.change_background()
			self.update_image()

	def setup_transparency(self):
		"""setup transparent btn and checkboxes"""
		if self.filename:
			if self.ui.transparency_btn.isChecked():
				self.ui.white_radiobtn.setDisabled(True)
				self.ui.color_radiobtn.setDisabled(True)
				self.ui.stripped_radiobtn.setDisabled(True)
				self.ui.squares_radiobtn.setDisabled(True)
				self.background = None	
			else:
				self.ui.white_radiobtn.setEnabled(True)
				self.ui.color_radiobtn.setEnabled(True)
				self.ui.stripped_radiobtn.setEnabled(True)
				self.ui.squares_radiobtn.setEnabled(True)
				self.change_background()
			self.update_image()	
		else:
			self.ui.transparency_btn.setChecked(True)

	def change_background(self):
		if not self.ui.transparency_btn.isChecked():
			w, h =  self.curr_image.width, self.curr_image.height
			color1 = self.ui.picked_color1.palette().button().color().name()
			color2 = self.ui.picked_color2.palette().button().color().name()
			self.background = Image.new("RGBA", (w, h))
			draw = ImageDraw.Draw(self.background)
			if self.ui.white_radiobtn.isChecked():
				draw.rectangle(  xy = [(0, 0), (w, h)],  fill = "#ffffff"  )
			elif self.ui.color_radiobtn.isChecked():
				draw.rectangle(  xy = [(0, 0), (w, h)],  fill = self.ui.picked_only_color.palette().button().color().name()  )
			elif self.ui.stripped_radiobtn.isChecked():
				stripes = self.ui.how_many_stripes.value()
				draw.rectangle(  xy = [(0, 0), (w, h)],  fill = color2  )											#black
				if self.ui.stripes_btn.text() == "||":
					for i in range(stripes):
						if i % 2 == 0:
							draw.rectangle(  xy = [(i*w//stripes, 0), ((i+1)*w//stripes, h)],  fill = color1  )		#white
				else:
					for i in range(stripes):
						if i % 2 == 0:
							draw.rectangle(  xy = [(0, i*h//stripes), (w, (i+1)*h//stripes)],  fill = color1  ) 	#white
			elif self.ui.squares_radiobtn.isChecked():
				squares = self.ui.how_many_squares.value()
				draw.rectangle(  xy = [(0, 0), (w, h)],  fill = color1  )											#black
				for i in range(squares):
					for j in range(squares):
						if (i + j) % 2:
							draw.rectangle( 
								xy = [ (i*w//squares, j*h//squares), ((i+1)*w//squares, (j+1)*h//squares) ],  
								fill = color2  ) 		#white
		self.update_image()

	def stripes_mode(self):
		if self.ui.stripes_btn.text() == "||":
			self.ui.stripes_btn.setText("=")
		elif self.ui.stripes_btn.text() == "=":
			self.ui.stripes_btn.setText("||")
		self.change_background()

	def one_color_picker(self):
		color = QColorDialog.getColor()
		if(color.isValid()):
			self.ui.picked_only_color.setStyleSheet("background-color: %s" % color.name())
			self.change_background()

	def color_picker1(self):
		color = QColorDialog.getColor()
		if(color.isValid()):
			self.ui.picked_color1.setStyleSheet("background-color: %s" % color.name())
			self.change_background()
	
	def color_picker2(self):
		color = QColorDialog.getColor()
		if(color.isValid()): 
			self.ui.picked_color2.setStyleSheet("background-color: %s" % color.name())
			self.change_background()
	
	def swap_colors(self):
		''' simply swap colors of 2 buttons '''
		color1 = self.ui.picked_color1.palette().button().color().name()
		color2 = self.ui.picked_color2.palette().button().color().name()
		self.ui.picked_color1.setStyleSheet("background-color: %s" % color2)
		self.ui.picked_color2.setStyleSheet("background-color: %s" % color1)
		self.change_background()

	def set_color(self):
		max_factor, min_factor = 2.0, 0.0	
		factor = self.ui.color_slider.value() * (max_factor-min_factor) / (self.ui.color_slider.maximum()-self.ui.color_slider.minimum()+1)
		enhancer = ImageEnhance.Color(self.curr_image)
		self.curr_image = enhancer.enhance(factor)

	def set_color_checkbox(self):
		''' Greyscale/color on photo with color checkbox '''
		if self.ui.color_chbox.isChecked():
			# self.curr_image = ImageOps.grayscale(self.image)
			self.ui.color_slider.setValue(self.ui.color_slider.maximum())
		elif not self.ui.color_chbox.isChecked():
			self.ui.color_slider.setValue(self.ui.color_slider.minimum())		
		self.change_color_spinbox()
		self.set_all_filters()

	def set_brightness(self):
		''' Set brightness of an image '''
		max_factor, min_factor = 2.0, 0.0		
		factor = self.ui.light_slider.value() * (max_factor-min_factor) / (self.ui.light_slider.maximum()-self.ui.light_slider.minimum()+1)
		enhancer = ImageEnhance.Brightness(self.curr_image)
		self.curr_image = enhancer.enhance(factor)

	def set_brightness_checkbox(self):
		''' Brightness on photo with light checkbox '''
		if self.ui.light_chbox.isChecked():
			self.ui.light_slider.setValue(self.ui.light_slider.maximum())
		elif not self.ui.light_chbox.isChecked():
			self.ui.light_slider.setValue(self.ui.light_slider.minimum())
		self.change_light_spinbox()	
		self.set_all_filters()

	def set_contrast(self):
		''' Set contrast on image'''
		max_factor, min_factor = 2.0, 0.0	
		factor = self.ui.contrast_slider.value() * (max_factor-min_factor) / (self.ui.contrast_slider.maximum()-self.ui.contrast_slider.minimum()+1)
		enhancer = ImageEnhance.Contrast(self.curr_image)
		self.curr_image = enhancer.enhance(factor)

	def set_contrast_checkbox(self):
		''' Contrast on photo with contrast checkbox '''
		if self.ui.contrast_chbox.isChecked():
			self.ui.contrast_slider.setValue(self.ui.contrast_slider.maximum())
		elif not self.ui.contrast_chbox.isChecked():
			self.ui.contrast_slider.setValue(self.ui.contrast_slider.minimum())		
		self.change_contrast_spinbox()
		self.set_all_filters()

	def change_color_slider(self):
		self.ui.color_slider.setValue(self.ui.color_spinbox.value())
		self.set_all_filters()

	def change_light_slider(self):
		self.ui.light_slider.setValue(self.ui.light_spinbox.value())
		self.set_all_filters()

	def change_contrast_slider(self):
		self.ui.contrast_slider.setValue(self.ui.contrast_spinbox.value())
		self.set_all_filters()

	def change_color_spinbox(self):
		self.ui.color_spinbox.setValue(self.ui.color_slider.value())
		if self.ui.color_slider.value() != self.ui.color_slider.maximum():
			self.ui.color_chbox.setChecked(False)
		else:
			self.ui.color_chbox.setChecked(True)
		self.set_all_filters()

	def change_light_spinbox(self):
		self.ui.light_spinbox.setValue(self.ui.light_slider.value())
		if self.ui.light_slider.value() != self.ui.light_slider.maximum():
			self.ui.light_chbox.setChecked(False)
		else:
			self.ui.light_chbox.setChecked(True)
		self.set_all_filters()

	def change_contrast_spinbox(self):
		self.ui.contrast_spinbox.setValue(self.ui.contrast_slider.value())
		if self.ui.contrast_slider.value() != self.ui.contrast_slider.maximum():
			self.ui.contrast_chbox.setChecked(False)
		else:
			self.ui.contrast_chbox.setChecked(True)
		self.set_all_filters()

	def invert_colors(self):
		if self.ui.invert_chbox.isChecked():
			self.curr_image = ImageOps.invert(self.curr_image)

	def invert_colors_checkbox(self):
		self.set_all_filters()

	def gauss_blur(self):
		if self.ui.gauss_chbox.isChecked():
			self.curr_image = self.curr_image.filter(ImageFilter.GaussianBlur(float(self.ui.gauss_value.value())))

	def gauss_blur_checkbox(self):
		self.set_all_filters()

	def change_mode(self):
		'''TODO
		mono color - set one color and greyscale others
		dual - set one color and color in one color others
		triangle - get 3 most popular colors '''
		if self.ui.mono_radiobtn.isChecked():
			return
		if self.ui.dual_radiobtn.isChecked():
			return
		if self.ui.triangle_radiobtn.isChecked():
			return
		self.update_image()

	def color_modifier(self):
		color = QColorDialog.getColor()
		if(color.isValid()):
			self.ui.first_color_effect.setStyleSheet("background-color: %s" % color.name())
			self.change_background()

	def get_color(self):
		''' get dominant color of an image from NUM_CLUSTERS points'''
		NUM_CLUSTERS = 5
		im = self.curr_image
		im = im.resize((150, 150))      # optional, to reduce time
		ar = np.asarray(im)
		shape = ar.shape
		ar = ar.reshape(np.product(shape[:2]), shape[2]).astype(float)

		#print('finding clusters')
		codes, dist = scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS)
		#print('cluster centres:\n', codes)

		vecs, dist = scipy.cluster.vq.vq(ar, codes)         # assign codes
		counts, bins = np.histogram(vecs, len(codes))    # count occurrences

		index_max = np.argmax(counts)                    # find most frequent
		peak = codes[index_max]
		col = binascii.hexlify(bytearray(int(c) for c in peak)).decode('ascii')
		# print('most frequent is %s (#%s)' % (peak, col))
		self.ui.color_from_image.setStyleSheet("background-color: #%s" % str(col))



if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())






###########################################
### smieci - może coś się kiedyś przyda ###


#color = QGraphicsColorizeEffect(self)		#library QWidgets QGraphicsColorizeEffect
# 	c = self.pixmap.pixel(x,y)
# 	avg = (c.getRed()*0.3 + c.getGreen()*0.6 + c.getBlue()*0.1)/3
# 	colors = QColor(c).getRgbF()
# 	print ("(%s,%s) = %s avg: %s" % (x, y, colors, avg))

# img = QImage(data, image.width, image.height, QImage.Format_A2BGR30_Premultiplied) 			#this thing change whole image into blue-pink-white image xd

'''class Window(QMainWindow):

	def __init__(self):
		super().__init__()
		name_list = ["name", "s_width", "s_height", "b_width", "b_height", "function"]
		set = {zip(name_list, set(enumerate(name_list)))}
		
		set_buttons = [
			[	"Add image", 	20, 	int(height / 2) - 20, 	100, 	40,		self.clickme],
			[	"Save",			20, 	int(height / 2) + 30,	100,	40 	]
		]

		self.setWindowTitle("Paintroom")
		self.setGeometry(400, 200, width, height)
		self.label = QLabel(self)
		
		self.UiComponents()
		self.show()

	def UiComponents(self):
		# for button in self.set_buttons:
		# 	button = QPushButton(button[0], self)
		# 	button.setGeometry(button[1], button[2], button[3], button[4])
		# 	button.clicked.connect(self.clickme)
		for i in self.set_buttons:
			button = QPushButton(i[self.set["name"]], self)
			button.setGeometry(i[self.set["s_width"]], i[self.set["s_height"]], i[self.set["b_width"]], i[self.set["b_height"]]  )
			button.clicked.connect(self.clickme)
		# button = QPushButton("Add image", self)
		# button.setGeometry(20, int(height / 2) + 40, 100, 40  )
		# button.clicked.connect(self.clickme)

	def explore(path):
		# explorer would choke on forward slashes
		path = os.path.normpath(path)

		if os.path.isdir(path):
			subprocess.run([FILEBROWSER_PATH, path])
		elif os.path.isfile(path):
			subprocess.run([FILEBROWSER_PATH, '/select,', os.path.normpath(path)])

	def clickme(self):
		filename, filter = QFileDialog.getOpenFileName(
            parent=self, caption='Open file', filter='*.png')
		self.pixmap = QPixmap(filename)
		self.label.setPixmap(self.pixmap)
		self.label.resize(self.pixmap.width(), self.pixmap.height())
		print("pressed")'''


# def text_setup(window):
# 	helloMsg = QLabel('<h1>Hello World!</h1>', parent=window)
# 	helloMsg.move(20, 1)	

# def buttons_setup(window):

# 	layout = QVBoxLayout()
# 	layout.addWidget(QPushButton('Add image'))
# 	window.setLayout(layout)

# def window_setup():
# 	window = QWidget()
# 	window.setWindowTitle('Paintroom')
# 	window.setGeometry(100, 100, 1000, 700)
# 	window.move(60, 15)
# 	text_setup(window)
# 	buttons_setup(window)	
# 	window.show()
# 	return window


# def main():
# 	try:
		
# 		#Relative Path
# 		img = Image.open("bird.jpg") 

# 		#Saved in the same relative location
# 		img.save("rotated_picture.jpg")


# 		#img = img.show()
# 	except IOError:
# 		pass


# app = QApplication(sys.argv)
# window = window_setup()
# sys.exit(app.exec_())



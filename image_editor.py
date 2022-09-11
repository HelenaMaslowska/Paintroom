#######################################
# Author: Helena Masłowska
# 30.07.2022

from xml.dom.minicompat import EmptyNodeList
from PIL import Image, ImageOps, ImageEnhance, ImageDraw
from PIL.ImageQt import ImageQt			#read and change picture
import sys
import pathlib
import tempfile
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog		#show on the screen
from PySide2.QtGui import QPixmap, QColor, QImage, QIcon
from PySide2.QtCore import QFile , Qt

import os
import subprocess

from numpy import apply_along_axis
from mainwindow import Ui_MainWindow
FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')

width = 1000
height = 800

# pyside2-uic mainwindow.ui -o mainwindow.py

# pixmap - tylko i wylacznie wyswietlanie obrazków
# qt - czyta i zapisuje obrazki
# pil - obrobka obrazu
# self.ui - wszystkie rzeczy związane z plikiem mainwindow
class MainWindow(QMainWindow):
	"""
	TODO
	Understand which path image is edited
	Fix jpg and png bug
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
		self.image: Image = None				# saved but not showed, bring back save pick from apply/start
		self.curr_image: Image = None		
		self.filename = ''
		self.filename_temp = ''
		self.filetype = ''			# type of file, e.g. ['.jpg']
		self.last_apply = ''
		self.background:Image = None

	def set_functions(self):
		#buttons
		self.ui.add_img_btn.clicked.connect(self.add_photo)
		self.ui.save_as_btn.clicked.connect(self.save_as)

		self.ui.transparency_btn.clicked.connect(self.setup_transparency)
		self.ui.white_radiobtn.clicked.connect(self.change_background)
		self.ui.black_radiobtn.clicked.connect(self.change_background)
		self.ui.stripped_radiobtn.clicked.connect(self.change_background)
		self.ui.squares_radiobtn.clicked.connect(self.change_background)

		self.ui.color_chbox.clicked.connect(self.set_color_checkbox)
		self.ui.color_slider.valueChanged.connect(self.change_color_spinbox)
		self.ui.color_spinbox.valueChanged.connect(self.change_color_slider)

		self.ui.light_slider.valueChanged.connect(self.change_light_spinbox)
		self.ui.light_spinbox.valueChanged.connect(self.change_light_slider)

		self.ui.contrast_chbox.clicked.connect(self.set_contrast_checkbox)
		self.ui.contrast_slider.valueChanged.connect(self.change_contrast_spinbox)
		self.ui.contrast_spinbox.valueChanged.connect(self.change_contrast_slider)

		self.ui.apply_btn.clicked.connect(self.apply)
		self.ui.cancel_btn.clicked.connect(self.cancel)

	def save_temp_file(self):
		self.filename_temp= 'paintroom_temp_image' + str(self.filetype[0])
		try:
			print(type(self.image), self.image)
			if(self.filetype[0] == '.jpg'):
				self.image.convert("RGB").save(self.filename_temp)
			self.image.save(self.filename_temp)
		except IOError:
			print("error", self.filename_temp)

	def scale(self, pixmap: QPixmap):
		''' scale pixmap '''
		w, h = self.ui.image_shower.width(), self.ui.image_shower.height()
		if (pixmap.width() >= w):
			pixmap = pixmap.scaledToWidth(w)
		if (pixmap.height() >= h):
			pixmap = pixmap.scaledToHeight(h)
		return pixmap
	
	def merge_images(self, foreground, background):
		background.paste(foreground, (0, 0), foreground)
		return background

	def img_to_pix(self, image: Image):
		''' merge background on pixmap and convert from Image type to pixmap '''
		image = image.convert("RGBA")
		print("img to pix image przed i self.back", image.width, image.height, type(self.background), self.background)
		if(self.background):
			image = self.merge_images(image, self.background)		#background się psuje
		print("img to pix image po ifie", image.width, image.height)
		r, g, b, a = image.split()
		data = Image.merge('RGBA', (b, g, r, a)).tobytes("raw", "RGBA")
		print("img to pix image po", image.width, image.height)
		img = QImage(data, image.width, image.height, QImage.Format_ARGB32) 
		self.pixmap = QPixmap.fromImage(img) 
		self.pixmap = self.scale(self.pixmap)

	def update_image(self, image):
		self.img_to_pix(image)
		self.ui.image_shower.setPixmap(self.pixmap)
		self.ui.image_shower.repaint()

	def apply(self):
		self.image = self.curr_image.copy()
		self.save_temp_file()
		self.update_image(self.image)
		print("applied!")

	def cancel(self):
		self.curr_image = self.image.copy()
		self.save_temp_file()
		self.update_image(self.curr_image)
		print("cancelled!")

	def save_as(self):			
		'''TODO
		IT DOESN'T WORK YET xd
		change type to self.type
		'''
		filepath = QFileDialog.getOpenFileName(self, 'Hey! Select a File')
		self.pixmap.save(self.pixmap)

	def add_photo(self):
		''' add/replace new photo to main screen and show it scaled on image_shower '''
		self.filename, filter = QFileDialog.getOpenFileName( parent=self, caption='Open file', filter="Image files (*.png *.jpg)" )	
		if self.filename != '':
			self.image = Image.open(self.filename)
			self.curr_image = Image.open(self.filename)
			self.filetype = pathlib.Path(self.filename).suffixes
			self.pixmap = QPixmap(self.filename)
			print("dodaję zdj przed skalowaniem", self.pixmap.size())
			self.pixmap = self.scale(self.pixmap)
			print("skaluję zdjecie", self.pixmap.size())
			self.change_background()
			self.update_image(self.curr_image)

	def setup_transparency(self):
		if self.filename:
			if self.ui.transparency_btn.isChecked():
				self.ui.transparency_btn.setChecked(True)
				self.ui.white_radiobtn.setDisabled(True)
				self.ui.black_radiobtn.setDisabled(True)
				self.ui.stripped_radiobtn.setDisabled(True)
				self.ui.squares_radiobtn.setDisabled(True)
				self.background = None	
				print("wlaczam przezroczystość")
			if not self.ui.transparency_btn.isChecked():
				self.ui.transparency_btn.setChecked(False)
				self.ui.white_radiobtn.setEnabled(True)
				self.ui.black_radiobtn.setEnabled(True)
				self.ui.stripped_radiobtn.setEnabled(True)
				self.ui.squares_radiobtn.setEnabled(True)
				print("wyylaczam przezroczystość")
			print("pixmapa po kliknięciu w przycisk przezroczystość", self.pixmap.size())	
			self.update_image(self.curr_image)	

	def change_background(self):			#w tej funkcji jest problem
		if not self.ui.transparency_btn.isChecked():
			print("to jest to", self.curr_image.width, self.curr_image.height)
			w, h =  self.curr_image.width, self.curr_image.height
			self.background = Image.new("RGBA", (w, h))								# pojawia się pusty obrazek
			draw = ImageDraw.Draw(self.background) 									# img1 będzie rysować na obrazku self.background
			if self.ui.white_radiobtn.isChecked() :								# img1 rysuje na self.background prostokąt
				draw.rectangle(xy = [(0, 0), (w, h)], fill = "#ffffff")
			elif self.ui.black_radiobtn.isChecked():
				draw.rectangle(xy = [(0, 0), (w, h)], fill = "#000000")
			elif self.ui.stripped_radiobtn.isChecked():
				print("lol paski", self.ui.how_many_stripes.value())
				draw.rectangle(xy = [(0, 0), (w, h)], fill = "#ffffff")
			elif self.ui.squares_radiobtn.isChecked():
				print(self.ui.how_many_squares.value)				
		self.update_image(self.curr_image)										# aktualizacja obrazka na scenie

	def set_color_checkbox(self):
		''' Greyscale/color on photo with color checkbox
			return nothing'''

		if self.filename == '':
			return 

		if not self.ui.color_chbox.isChecked():
			self.curr_image = ImageOps.grayscale(self.image).convert("RGBA")
			self.ui.color_slider.setValue(self.ui.color_slider.minimum())
			self.update_image(self.curr_image)
		else:
			self.ui.color_slider.setValue(self.ui.color_slider.maximum())		
			self.curr_image = self.image.copy()
			self.update_image(self.image)
		self.change_color_spinbox()

	def set_contrast_checkbox(self):
		if self.ui.contrast_chbox.isChecked():
			enhancer = ImageEnhance.Contrast(self.curr_image)
			factor = 10
			self.curr_image = enhancer.enhance(factor)
			self.ui.contrast_slider.setValue(self.ui.contrast_slider.maximum())
		else:
			enhancer = ImageEnhance.Contrast(self.curr_image)
			factor = 0.1
			self.curr_image = enhancer.enhance(factor)
			self.ui.contrast_slider.setValue(self.ui.contrast_slider.minimum())		
		self.change_contrast_spinbox()
		self.update_image(self.curr_image)

	def change_color_slider(self):
		self.ui.color_slider.setValue(self.ui.color_spinbox.value())

	def change_light_slider(self):
		self.ui.light_slider.setValue(self.ui.light_spinbox.value())

	def change_contrast_slider(self):
		self.ui.contrast_slider.setValue(self.ui.contrast_spinbox.value())

	def change_color_spinbox(self):
		self.ui.color_spinbox.setValue(self.ui.color_slider.value())

	def change_light_spinbox(self):
		self.ui.light_spinbox.setValue(self.ui.light_slider.value())

	def change_contrast_spinbox(self):
		self.ui.contrast_spinbox.setValue(self.ui.contrast_slider.value())


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



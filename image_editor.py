from PIL import Image, ImageOps
from PIL.ImageQt import ImageQt
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QGraphicsColorizeEffect
from PySide2.QtGui import QPixmap, QColor, QImage
from PySide2.QtCore import QFile , Qt

import os
import subprocess
from mainwindow import Ui_MainWindow
FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')

width = 1000
height = 800

if hasattr(Qt, 'AA_EnableHighDpiScaling'):
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)

if hasattr(Qt, 'AA_UseHighDpiPixmaps'):
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
class MainWindow(QMainWindow):
	def __init__(self) -> None:
		super(MainWindow, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.set_functions()
		self.pixmap = ''
		self.image = ''
		self. curr_image = ''
		self.filename = ''

	def set_functions(self):
		self.ui.add_img_btn.clicked.connect(self.add_photo)
		self.ui.save_as_btn.clicked.connect(self.save_as)
		self.ui.color_chbox.clicked.connect(self.set_minmax_color)

	def scale(self, pixmap: QPixmap):
		'''
		Scale Pixmap
		'''
		w, h = self.ui.image_shower.width(), self.ui.image_shower.height()
		if (pixmap.width() >= w):
			pixmap = pixmap.scaledToWidth(w)
		if (pixmap.height() >= h):
			pixmap = pixmap.scaledToHeight(h)
		print(pixmap.width(), pixmap.height())
		return pixmap
	
	def img_to_pix(self, image):
		"""
		important TODO
		add
		"""
		data = image.tobytes("raw", "RGBA") 
		img = QImage(data, image.width, image.height, QImage.Format_ARGB32) 
		pix = QPixmap.fromImage(img) 
		pix = self.scale(pix)
		return pix

	def add_photo(self):
		'''
			Add new photo to main screen and show it (image_shower).
		'''
		filename, filter = QFileDialog.getOpenFileName(
			parent=self, caption='Open file', filter="Image files (*.png *.jpg)")
		pixmap2 = QPixmap(filename)
		self.filename = filename
		if pixmap2.size():
			pixmap2 = self.scale(pixmap2)
			self.pixmap = pixmap2
			print(self.pixmap.size())
		self.ui.image_shower.setPixmap(self.pixmap)
		self.ui.image_shower.repaint()

	def save_as(self):			
		'''TODO
			IT DOESN'T WORK YET xd
		'''
		filepath = QFileDialog.getOpenFileName(self, 'Hey! Select a File')
		self.pixmap.save(self.pixmap)

	def set_minmax_color(self):
		'''TODO
			Set max or min when this is checked or unchecked
			Set color here
		'''

		image = Image.open(self.filename)

		if not self.ui.color_chbox.isChecked():
			print("", self.ui.color_chbox.isChecked())
			#color = QGraphicsColorizeEffect(self)
			#color.setColor(QColor(0, 50, 192))
			#self.pixmap.setGraphicsEffect(color)
			image = ImageOps.grayscale(image).convert("RGBA")
			self.pixmap = self.img_to_pix(image)
			
						# for x in range(50):
						# 	for y in range(50):

						# 		c = self.pixmap.pixel(x,y)
						# 		avg = (c.getRed()*0.3 + c.getGreen()*0.6 + c.getBlue()*0.1)/3
						# 		colors = QColor(c).getRgbF()
						# 		print ("(%s,%s) = %s avg: %s" % (x, y, colors, avg))
			self.ui.image_shower.setPixmap(self.pixmap)
			self.ui.image_shower.repaint()
		else:
			self.pixmap = self.scale(self.pixmap)
			self.ui.image_shower.setPixmap(self.filename)
			self.ui.image_shower.repaint()
			

	def set_color(self):
		return

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


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

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



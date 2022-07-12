from PIL import Image
import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import os
import subprocess
FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')

width = 1000
height = 800

class Window(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Paintroom")
		self.setGeometry(400, 200, width, height)
		self.label = QLabel(self)
		
		self.UiComponents()
		self.show()

	def UiComponents(self):
		button = QPushButton("Add image", self)
		button.setGeometry(20, height / 2 - 20, 100, 40)
		button.clicked.connect(self.clickme)
	
	def explore(path):
		# explorer would choke on forward slashes
		path = os.path.normpath(path)

		if os.path.isdir(path):
			subprocess.run([FILEBROWSER_PATH, path])
		elif os.path.isfile(path):
			subprocess.run([FILEBROWSER_PATH, '/select,', os.path.normpath(path)])

	def clickme(self):
		explore()
		self.pixmap = QPixmap('bird.jpg')
		self.label.setPixmap(self.pixmap)
		self.label.resize(self.pixmap.width(), self.pixmap.height())
		print("pressed")

App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())

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



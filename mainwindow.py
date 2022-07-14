# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1159, 734)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 10, 231, 701))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Settings = QToolBox(self.verticalLayoutWidget_2)
        self.Settings.setObjectName(u"Settings")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 229, 639))
        self.verticalLayoutWidget = QWidget(self.page)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(60, 10, 101, 151))
        self.image_layout = QVBoxLayout(self.verticalLayoutWidget)
        self.image_layout.setObjectName(u"image_layout")
        self.image_layout.setContentsMargins(0, 0, 0, 0)
        self.add_img_btn = QPushButton(self.verticalLayoutWidget)
        self.add_img_btn.setObjectName(u"add_img_btn")

        self.image_layout.addWidget(self.add_img_btn)

        self.save_as_btn = QPushButton(self.verticalLayoutWidget)
        self.save_as_btn.setObjectName(u"save_as_btn")

        self.image_layout.addWidget(self.save_as_btn)

        self.save_btn = QPushButton(self.verticalLayoutWidget)
        self.save_btn.setObjectName(u"save_btn")

        self.image_layout.addWidget(self.save_btn)

        self.verticalLayoutWidget_5 = QWidget(self.page)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(50, 210, 131, 159))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.verticalLayoutWidget_5)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(False)

        self.verticalLayout.addWidget(self.pushButton)

        self.white_radiobtn = QRadioButton(self.verticalLayoutWidget_5)
        self.white_radiobtn.setObjectName(u"white_radiobtn")

        self.verticalLayout.addWidget(self.white_radiobtn)

        self.black_radiobtn = QRadioButton(self.verticalLayoutWidget_5)
        self.black_radiobtn.setObjectName(u"black_radiobtn")

        self.verticalLayout.addWidget(self.black_radiobtn)

        self.stripped_radiobtn = QRadioButton(self.verticalLayoutWidget_5)
        self.stripped_radiobtn.setObjectName(u"stripped_radiobtn")

        self.verticalLayout.addWidget(self.stripped_radiobtn)

        self.squares_radiobtn = QRadioButton(self.verticalLayoutWidget_5)
        self.squares_radiobtn.setObjectName(u"squares_radiobtn")

        self.verticalLayout.addWidget(self.squares_radiobtn)

        self.Settings.addItem(self.page, u"Image")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 229, 639))
        self.verticalLayoutWidget_3 = QWidget(self.page_2)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(20, 10, 181, 611))
        self.settings_layout = QVBoxLayout(self.verticalLayoutWidget_3)
        self.settings_layout.setObjectName(u"settings_layout")
        self.settings_layout.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.verticalLayoutWidget_3)
        self.groupBox.setObjectName(u"groupBox")
        self.color_slider = QSlider(self.groupBox)
        self.color_slider.setObjectName(u"color_slider")
        self.color_slider.setGeometry(QRect(30, 60, 22, 121))
        self.color_slider.setMaximum(100)
        self.color_slider.setOrientation(Qt.Vertical)
        self.light_slider = QSlider(self.groupBox)
        self.light_slider.setObjectName(u"light_slider")
        self.light_slider.setGeometry(QRect(80, 60, 22, 121))
        self.light_slider.setMaximum(100)
        self.light_slider.setValue(50)
        self.light_slider.setOrientation(Qt.Vertical)
        self.dark_slider = QSlider(self.groupBox)
        self.dark_slider.setObjectName(u"dark_slider")
        self.dark_slider.setGeometry(QRect(130, 60, 22, 121))
        self.dark_slider.setMaximum(100)
        self.dark_slider.setValue(50)
        self.dark_slider.setOrientation(Qt.Vertical)
        self.color_spinbox = QSpinBox(self.groupBox)
        self.color_spinbox.setObjectName(u"color_spinbox")
        self.color_spinbox.setGeometry(QRect(20, 190, 42, 26))
        self.light_spinbox = QSpinBox(self.groupBox)
        self.light_spinbox.setObjectName(u"light_spinbox")
        self.light_spinbox.setGeometry(QRect(70, 190, 42, 26))
        self.dark_spinbox = QSpinBox(self.groupBox)
        self.dark_spinbox.setObjectName(u"dark_spinbox")
        self.dark_spinbox.setGeometry(QRect(120, 190, 42, 26))
        self.color_label = QLabel(self.groupBox)
        self.color_label.setObjectName(u"color_label")
        self.color_label.setGeometry(QRect(20, 20, 41, 20))
        self.color_label.setAlignment(Qt.AlignCenter)
        self.light_label = QLabel(self.groupBox)
        self.light_label.setObjectName(u"light_label")
        self.light_label.setGeometry(QRect(70, 20, 41, 20))
        self.light_label.setAlignment(Qt.AlignCenter)
        self.dark_label = QLabel(self.groupBox)
        self.dark_label.setObjectName(u"dark_label")
        self.dark_label.setGeometry(QRect(120, 20, 41, 20))
        self.dark_label.setAlignment(Qt.AlignCenter)
        self.color_chbox = QCheckBox(self.groupBox)
        self.color_chbox.setObjectName(u"color_chbox")
        self.color_chbox.setEnabled(True)
        self.color_chbox.setGeometry(QRect(33, 40, 16, 16))
        self.color_chbox.setLayoutDirection(Qt.LeftToRight)
        self.color_chbox.setAutoFillBackground(False)
        self.color_chbox.setChecked(True)
        self.light_chbox = QCheckBox(self.groupBox)
        self.light_chbox.setObjectName(u"light_chbox")
        self.light_chbox.setEnabled(True)
        self.light_chbox.setGeometry(QRect(84, 40, 16, 16))
        self.light_chbox.setLayoutDirection(Qt.LeftToRight)
        self.light_chbox.setAutoFillBackground(False)
        self.dark_chbox = QCheckBox(self.groupBox)
        self.dark_chbox.setObjectName(u"dark_chbox")
        self.dark_chbox.setEnabled(True)
        self.dark_chbox.setGeometry(QRect(133, 40, 16, 16))
        self.dark_chbox.setLayoutDirection(Qt.LeftToRight)
        self.dark_chbox.setAutoFillBackground(False)
        self.normal_radiobtn = QRadioButton(self.groupBox)
        self.normal_radiobtn.setObjectName(u"normal_radiobtn")
        self.normal_radiobtn.setGeometry(QRect(30, 230, 110, 24))
        self.triangle_radiobtn = QRadioButton(self.groupBox)
        self.triangle_radiobtn.setObjectName(u"triangle_radiobtn")
        self.triangle_radiobtn.setGeometry(QRect(30, 250, 110, 24))
        self.mono_radiobtn = QRadioButton(self.groupBox)
        self.mono_radiobtn.setObjectName(u"mono_radiobtn")
        self.mono_radiobtn.setGeometry(QRect(30, 290, 110, 24))
        self.dual_radiobtn = QRadioButton(self.groupBox)
        self.dual_radiobtn.setObjectName(u"dual_radiobtn")
        self.dual_radiobtn.setGeometry(QRect(30, 270, 110, 24))
        self.random_btn = QPushButton(self.groupBox)
        self.random_btn.setObjectName(u"random_btn")
        self.random_btn.setGeometry(QRect(90, 460, 81, 29))
        self.save_this_btn = QPushButton(self.groupBox)
        self.save_this_btn.setObjectName(u"save_this_btn")
        self.save_this_btn.setGeometry(QRect(10, 460, 81, 29))

        self.settings_layout.addWidget(self.groupBox)

        self.apply_btn = QPushButton(self.verticalLayoutWidget_3)
        self.apply_btn.setObjectName(u"apply_btn")

        self.settings_layout.addWidget(self.apply_btn)

        self.Settings.addItem(self.page_2, u"Options")

        self.verticalLayout_3.addWidget(self.Settings)

        self.image_shower = QLabel(self.centralwidget)
        self.image_shower.setObjectName(u"image_shower")
        self.image_shower.setGeometry(QRect(252, 10, 900, 700))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.Settings.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.add_img_btn.setText(QCoreApplication.translate("MainWindow", u"Add image", None))
        self.save_as_btn.setText(QCoreApplication.translate("MainWindow", u"Save as", None))
        self.save_btn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Transparency", None))
        self.white_radiobtn.setText(QCoreApplication.translate("MainWindow", u"white", None))
        self.black_radiobtn.setText(QCoreApplication.translate("MainWindow", u"black", None))
        self.stripped_radiobtn.setText(QCoreApplication.translate("MainWindow", u"stripped", None))
        self.squares_radiobtn.setText(QCoreApplication.translate("MainWindow", u"squares", None))
        self.Settings.setItemText(self.Settings.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Image", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Color", None))
        self.color_label.setText(QCoreApplication.translate("MainWindow", u"Color", None))
        self.light_label.setText(QCoreApplication.translate("MainWindow", u"Light", None))
        self.dark_label.setText(QCoreApplication.translate("MainWindow", u"Dark", None))
        self.color_chbox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.light_chbox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.dark_chbox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.normal_radiobtn.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.triangle_radiobtn.setText(QCoreApplication.translate("MainWindow", u"Triangle", None))
        self.mono_radiobtn.setText(QCoreApplication.translate("MainWindow", u"Mono", None))
        self.dual_radiobtn.setText(QCoreApplication.translate("MainWindow", u"Dual", None))
        self.random_btn.setText(QCoreApplication.translate("MainWindow", u"Random", None))
        self.save_this_btn.setText(QCoreApplication.translate("MainWindow", u"Save this", None))
        self.apply_btn.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.Settings.setItemText(self.Settings.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Options", None))
        self.image_shower.setText("")
    # retranslateUi


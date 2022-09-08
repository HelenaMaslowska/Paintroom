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
        MainWindow.resize(1156, 739)
        icon = QIcon()
        icon.addFile(u"b.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Settings = QToolBox(self.centralwidget)
        self.Settings.setObjectName(u"Settings")
        self.Settings.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Settings.sizePolicy().hasHeightForWidth())
        self.Settings.setSizePolicy(sizePolicy)
        self.Settings.setMinimumSize(QSize(200, 0))
        self.Settings.setMaximumSize(QSize(200, 16777215))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 200, 640))
        self.groupBox_3 = QGroupBox(self.page)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 160, 181, 164))
        self.groupBox_3.setAlignment(Qt.AlignCenter)
        self.verticalLayout = QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.transparency_btn = QPushButton(self.groupBox_3)
        self.transparency_btn.setObjectName(u"transparency_btn")
        self.transparency_btn.setCheckable(True)
        self.transparency_btn.setChecked(False)

        self.verticalLayout.addWidget(self.transparency_btn)

        self.white_radiobtn = QRadioButton(self.groupBox_3)
        self.white_radiobtn.setObjectName(u"white_radiobtn")
        self.white_radiobtn.setChecked(True)

        self.verticalLayout.addWidget(self.white_radiobtn)

        self.black_radiobtn = QRadioButton(self.groupBox_3)
        self.black_radiobtn.setObjectName(u"black_radiobtn")

        self.verticalLayout.addWidget(self.black_radiobtn)

        self.stripped_radiobtn = QRadioButton(self.groupBox_3)
        self.stripped_radiobtn.setObjectName(u"stripped_radiobtn")

        self.verticalLayout.addWidget(self.stripped_radiobtn)

        self.squares_radiobtn = QRadioButton(self.groupBox_3)
        self.squares_radiobtn.setObjectName(u"squares_radiobtn")

        self.verticalLayout.addWidget(self.squares_radiobtn)

        self.image_groupbox = QGroupBox(self.page)
        self.image_groupbox.setObjectName(u"image_groupbox")
        self.image_groupbox.setGeometry(QRect(9, 9, 181, 131))
        self.image_groupbox.setAlignment(Qt.AlignCenter)
        self.verticalLayoutWidget = QWidget(self.image_groupbox)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 30, 121, 86))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.add_img_btn = QPushButton(self.verticalLayoutWidget)
        self.add_img_btn.setObjectName(u"add_img_btn")

        self.verticalLayout_3.addWidget(self.add_img_btn)

        self.save_as_btn = QPushButton(self.verticalLayoutWidget)
        self.save_as_btn.setObjectName(u"save_as_btn")

        self.verticalLayout_3.addWidget(self.save_as_btn)

        self.save_btn = QPushButton(self.verticalLayoutWidget)
        self.save_btn.setObjectName(u"save_btn")

        self.verticalLayout_3.addWidget(self.save_btn)

        self.Settings.addItem(self.page, u"Image")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 200, 640))
        self.groupBox_2 = QGroupBox(self.page_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 260, 181, 134))
        self.groupBox_2.setMaximumSize(QSize(16777215, 150))
        self.groupBox_2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.normal_radiobtn = QRadioButton(self.groupBox_2)
        self.normal_radiobtn.setObjectName(u"normal_radiobtn")
        self.normal_radiobtn.setChecked(True)

        self.verticalLayout_4.addWidget(self.normal_radiobtn)

        self.triangle_radiobtn = QRadioButton(self.groupBox_2)
        self.triangle_radiobtn.setObjectName(u"triangle_radiobtn")

        self.verticalLayout_4.addWidget(self.triangle_radiobtn)

        self.dual_radiobtn = QRadioButton(self.groupBox_2)
        self.dual_radiobtn.setObjectName(u"dual_radiobtn")

        self.verticalLayout_4.addWidget(self.dual_radiobtn)

        self.mono_radiobtn = QRadioButton(self.groupBox_2)
        self.mono_radiobtn.setObjectName(u"mono_radiobtn")

        self.verticalLayout_4.addWidget(self.mono_radiobtn)

        self.groupBox = QGroupBox(self.page_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 0, 182, 250))
        self.groupBox.setMaximumSize(QSize(16777215, 250))
        self.groupBox.setLayoutDirection(Qt.LeftToRight)
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.color_slider = QSlider(self.groupBox)
        self.color_slider.setObjectName(u"color_slider")
        self.color_slider.setGeometry(QRect(30, 70, 22, 121))
        self.color_slider.setMaximum(100)
        self.color_slider.setValue(100)
        self.color_slider.setOrientation(Qt.Vertical)
        self.light_slider = QSlider(self.groupBox)
        self.light_slider.setObjectName(u"light_slider")
        self.light_slider.setGeometry(QRect(80, 70, 22, 121))
        self.light_slider.setMaximum(100)
        self.light_slider.setValue(50)
        self.light_slider.setOrientation(Qt.Vertical)
        self.contrast_slider = QSlider(self.groupBox)
        self.contrast_slider.setObjectName(u"contrast_slider")
        self.contrast_slider.setGeometry(QRect(130, 70, 22, 121))
        self.contrast_slider.setMaximum(100)
        self.contrast_slider.setValue(50)
        self.contrast_slider.setOrientation(Qt.Vertical)
        self.color_spinbox = QSpinBox(self.groupBox)
        self.color_spinbox.setObjectName(u"color_spinbox")
        self.color_spinbox.setGeometry(QRect(20, 200, 42, 26))
        self.color_spinbox.setMaximum(100)
        self.color_spinbox.setValue(100)
        self.light_spinbox = QSpinBox(self.groupBox)
        self.light_spinbox.setObjectName(u"light_spinbox")
        self.light_spinbox.setGeometry(QRect(70, 200, 42, 26))
        self.light_spinbox.setMaximum(100)
        self.light_spinbox.setValue(50)
        self.contrast_spinbox = QSpinBox(self.groupBox)
        self.contrast_spinbox.setObjectName(u"contrast_spinbox")
        self.contrast_spinbox.setGeometry(QRect(120, 200, 42, 26))
        self.contrast_spinbox.setMaximum(100)
        self.contrast_spinbox.setValue(50)
        self.color_label = QLabel(self.groupBox)
        self.color_label.setObjectName(u"color_label")
        self.color_label.setGeometry(QRect(20, 30, 41, 20))
        self.color_label.setAlignment(Qt.AlignCenter)
        self.light_label = QLabel(self.groupBox)
        self.light_label.setObjectName(u"light_label")
        self.light_label.setGeometry(QRect(70, 30, 41, 20))
        self.light_label.setAlignment(Qt.AlignCenter)
        self.contrast_label = QLabel(self.groupBox)
        self.contrast_label.setObjectName(u"contrast_label")
        self.contrast_label.setGeometry(QRect(110, 30, 61, 20))
        self.contrast_label.setAlignment(Qt.AlignCenter)
        self.color_chbox = QCheckBox(self.groupBox)
        self.color_chbox.setObjectName(u"color_chbox")
        self.color_chbox.setEnabled(True)
        self.color_chbox.setGeometry(QRect(33, 50, 16, 16))
        self.color_chbox.setLayoutDirection(Qt.LeftToRight)
        self.color_chbox.setAutoFillBackground(False)
        self.color_chbox.setChecked(True)
        self.light_chbox = QCheckBox(self.groupBox)
        self.light_chbox.setObjectName(u"light_chbox")
        self.light_chbox.setEnabled(True)
        self.light_chbox.setGeometry(QRect(84, 50, 16, 16))
        self.light_chbox.setLayoutDirection(Qt.LeftToRight)
        self.light_chbox.setAutoFillBackground(False)
        self.contrast_chbox = QCheckBox(self.groupBox)
        self.contrast_chbox.setObjectName(u"contrast_chbox")
        self.contrast_chbox.setEnabled(True)
        self.contrast_chbox.setGeometry(QRect(133, 50, 16, 16))
        self.contrast_chbox.setLayoutDirection(Qt.LeftToRight)
        self.contrast_chbox.setAutoFillBackground(False)
        self.apply_btn = QPushButton(self.page_2)
        self.apply_btn.setObjectName(u"apply_btn")
        self.apply_btn.setGeometry(QRect(10, 430, 91, 24))
        self.cancel_btn = QPushButton(self.page_2)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setGeometry(QRect(110, 430, 75, 24))
        self.Settings.addItem(self.page_2, u"Options")

        self.horizontalLayout.addWidget(self.Settings)

        self.image_shower = QLabel(self.centralwidget)
        self.image_shower.setObjectName(u"image_shower")
        self.image_shower.setMinimumSize(QSize(911, 700))

        self.horizontalLayout.addWidget(self.image_shower)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.Settings.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Paintroom", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"For transparent images", None))
        self.transparency_btn.setText(QCoreApplication.translate("MainWindow", u"Transparency", None))
        self.white_radiobtn.setText(QCoreApplication.translate("MainWindow", u"white", None))
        self.black_radiobtn.setText(QCoreApplication.translate("MainWindow", u"black", None))
        self.stripped_radiobtn.setText(QCoreApplication.translate("MainWindow", u"stripped", None))
        self.squares_radiobtn.setText(QCoreApplication.translate("MainWindow", u"squares", None))
        self.image_groupbox.setTitle(QCoreApplication.translate("MainWindow", u"Image", None))
        self.add_img_btn.setText(QCoreApplication.translate("MainWindow", u"Add image", None))
        self.save_as_btn.setText(QCoreApplication.translate("MainWindow", u"Save as", None))
        self.save_btn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.Settings.setItemText(self.Settings.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Image", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.normal_radiobtn.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.triangle_radiobtn.setText(QCoreApplication.translate("MainWindow", u"Triangle", None))
        self.dual_radiobtn.setText(QCoreApplication.translate("MainWindow", u"Dual", None))
        self.mono_radiobtn.setText(QCoreApplication.translate("MainWindow", u"Mono", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Image beautifier", None))
        self.color_label.setText(QCoreApplication.translate("MainWindow", u"Color", None))
        self.light_label.setText(QCoreApplication.translate("MainWindow", u"Light", None))
        self.contrast_label.setText(QCoreApplication.translate("MainWindow", u"Contrast", None))
        self.color_chbox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.light_chbox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.contrast_chbox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.apply_btn.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.cancel_btn.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.Settings.setItemText(self.Settings.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Options", None))
        self.image_shower.setText("")
    # retranslateUi


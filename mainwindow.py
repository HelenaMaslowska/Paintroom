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
        self.background_groupbox = QGroupBox(self.page)
        self.background_groupbox.setObjectName(u"background_groupbox")
        self.background_groupbox.setGeometry(QRect(10, 160, 181, 261))
        self.background_groupbox.setAlignment(Qt.AlignCenter)
        self.verticalLayout = QVBoxLayout(self.background_groupbox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.transparency_btn = QPushButton(self.background_groupbox)
        self.transparency_btn.setObjectName(u"transparency_btn")
        self.transparency_btn.setEnabled(True)
        self.transparency_btn.setMouseTracking(False)
        self.transparency_btn.setCheckable(True)
        self.transparency_btn.setChecked(True)

        self.verticalLayout.addWidget(self.transparency_btn)

        self.white_hor_layout = QHBoxLayout()
        self.white_hor_layout.setObjectName(u"white_hor_layout")
        self.white_radiobtn = QRadioButton(self.background_groupbox)
        self.white_radiobtn.setObjectName(u"white_radiobtn")
        self.white_radiobtn.setEnabled(False)
        self.white_radiobtn.setCheckable(True)
        self.white_radiobtn.setChecked(False)

        self.white_hor_layout.addWidget(self.white_radiobtn)


        self.verticalLayout.addLayout(self.white_hor_layout)

        self.color_hor_layout = QHBoxLayout()
        self.color_hor_layout.setObjectName(u"color_hor_layout")
        self.color_radiobtn = QRadioButton(self.background_groupbox)
        self.color_radiobtn.setObjectName(u"color_radiobtn")
        self.color_radiobtn.setEnabled(False)

        self.color_hor_layout.addWidget(self.color_radiobtn)

        self.picked_only_color = QPushButton(self.background_groupbox)
        self.picked_only_color.setObjectName(u"picked_only_color")
        self.picked_only_color.setMaximumSize(QSize(25, 25))
        self.picked_only_color.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.color_hor_layout.addWidget(self.picked_only_color)


        self.verticalLayout.addLayout(self.color_hor_layout)

        self.stripped_hor_layout = QHBoxLayout()
        self.stripped_hor_layout.setSpacing(13)
        self.stripped_hor_layout.setObjectName(u"stripped_hor_layout")
        self.stripped_hor_layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.stripped_radiobtn = QRadioButton(self.background_groupbox)
        self.stripped_radiobtn.setObjectName(u"stripped_radiobtn")
        self.stripped_radiobtn.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.stripped_radiobtn.sizePolicy().hasHeightForWidth())
        self.stripped_radiobtn.setSizePolicy(sizePolicy1)

        self.stripped_hor_layout.addWidget(self.stripped_radiobtn)

        self.stripes_btn = QPushButton(self.background_groupbox)
        self.stripes_btn.setObjectName(u"stripes_btn")
        self.stripes_btn.setEnabled(False)
        self.stripes_btn.setMaximumSize(QSize(25, 25))
        self.stripes_btn.setCheckable(True)

        self.stripped_hor_layout.addWidget(self.stripes_btn)

        self.how_many_stripes = QSpinBox(self.background_groupbox)
        self.how_many_stripes.setObjectName(u"how_many_stripes")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.how_many_stripes.sizePolicy().hasHeightForWidth())
        self.how_many_stripes.setSizePolicy(sizePolicy2)
        self.how_many_stripes.setMinimum(2)
        self.how_many_stripes.setMaximum(99)
        self.how_many_stripes.setValue(4)

        self.stripped_hor_layout.addWidget(self.how_many_stripes)


        self.verticalLayout.addLayout(self.stripped_hor_layout)

        self.squares_hor_layout = QHBoxLayout()
        self.squares_hor_layout.setSpacing(57)
        self.squares_hor_layout.setObjectName(u"squares_hor_layout")
        self.squares_radiobtn = QRadioButton(self.background_groupbox)
        self.squares_radiobtn.setObjectName(u"squares_radiobtn")
        self.squares_radiobtn.setEnabled(False)

        self.squares_hor_layout.addWidget(self.squares_radiobtn)

        self.how_many_squares = QSpinBox(self.background_groupbox)
        self.how_many_squares.setObjectName(u"how_many_squares")
        self.how_many_squares.setMinimum(2)
        self.how_many_squares.setMaximum(999)
        self.how_many_squares.setValue(2)

        self.squares_hor_layout.addWidget(self.how_many_squares)


        self.verticalLayout.addLayout(self.squares_hor_layout)

        self.colors_hor_layout = QHBoxLayout()
        self.colors_hor_layout.setSpacing(5)
        self.colors_hor_layout.setObjectName(u"colors_hor_layout")
        self.colors_hor_layout.setContentsMargins(30, -1, 30, -1)
        self.picked_color1 = QPushButton(self.background_groupbox)
        self.picked_color1.setObjectName(u"picked_color1")
        self.picked_color1.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.picked_color1.sizePolicy().hasHeightForWidth())
        self.picked_color1.setSizePolicy(sizePolicy2)
        self.picked_color1.setMaximumSize(QSize(25, 25))
        self.picked_color1.setAutoFillBackground(False)
        self.picked_color1.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.picked_color1.setCheckable(False)
        self.picked_color1.setChecked(False)
        self.picked_color1.setAutoRepeatDelay(300)

        self.colors_hor_layout.addWidget(self.picked_color1)

        self.swap_btn = QPushButton(self.background_groupbox)
        self.swap_btn.setObjectName(u"swap_btn")
        self.swap_btn.setMaximumSize(QSize(50, 25))

        self.colors_hor_layout.addWidget(self.swap_btn)

        self.picked_color2 = QPushButton(self.background_groupbox)
        self.picked_color2.setObjectName(u"picked_color2")
        sizePolicy2.setHeightForWidth(self.picked_color2.sizePolicy().hasHeightForWidth())
        self.picked_color2.setSizePolicy(sizePolicy2)
        self.picked_color2.setMaximumSize(QSize(25, 25))
        self.picked_color2.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.picked_color2.setCheckable(False)
        self.picked_color2.setChecked(False)

        self.colors_hor_layout.addWidget(self.picked_color2)


        self.verticalLayout.addLayout(self.colors_hor_layout)

        self.image_groupbox = QGroupBox(self.page)
        self.image_groupbox.setObjectName(u"image_groupbox")
        self.image_groupbox.setGeometry(QRect(9, 9, 181, 131))
        self.image_groupbox.setAlignment(Qt.AlignCenter)
        self.verticalLayoutWidget = QWidget(self.image_groupbox)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 30, 121, 86))
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
        self.color_slider.setMinimum(1)
        self.color_slider.setMaximum(100)
        self.color_slider.setValue(50)
        self.color_slider.setOrientation(Qt.Vertical)
        self.light_slider = QSlider(self.groupBox)
        self.light_slider.setObjectName(u"light_slider")
        self.light_slider.setGeometry(QRect(80, 70, 22, 121))
        self.light_slider.setMinimum(1)
        self.light_slider.setMaximum(100)
        self.light_slider.setValue(50)
        self.light_slider.setOrientation(Qt.Vertical)
        self.contrast_slider = QSlider(self.groupBox)
        self.contrast_slider.setObjectName(u"contrast_slider")
        self.contrast_slider.setGeometry(QRect(130, 70, 22, 121))
        self.contrast_slider.setMinimum(1)
        self.contrast_slider.setMaximum(100)
        self.contrast_slider.setValue(50)
        self.contrast_slider.setOrientation(Qt.Vertical)
        self.color_spinbox = QSpinBox(self.groupBox)
        self.color_spinbox.setObjectName(u"color_spinbox")
        self.color_spinbox.setGeometry(QRect(20, 200, 42, 26))
        self.color_spinbox.setMaximum(100)
        self.color_spinbox.setValue(50)
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
        self.color_chbox.setChecked(False)
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

        self.Settings.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Paintroom", None))
        self.background_groupbox.setTitle(QCoreApplication.translate("MainWindow", u"Background", None))
        self.transparency_btn.setText(QCoreApplication.translate("MainWindow", u"Transparency", None))
        self.white_radiobtn.setText(QCoreApplication.translate("MainWindow", u"white", None))
        self.color_radiobtn.setText(QCoreApplication.translate("MainWindow", u"color", None))
        self.picked_only_color.setText("")
        self.stripped_radiobtn.setText(QCoreApplication.translate("MainWindow", u"stripped   ", None))
        self.stripes_btn.setText(QCoreApplication.translate("MainWindow", u"||", None))
        self.squares_radiobtn.setText(QCoreApplication.translate("MainWindow", u"squares", None))
        self.picked_color1.setText("")
        self.swap_btn.setText(QCoreApplication.translate("MainWindow", u"swap", None))
        self.picked_color2.setText("")
        self.image_groupbox.setTitle(QCoreApplication.translate("MainWindow", u"Image", None))
        self.add_img_btn.setText(QCoreApplication.translate("MainWindow", u"Add image", None))
        self.save_as_btn.setText(QCoreApplication.translate("MainWindow", u"Save as", None))
        self.save_btn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.Settings.setItemText(self.Settings.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Image", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Color effects", None))
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


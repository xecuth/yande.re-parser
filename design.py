# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Design.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 293)
        MainWindow.setMinimumSize(QtCore.QSize(640, 293))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 71, 21))
        self.label.setText("Tags:")
        self.label.setObjectName("label")
        self.TagsQueryLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.TagsQueryLineEdit.setGeometry(QtCore.QRect(70, 30, 191, 22))
        self.TagsQueryLineEdit.setObjectName("TagsQueryLineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 71, 21))
        self.label_2.setText("Page count:")
        self.label_2.setObjectName("label_2")
        self.PageCountSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.PageCountSpinBox.setGeometry(QtCore.QRect(100, 70, 81, 22))
        self.PageCountSpinBox.setMinimum(1)
        self.PageCountSpinBox.setMaximum(10000)
        self.PageCountSpinBox.setObjectName("PageCountSpinBox")
        self.explicitContentCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.explicitContentCheckBox.setGeometry(QtCore.QRect(20, 110, 111, 31))
        self.explicitContentCheckBox.setObjectName("explicitContentCheckBox")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 210, 591, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.StartPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.StartPushButton.setGeometry(QtCore.QRect(330, 20, 281, 51))
        self.StartPushButton.setObjectName("StartPushButton")
        self.ButtonDescriptionLabel = QtWidgets.QLabel(self.centralwidget)
        self.ButtonDescriptionLabel.setGeometry(QtCore.QRect(330, 100, 281, 31))
        self.ButtonDescriptionLabel.setText("")
        self.ButtonDescriptionLabel.setObjectName("ButtonDescriptionLabel")
        self.ProgressBarDescriptionLabel = QtWidgets.QLabel(self.centralwidget)
        self.ProgressBarDescriptionLabel.setGeometry(QtCore.QRect(20, 240, 591, 21))
        self.ProgressBarDescriptionLabel.setText("")
        self.ProgressBarDescriptionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ProgressBarDescriptionLabel.setObjectName("ProgressBarDescriptionLabel")
        self.ChooseFolderPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.ChooseFolderPushButton.setGeometry(QtCore.QRect(20, 150, 141, 28))
        self.ChooseFolderPushButton.setObjectName("ChooseFolderPushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Yande.re Parser"))
        self.explicitContentCheckBox.setText(_translate("MainWindow", "Explicit content"))
        self.StartPushButton.setText(_translate("MainWindow", "START"))
        self.ChooseFolderPushButton.setText(_translate("MainWindow", "Choose Folder"))

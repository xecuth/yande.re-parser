# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'des.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 200)
        MainWindow.setMinimumSize(QtCore.QSize(800, 200))
        MainWindow.setMaximumSize(QtCore.QSize(800, 200))
        font = QtGui.QFont()
        font.setFamily("DejaVu Math TeX Gyre")
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTip("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tagsQueryLabel = QtWidgets.QLabel(self.centralwidget)
        self.tagsQueryLabel.setGeometry(QtCore.QRect(10, 20, 101, 21))
        font = QtGui.QFont()
        font.setFamily("DejaVu Math TeX Gyre")
        font.setPointSize(9)
        self.tagsQueryLabel.setFont(font)
        self.tagsQueryLabel.setStatusTip("")
        self.tagsQueryLabel.setWhatsThis("")
        self.tagsQueryLabel.setObjectName("tagsQueryLabel")
        self.tagsQueryLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.tagsQueryLineEdit.setGeometry(QtCore.QRect(110, 20, 201, 22))
        font = QtGui.QFont()
        font.setFamily("DejaVu Math TeX Gyre")
        font.setPointSize(8)
        self.tagsQueryLineEdit.setFont(font)
        self.tagsQueryLineEdit.setText("")
        self.tagsQueryLineEdit.setObjectName("tagsQueryLineEdit")
        self.pageCountLabel = QtWidgets.QLabel(self.centralwidget)
        self.pageCountLabel.setGeometry(QtCore.QRect(10, 60, 101, 21))
        font = QtGui.QFont()
        font.setFamily("DejaVu Math TeX Gyre")
        font.setPointSize(9)
        self.pageCountLabel.setFont(font)
        self.pageCountLabel.setObjectName("pageCountLabel")
        self.pageCountSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.pageCountSpinBox.setGeometry(QtCore.QRect(110, 60, 71, 22))
        font = QtGui.QFont()
        font.setFamily("DejaVu Math TeX Gyre")
        self.pageCountSpinBox.setFont(font)
        self.pageCountSpinBox.setMinimum(1)
        self.pageCountSpinBox.setMaximum(10000)
        self.pageCountSpinBox.setObjectName("pageCountSpinBox")
        self.savePathLabel = QtWidgets.QLabel(self.centralwidget)
        self.savePathLabel.setGeometry(QtCore.QRect(10, 100, 101, 21))
        font = QtGui.QFont()
        font.setFamily("DejaVu Math TeX Gyre")
        font.setPointSize(9)
        self.savePathLabel.setFont(font)
        self.savePathLabel.setObjectName("savePathLabel")
        self.savePathLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.savePathLineEdit.setGeometry(QtCore.QRect(110, 100, 131, 22))
        self.savePathLineEdit.setText("")
        self.savePathLineEdit.setReadOnly(True)
        self.savePathLineEdit.setObjectName("savePathLineEdit")
        self.explicitContentCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.explicitContentCheckBox.setGeometry(QtCore.QRect(230, 140, 16, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.explicitContentCheckBox.setFont(font)
        self.explicitContentCheckBox.setText("")
        self.explicitContentCheckBox.setTristate(False)
        self.explicitContentCheckBox.setObjectName("explicitContentCheckBox")
        self.explicitContentLabel = QtWidgets.QLabel(self.centralwidget)
        self.explicitContentLabel.setGeometry(QtCore.QRect(10, 140, 211, 21))
        font = QtGui.QFont()
        font.setFamily("DejaVu Math TeX Gyre")
        font.setPointSize(9)
        self.explicitContentLabel.setFont(font)
        self.explicitContentLabel.setObjectName("explicitContentLabel")
        self.savePathPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.savePathPushButton.setGeometry(QtCore.QRect(240, 100, 71, 21))
        self.savePathPushButton.setObjectName("savePathPushButton")
        self.startPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.startPushButton.setGeometry(QtCore.QRect(460, 20, 181, 41))
        self.startPushButton.setObjectName("startPushButton")
        self.stopPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopPushButton.setGeometry(QtCore.QRect(640, 20, 111, 41))
        self.stopPushButton.setObjectName("stopPushButton")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(460, 70, 331, 21))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.statusLabel = QtWidgets.QLabel(self.centralwidget)
        self.statusLabel.setGeometry(QtCore.QRect(460, 100, 291, 41))
        self.statusLabel.setStyleSheet("line-height: 8px;")
        self.statusLabel.setText("")
        self.statusLabel.setTextFormat(QtCore.Qt.AutoText)
        self.statusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statusLabel.setObjectName("statusLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuAbout = QtWidgets.QMenu(self.menuBar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menuBar)
        self.actionAuthor = QtWidgets.QAction(MainWindow)
        self.actionAuthor.setObjectName("actionAuthor")
        self.actionAuthor_2 = QtWidgets.QAction(MainWindow)
        self.actionAuthor_2.setObjectName("actionAuthor_2")
        self.menuAbout.addAction(self.actionAuthor_2)
        self.menuBar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "yande.re_parser"))
        self.tagsQueryLabel.setToolTip(_translate("MainWindow", "Tags for search; ex.: azur_lane wallpaper"))
        self.tagsQueryLabel.setText(_translate("MainWindow", "Tags Query:"))
        self.pageCountLabel.setToolTip(_translate("MainWindow", "Number of pages for parsing; ex.: 5"))
        self.pageCountLabel.setText(_translate("MainWindow", "Page count:"))
        self.savePathLabel.setToolTip(_translate("MainWindow", "Choosing a save path; ex.: D:\\temp"))
        self.savePathLabel.setText(_translate("MainWindow", "Save to:"))
        self.explicitContentLabel.setToolTip(_translate("MainWindow", "Explicit content confirm; may not work"))
        self.explicitContentLabel.setText(_translate("MainWindow", "Download explicit content:"))
        self.savePathPushButton.setText(_translate("MainWindow", "Choose..."))
        self.startPushButton.setToolTip(_translate("MainWindow", "Start parsing"))
        self.startPushButton.setText(_translate("MainWindow", "START"))
        self.stopPushButton.setToolTip(_translate("MainWindow", "Stop parsing"))
        self.stopPushButton.setText(_translate("MainWindow", "STOP"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionAuthor.setText(_translate("MainWindow", "Author"))
        self.actionAuthor_2.setText(_translate("MainWindow", "Author"))

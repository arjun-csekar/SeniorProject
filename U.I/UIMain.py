# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIMain.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from UIAdvanced import Ui_AdvancedWindow
import main
from functools import partial
from PIL import Image
import os

class Ui_MainWindow(object):

    def clickable(self, widget):
        class Filter(QtCore.QObject):
            clicked = QtCore.pyqtSignal()
            def eventFilter(self, obj, event):
                if obj == widget:
                    if event.type() == QtCore.QEvent.MouseButtonRelease:
                        if obj.rect().contains(event.pos()):
                            self.clicked.emit()
                            return True
                return False
        filter = Filter(widget)
        widget.installEventFilter(filter)
        return filter.clicked

    def convert(self):
        main.main.start_convert(1, 100, fname, 10, 10, 1)
        self.btn_advanced.setDisabled(False)
        self.btn_save.setDisabled(False)

    def open_advanced(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AdvancedWindow()
        self.ui.setupUi(self.window, fname)
        self.window.show()

    def open_image(self):
        global fname
        fname, _ = QtWidgets.QFileDialog.getOpenFileName()
        lb = self.imagePreview
        lb.setPixmap(QtGui.QPixmap(fname))
        lb.setScaledContents(True)
        lb.show()
        self.btn_convert.setDisabled(False)

    def display_image(self, name):
        if (name == "preview"):
            os.startfile(fname)
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_upload = QtWidgets.QPushButton(self.centralwidget)
        self.btn_upload.setGeometry(QtCore.QRect(100, 480, 75, 23))
        self.btn_upload.setObjectName("btn_upload")
        self.btn_upload.clicked.connect(self.open_image)
        self.btn_convert = QtWidgets.QPushButton(self.centralwidget)
        self.btn_convert.setGeometry(QtCore.QRect(260, 480, 75, 23))
        self.btn_convert.setObjectName("btn_convert")
        self.btn_convert.clicked.connect(self.convert)
        self.btn_convert.setEnabled(False)
        self.btn_save = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save.setGeometry(QtCore.QRect(420, 480, 75, 23))
        self.btn_save.setObjectName("btn_save")
        self.btn_save.setEnabled(False)
        self.btn_advanced = QtWidgets.QPushButton(self.centralwidget)
        self.btn_advanced.setGeometry(QtCore.QRect(260, 550, 75, 23))
        self.btn_advanced.setObjectName("btn_advanced")
        self.btn_advanced.clicked.connect(self.open_advanced)
        self.btn_advanced.setEnabled(False)
        self.imagePreview = QtWidgets.QLabel(self.centralwidget)
        self.imagePreview.setGeometry(QtCore.QRect(20, 50, 250, 400))
        self.imagePreview.setText("")
        self.imagePreview.setObjectName("imagePreview")
        self.clickable(self.imagePreview).connect(partial(self.display_image, "preview"))
        self.textPreview = QtWidgets.QLabel(self.centralwidget)
        self.textPreview.setGeometry(QtCore.QRect(330, 50, 250, 400))
        self.textPreview.setText("")
        self.textPreview.setObjectName("textPreview")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_upload.setText(_translate("MainWindow", "Upload Image"))
        self.btn_convert.setText(_translate("MainWindow", "Convert"))
        self.btn_save.setText(_translate("MainWindow", "Save"))
        self.btn_advanced.setText(_translate("MainWindow", "Advanced"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


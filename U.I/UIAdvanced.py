# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIAdvanced.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from main import main
from functools import partial
from PIL import Image
import os

class Ui_AdvancedWindow(object):

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
    
    def edge_change(self):
        value = str(self.edgeSlider.value())
        self.lb_edge.setText(value)

    def width_change(self):
        value = str(self.boundingSlider.value())
        self.lb_width.setText(value)

    def height_change(self):
        value = str(self.horizontalSlider.value())
        self.lb_height.setText(value)

    def noise_change(self):
        value = str(self.deNoiseSlider.value())
        self.lb_denoise.setText(value)

    def refresh(self):
        lb1 = self.deNoiseImage
        lb2 = self.edgeDetectionImage
        lb3 = self.boundingImage
        lb1.setPixmap(QtGui.QPixmap('data/greyscale-after.png'))
        lb2.setPixmap(QtGui.QPixmap('data/edge.png'))
        lb3.setPixmap(QtGui.QPixmap('data/contour.png'))
        lb1.setScaledContents(True)
        lb2.setScaledContents(True)
        lb3.setScaledContents(True)
        lb1.show()
        lb2.show()
        lb3.show()

    def edge_run(self, i):
        val = i
        noiseVal = (int(self.lb_denoise.text()))
        value = (int(self.lb_edge.text()))
        value_width = (int(self.lb_width.text()))
        value_height = (int(self.lb_height.text()))
        print("edge_run")
        main.run(val, value, self.filePath, value_width, value_height, noiseVal)
        self.refresh()

    def display_image(self, name):
        if (name == "noise"):
            os.startfile('data\\greyscale-after.png')
        elif (name == "edge"):
            os.startfile('data\\edge.png')
        elif (name == "box"):
            os.startfile('data\\contour.png')

    def setupUi(self, AdvancedWindow, path):
        self.filePath = path
        AdvancedWindow.setObjectName("AdvancedWindow")
        AdvancedWindow.resize(800, 949)
        self.centralwidget = QtWidgets.QWidget(AdvancedWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_denoise = QtWidgets.QPushButton(self.centralwidget)
        self.btn_denoise.setGeometry(QtCore.QRect(160, 430, 75, 23))
        self.btn_denoise.setObjectName("btn_denoise")
        self.btn_denoise.clicked.connect(partial(self.edge_run, 1))
        self.boundingImage = QtWidgets.QLabel(self.centralwidget)
        self.boundingImage.setGeometry(QtCore.QRect(250, 500, 291, 361))
        self.boundingImage.setObjectName("boundingImage")
        self.clickable(self.boundingImage).connect(partial(self.display_image, "box"))
        self.btn_bounding = QtWidgets.QPushButton(self.centralwidget)
        self.btn_bounding.setGeometry(QtCore.QRect(350, 870, 75, 23))
        self.btn_bounding.setObjectName("btn_bounding")
        self.btn_bounding.clicked.connect(partial(self.edge_run, 3))
        self.deNoiseImage = QtWidgets.QLabel(self.centralwidget)
        self.deNoiseImage.setGeometry(QtCore.QRect(60, 60, 291, 361))
        self.deNoiseImage.setObjectName("deNoiseImage")
        self.clickable(self.deNoiseImage).connect(partial(self.display_image, "noise"))
        self.btn_edge = QtWidgets.QPushButton(self.centralwidget)
        self.btn_edge.setGeometry(QtCore.QRect(540, 430, 75, 23))
        self.btn_edge.setObjectName("btn_edge")
        self.btn_edge.clicked.connect(partial(self.edge_run, 2))
        self.edgeDetectionImage = QtWidgets.QLabel(self.centralwidget)
        self.edgeDetectionImage.setGeometry(QtCore.QRect(430, 60, 291, 361))
        self.edgeDetectionImage.setObjectName("edgeDetectionImage")
        self.clickable(self.edgeDetectionImage).connect(partial(self.display_image, "edge"))
        self.deNoiseSlider = QtWidgets.QSlider(self.centralwidget)
        self.deNoiseSlider.setGeometry(QtCore.QRect(120, 30, 160, 22))
        self.deNoiseSlider.setMinimum(1)
        self.deNoiseSlider.setMaximum(3)
        self.deNoiseSlider.setProperty("value", 1)
        self.deNoiseSlider.setOrientation(QtCore.Qt.Horizontal)
        self.deNoiseSlider.setObjectName("deNoiseSlider")
        self.deNoiseSlider.valueChanged.connect(self.noise_change)
        self.edgeSlider = QtWidgets.QSlider(self.centralwidget)
        self.edgeSlider.setGeometry(QtCore.QRect(500, 30, 160, 22))
        self.edgeSlider.setMaximum(250)
        self.edgeSlider.setProperty("value", 100)
        self.edgeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.edgeSlider.setObjectName("edgeSlider")
        self.edgeSlider.valueChanged.connect(self.edge_change)
        self.boundingSlider = QtWidgets.QSlider(self.centralwidget)
        self.boundingSlider.setGeometry(QtCore.QRect(260, 470, 111, 22))
        self.boundingSlider.setMaximum(50)
        self.boundingSlider.setProperty("value", 10)
        self.boundingSlider.setOrientation(QtCore.Qt.Horizontal)
        self.boundingSlider.setObjectName("boundingSlider")
        self.boundingSlider.valueChanged.connect(self.width_change)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 470, 31, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(430, 470, 41, 16))
        self.label_2.setObjectName("label_2")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(470, 470, 160, 22))
        self.horizontalSlider.setMaximum(50)
        self.horizontalSlider.setProperty("value", 10)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.valueChanged.connect(self.height_change)
        self.lb_denoise = QtWidgets.QLabel(self.centralwidget)
        self.lb_denoise.setGeometry(QtCore.QRect(90, 30, 21, 16))
        self.lb_denoise.setObjectName("lb_denoise")
        self.lb_edge = QtWidgets.QLabel(self.centralwidget)
        self.lb_edge.setGeometry(QtCore.QRect(460, 30, 31, 16))
        self.lb_edge.setObjectName("lb_edge")
        self.lb_width = QtWidgets.QLabel(self.centralwidget)
        self.lb_width.setGeometry(QtCore.QRect(180, 470, 31, 16))
        self.lb_width.setObjectName("lb_width")
        self.lb_height = QtWidgets.QLabel(self.centralwidget)
        self.lb_height.setGeometry(QtCore.QRect(400, 470, 31, 16))
        self.lb_height.setObjectName("lb_height")
        AdvancedWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AdvancedWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        AdvancedWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AdvancedWindow)
        self.statusbar.setObjectName("statusbar")
        AdvancedWindow.setStatusBar(self.statusbar)
        self.refresh()

        self.retranslateUi(AdvancedWindow)
        QtCore.QMetaObject.connectSlotsByName(AdvancedWindow)

    def retranslateUi(self, AdvancedWindow):
        _translate = QtCore.QCoreApplication.translate
        AdvancedWindow.setWindowTitle(_translate("AdvancedWindow", "MainWindow"))
        self.btn_denoise.setText(_translate("AdvancedWindow", "Run"))
        self.btn_bounding.setText(_translate("AdvancedWindow", "Run"))
        self.btn_edge.setText(_translate("AdvancedWindow", "Run"))
        self.label.setText(_translate("AdvancedWindow", "Width:"))
        self.label_2.setText(_translate("AdvancedWindow", "Height:"))
        self.lb_denoise.setText(_translate("AdvancedWindow", "0"))
        self.lb_edge.setText(_translate("AdvancedWindow", "100"))
        self.lb_width.setText(_translate("AdvancedWindow", "10"))
        self.lb_height.setText(_translate("AdvancedWindow", "10"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AdvancedWindow = QtWidgets.QMainWindow()
    ui = Ui_AdvancedWindow()
    ui.setupUi(AdvancedWindow)
    AdvancedWindow.show()
    sys.exit(app.exec_())


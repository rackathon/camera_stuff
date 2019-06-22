# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui',
# licensing of 'main_window.ui' applies.
#
# Created: Fri Jun 21 21:05:54 2019
#      by: pyside2-uic  running on PySide2 5.12.4
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout.addWidget(self.groupBox)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(0, -1, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.facial_recognition_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.facial_recognition_button.sizePolicy().hasHeightForWidth())
        self.facial_recognition_button.setSizePolicy(sizePolicy)
        self.facial_recognition_button.setObjectName("facial_recognition_button")
        self.gridLayout.addWidget(self.facial_recognition_button, 3, 0, 1, 1)
        self.raw_video_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.raw_video_button.sizePolicy().hasHeightForWidth())
        self.raw_video_button.setSizePolicy(sizePolicy)
        self.raw_video_button.setObjectName("raw_video_button")
        self.gridLayout.addWidget(self.raw_video_button, 0, 0, 1, 1)
        self.background_removal_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.background_removal_button.sizePolicy().hasHeightForWidth())
        self.background_removal_button.setSizePolicy(sizePolicy)
        self.background_removal_button.setObjectName("background_removal_button")
        self.gridLayout.addWidget(self.background_removal_button, 1, 0, 1, 1)
        self.edge_detection_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edge_detection_button.sizePolicy().hasHeightForWidth())
        self.edge_detection_button.setSizePolicy(sizePolicy)
        self.edge_detection_button.setObjectName("edge_detection_button")
        self.gridLayout.addWidget(self.edge_detection_button, 2, 0, 1, 1)
        self.vignette_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vignette_button.sizePolicy().hasHeightForWidth())
        self.vignette_button.setSizePolicy(sizePolicy)
        self.vignette_button.setObjectName("vignette_button")
        self.gridLayout.addWidget(self.vignette_button, 4, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("MainWindow", "Live Video", None, -1))
        self.facial_recognition_button.setText(QtWidgets.QApplication.translate("MainWindow", "Facial Recognition", None, -1))
        self.raw_video_button.setText(QtWidgets.QApplication.translate("MainWindow", "Raw Video", None, -1))
        self.background_removal_button.setText(QtWidgets.QApplication.translate("MainWindow", "Background Removal", None, -1))
        self.edge_detection_button.setText(QtWidgets.QApplication.translate("MainWindow", "Edge Detection", None, -1))
        self.vignette_button.setText(QtWidgets.QApplication.translate("MainWindow", "Vignette", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


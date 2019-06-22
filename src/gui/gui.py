import sys

from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtGui import QPalette
from PySide2 import QtCore, QtGui

from main_window import Ui_MainWindow
from pprint import pprint




class MyWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connect_widgets()

    def connect_widgets(self):
        self.facial_recognition_button.clicked.connect(self.facial_recognition)
        self.raw_video_button.clicked.connect(self.raw_video)
        self.edge_detection_button.clicked.connect(self.edge_detection)
        self.vignette_button.clicked.connect(self.vignette)
        self.background_removal_button.clicked.connect(self.background_removal)

    def facial_recognition(self):
        print("facial recognition")

    def raw_video(self):
        print("raw video")

    def vignette(self):
        print("This is viggy viggy viggy can't you see")

    def edge_detection(self):
        print("sometimes you words just hypnotise me")

    def background_removal(self):
        print("I don't know the rest of the words")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    palette = QPalette()
    palette.setColor(QPalette.Window, QtGui.QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, QtCore.Qt.white)
    palette.setColor(QPalette.Base, QtGui.QColor(15, 15, 15))
    palette.setColor(QPalette.AlternateBase, QtGui.QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, QtCore.Qt.white)
    palette.setColor(QPalette.ToolTipText, QtCore.Qt.white)
    palette.setColor(QPalette.Text, QtCore.Qt.white)
    palette.setColor(QPalette.Button, QtGui.QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, QtCore.Qt.white)
    palette.setColor(QPalette.BrightText, QtCore.Qt.red)

    palette.setColor(QPalette.Highlight, QtGui.QColor(142, 45, 197).lighter())
    palette.setColor(QPalette.HighlightedText, QtCore.Qt.black)
    app.setPalette(palette)

    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

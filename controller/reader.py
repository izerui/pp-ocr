import os

from PySide6 import QtGui, QtCore
from PySide6.QtCore import Slot, QRect, QEvent
from PySide6.QtGui import QAction, QImage, Qt, QPainter, QPen
from PySide6.QtWidgets import QMainWindow, QFileDialog, QVBoxLayout

from ui.ui_reader import Ui_MainWindow


class Reader(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.scrollArea.installEventFilter(self)

    @Slot()
    def actionTriggered(self, *args):
        action: QAction = args[0]
        if action.objectName() == 'openFileAction':
            fileDialog = QFileDialog()
            files = fileDialog.getOpenFileName(self, '选择要识别的图片', os.getcwd())
            print(repr(files[0]))
            # jpg = QtGui.QPixmap(files[0]).scaled(self.label.width(), self.label.height())
            jpg = QtGui.QPixmap(files[0])
            self.label.clear()
            self.label.setPixmap(jpg)
            self.label.setMaximumWidth(jpg.width())
            self.label.setMaximumHeight(jpg.height())
            self.label.setCursor(Qt.CrossCursor)

    def eventFilter(self, source, event):
        if source == self.scrollArea:
            # print(event.type())
            if event.type() == QEvent.Type.Wheel:
                self.label.update()
        return super().eventFilter(source, event)
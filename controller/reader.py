import imghdr
import os
from pathlib import Path
from tempfile import gettempdir

import fitz
from PySide6 import QtGui, QtCore
from PySide6.QtCore import Slot, QEvent
from PySide6.QtGui import QAction, QImage, Qt, QPixmap
from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from fitz import Page, Annot, Pixmap
from paddleocr import PaddleOCR

from controller.model import ThumbModel
from ui.ui_reader import Ui_MainWindow


class Reader(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.scrollArea.installEventFilter(self)
        self.label.imageRectGrabed.connect(self.ocrImage)
        self.ocr = PaddleOCR(use_angle_cls=True, lang="ch")
        self.splitter.setSizes([20000, 70000])
        self.splitter_2.setSizes([60000, 20000])
        self.imagePaths = []

    @Slot()
    def actionTriggered(self, *args):
        self.imagePaths = []
        action: QAction = args[0]
        if action.objectName() == 'openFileAction':
            # 先清空预览
            self.listView.setModel(ThumbModel())
            fileDialog = QFileDialog()
            files = fileDialog.getOpenFileName(self, '选择要识别的图片', os.getcwd())
            if imghdr.what(files[0]):
                self.renderImage(files[0])
            elif str(files[0]).lower().endswith('.pdf'):
                self.renderPdf(files[0])

    # 渲染图片
    def renderImage(self, f):
        self.imagePaths = [f]
        # 设置分页预览
        self.listView.setModel(ThumbModel(self.imagePaths))
        # img = check_img(files[0])
        # jpg = QtGui.QPixmap(files[0]).scaled(self.label.width(), self.label.height())
        png = QtGui.QPixmap(self.imagePaths[0])
        self.renderPixmap(png)

    def renderPdf(self, f):
        _fname = os.path.splitext(os.path.basename(f))[0]
        self.imagePaths = []
        with fitz.open(f) as pdf:
            tmpFolder = os.path.join(gettempdir(), '.{}'.format(hash(os.times())))
            os.makedirs(tmpFolder)
            for index in range(pdf.page_count):
                page: Annot = pdf.load_page(index)
                pixmap: Pixmap = page.get_pixmap()
                _tmpPath = str(Path(tmpFolder) / f'{_fname}_{index}.png')
                pixmap.save(_tmpPath)
                print(_tmpPath)
                self.imagePaths.append(_tmpPath)

                # fitz pixmap 转成 qt QImage
                # image_format = QImage.Format_RGBA8888 if pixmap.alpha else QImage.Format_RGB888
                # page_image = QImage(pixmap.samples, pixmap.width, pixmap.height, pixmap.stride, image_format)

        # 设置分页预览
        self.listView.setModel(ThumbModel(self.imagePaths))
        # jpg = QtGui.QPixmap(files[0]).scaled(self.label.width(), self.label.height())
        # qpixmap = QPixmap.fromImage(self.images[0])
        png = QtGui.QPixmap(self.imagePaths[0])
        self.renderPixmap(png)

    def renderPixmap(self, pixmap):
        self.label.clear()
        self.label.setPixmap(pixmap)
        self.label.setMaximumWidth(pixmap.width())
        self.label.setMaximumHeight(pixmap.height())
        self.label.setCursor(Qt.CrossCursor)

    # 监听滚动区域的事件
    def eventFilter(self, source, event):
        if source == self.scrollArea:
            # print(event.type())
            if event.type() == QEvent.Type.Wheel:
                self.label.update()
        return super().eventFilter(source, event)

    @Slot()
    def ocrImage(self, pixmap: QPixmap):
        ba = QtCore.QByteArray()
        buff = QtCore.QBuffer(ba)
        buff.open(QtCore.QIODevice.WriteOnly)
        pixmap.save(buff, "PNG")
        result = self.ocr.ocr(ba.data(), cls=True)
        QMessageBox.information(None, '解析结果', repr(result))

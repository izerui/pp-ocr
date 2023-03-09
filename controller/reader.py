import imghdr
import os
from itertools import groupby

import fitz
from PySide6 import QtGui, QtCore
from PySide6.QtCore import Slot, QEvent, QObject
from PySide6.QtGui import QAction, Qt, QPixmap, QImage, QMouseEvent
from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from paddleocr import PaddleOCR

from controller.model import ThumbModel
from ui.ui_reader import Ui_MainWindow


class Reader(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.scrollArea.installEventFilter(self)
        self.label.imageRectGrabed.connect(self.ocrImage)
        # self.label.mouseMoveAndFlag.connect(self.mouseMoveAndFlag)
        self.ocr = PaddleOCR(use_angle_cls=True, lang="ch")
        self.splitter.setSizes([20000, 70000])
        self.splitter_2.setSizes([60000, 20000])
        # 选择的文件
        self.file = None
        # 当前页
        self.pageIndex = 0
        # 缩放比例： 100：原比例 200：放大2倍 50：缩小一倍
        self.zoom = 100

    # @Slot()
    # def mouseMoveAndFlag(self, event: QMouseEvent):
    #     if event.x() > self.scrollArea.width() + self.scrollArea.x():
    #         self.scrollArea.horizontalScrollBar().setValue(event.x())
    #     if event.y() > self.scrollArea.height() + self.scrollArea.y():
    #         self.scrollArea.verticalScrollBar().setValue(event.y())
    #     # print('scroll', self.scrollArea.width() + self.scrollArea.x(), self.scrollArea.height() + self.scrollArea.y())
    #     # print('mouse', event.x(), event.y())
    #     pass

    @Slot()
    def actionTriggered(self, *args):
        action: QAction = args[0]
        if action.objectName() == 'openFileAction':
            # 先清空预览
            self.listView.setModel(ThumbModel())
            fileDialog = QFileDialog()
            files = fileDialog.getOpenFileName(self, '选择要识别的图片', os.getcwd())
            self.file = files[0] if files[0] else None
            self.render()
        elif action.objectName() == 'largeAction':
            self.zoom += 10
            self.zoom = max(self.zoom, 10)
            self.zoom = min(self.zoom, 300)
            self.render()
        elif action.objectName() == 'smallAction':
            self.zoom -= 10
            self.zoom = max(self.zoom, 10)
            self.zoom = min(self.zoom, 300)
            self.render()
        self.showStatusTip()


    def showStatusTip(self):
        if self.file:
            self.statusbar.showMessage(f'文件: {self.file}    当前页: {self.pageIndex + 1}    缩放比例: {self.zoom}%')


    # 渲染image或者pdf
    def render(self):
        if not self.file:
            return
        if imghdr.what(self.file):
            self.renderImage()
        elif str(self.file).lower().endswith('.pdf'):
            self.renderPdf()

    # 渲染图片
    def renderImage(self):
        # 设置分页预览
        model = ThumbModel(self.file, 1, 0)
        self.listView.setModel(model)
        self.listView.setCurrentIndex(model.index(0))
        # img = check_img(files[0])
        # jpg = QtGui.QPixmap(files[0]).scaled(self.label.width(), self.label.height())
        jpg = QtGui.QPixmap(self.file)
        self.renderPixmap(jpg)

    def renderPdf(self):
        with fitz.open(self.file) as pdf:
            if self.pageIndex + 1 > pdf.page_count:
                self.pageIndex = pdf.page_count - 1
            page = pdf.load_page(self.pageIndex)
            # 设置缩放比例
            mat = fitz.Matrix(self.zoom/100.0, self.zoom/100.0)
            # alpha 不透明
            pixmap = page.get_pixmap(matrix=mat, alpha=False)
            image_format = QImage.Format_RGBA8888 if pixmap.alpha else QImage.Format_RGB888
            page_image = QImage(pixmap.samples, pixmap.width, pixmap.height, pixmap.stride, image_format)
            # 设置分页预览
            model = ThumbModel(self.file, pdf.page_count, 0)
            self.listView.setModel(model)
            self.listView.setCurrentIndex(model.index(self.pageIndex))
        # jpg = QtGui.QPixmap(files[0]).scaled(self.label.width(), self.label.height())
        qpixmap = QPixmap.fromImage(page_image)
        self.renderPixmap(qpixmap)

    def renderPixmap(self, pixmap):
        self.label.clear()
        self.label.setPixmap(pixmap)
        self.label.setMaximumWidth(pixmap.width())
        self.label.setMaximumHeight(pixmap.height())
        self.label.setCursor(Qt.CrossCursor)
        # 点击每页恢复滚动条
        # self.scrollArea.horizontalScrollBar().setValue(0)
        # self.scrollArea.verticalScrollBar().setValue(0)
        self.showStatusTip()

    # 监听滚动区域的事件
    def eventFilter(self, source: QObject, event: QEvent):
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
        self.textBrowser.append(f'{result} \n')
        # QMessageBox.information(None, '解析结果', repr(result))

    @Slot()
    def pageClicked(self):
        for rowIndex, group in groupby(self.listView.selectedIndexes(), lambda x: x.row()):
            self.pageIndex = rowIndex
        self.renderPdf()

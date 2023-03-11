import PySide6.QtGui
from PySide6 import QtCore
from PySide6.QtCore import QRect, Qt, Signal, QPoint
from PySide6.QtGui import QPainter, QPen, QPixmap, QIcon, QCursor
from PySide6.QtWidgets import QLabel, QMenu


class ImageLabel(QLabel):
    # 矩形绘画完毕信号
    pixmap_rect_ocr = Signal(QPixmap, QRect)

    # 拖拽矩形鼠标移动信号
    mouseMoveAndFlag = Signal(PySide6.QtGui.QMouseEvent)

    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)
        self.setCursor(Qt.CrossCursor)
        # 鼠标按下状态
        self.flag = False
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.contextMenu = QMenu()
        self.customContextMenuRequested.connect(self.showContextMenu)
        self.ocrAction = self.contextMenu.addAction(QIcon(u":/logo/logo/ocr.png"), '开始识别')
        self.ocrAction.triggered.connect(self.beginOcr)

    # 单击鼠标按下事件
    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent) -> None:
        # barHeight = self.bar.height()
        if event.button() == QtCore.Qt.LeftButton:
            self.startPoint = event.pos()
            self.endPoint = None
            self.flag = True

    # 鼠标移动事件
    def mouseMoveEvent(self, event: PySide6.QtGui.QMouseEvent) -> None:
        # 如果鼠标未释放按下状态，则开始记录endpoint
        if self.flag:
            self.endPoint = event.pos()
            # 触发组件重绘
            self.update()

    # 鼠标释放事件
    def mouseReleaseEvent(self, event: PySide6.QtGui.QMouseEvent) -> None:
        self.beginOcr()
            # pixmap.save('pixmap.png')
        # 鼠标按下状态设置为False
        # self.flag = False
        # self.startPoint = None
        # self.endPoint = None
        # 释放鼠标使矩形区域消失
        # self.update()

    # 绘制事件
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent) -> None:
        super().paintEvent(event)
        # 根据初始点击坐标和当前鼠标坐标绘制矩形
        if self.flag and self.endPoint:  # 鼠标按下移动中、画布重新显示时
            # print('绘制坐标:', self.startPoint, self.endPoint)
            rect = QRect(self.startPoint, self.endPoint)
            painter = QPainter(self)
            painter.setPen(QPen(Qt.red, 1, Qt.SolidLine))
            painter.drawRect(rect)
        # self.drawSampleRects()

    def clear(self) -> None:
        super().clear()
        self.flag = False
        self.startPoint = None
        self.endPoint = None

    # 开始ocr识别
    def beginOcr(self):
        pixmap = self.getRectRegionPixmap()
        if pixmap:
            # print('pixmap: ', pixmap.width(), pixmap.height())
            self.pixmap_rect_ocr.emit(pixmap, QRect(self.startPoint, self.endPoint))

    # 获取选择框区域内的图片
    def getRectRegionPixmap(self):
        if not self.flag:
            return None
        if not self.startPoint or not self.endPoint:
            return None
        # print('point: ', self.startPoint, self.endPoint)
        grabX = min(self.startPoint.x(), self.endPoint.x())
        grabY = min(self.startPoint.y(), self.endPoint.y())
        grabW = abs(self.endPoint.x() - self.startPoint.x())
        grabH = abs(self.endPoint.y() - self.startPoint.y())
        # 矩形区域大于10 * 10 才返回截屏区域
        if grabW < 10 and grabH < 10:
            return None
        pixmap = self.screen().grabWindow(self.winId(), grabX, grabY, grabW, grabH)
        return pixmap

    def drawSampleRects(self):
        rect = QRect(QPoint(20, 20), QPoint(200, 200))
        painter = QPainter(self)
        painter.setPen(QPen(Qt.red, 1, Qt.SolidLine))
        painter.drawRect(rect)
    # def clear(self) -> None:
    #     super().clear()
    #     self.flag = False

    def showContextMenu(self):
        self.contextMenu.move(QCursor.pos())
        self.contextMenu.show()

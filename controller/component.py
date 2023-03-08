import PySide6.QtGui
from PySide6.QtCore import QRect, Qt, QPoint
from PySide6.QtGui import QPainter, QPen
from PySide6.QtWidgets import QLabel


class ImageLabel(QLabel):

    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)
        self.setCursor(Qt.CrossCursor)
        self.flag = False

    # 鼠标移动事件
    def mouseMoveEvent(self, event: PySide6.QtGui.QMouseEvent) -> None:
        # barHeight = self.bar.height()
        if self.flag:
            self.endPoint = event.pos()
            # 触发组件重绘
            self.update()

    # 鼠标释放事件
    # def mouseReleaseEvent(self, event: PySide6.QtGui.QMouseEvent) -> None:
        # self.flag = False
        # print(self.startPoint, self.endPoint)

    # 绘制事件
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent) -> None:
        super().paintEvent(event)
        # 根据初始点击坐标和当前鼠标坐标绘制矩形
        if self.flag:  # 鼠标按下移动中、画布重新显示时
            print('绘制坐标:', self.startPoint, self.endPoint)
            rect = QRect(self.startPoint, self.endPoint)
            painter = QPainter(self)
            painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
            painter.drawRect(rect)

    # 单击鼠标触发事件
    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent) -> None:
        # barHeight = self.bar.height()
        self.startPoint = event.pos()
        self.endPoint = QPoint(0, 0)
        self.flag = True

    def clear(self) -> None:
        super().clear()
        self.flag = False


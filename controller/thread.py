from queue import Queue

from PySide6 import QtCore
from PySide6.QtCore import QThread, Signal, QRect
from PySide6.QtGui import QPixmap
from paddleocr import PaddleOCR

ocr = PaddleOCR(use_angle_cls=True, lang="ch")


class OcrThread(QThread):
    ocr_result = Signal(object, object)

    def __init__(self, pixmap: QPixmap, rect: QRect):
        super().__init__()
        self.pixmap = pixmap
        self.rect = rect

    def run(self) -> None:
        ba = QtCore.QByteArray()
        buff = QtCore.QBuffer(ba)
        buff.open(QtCore.QIODevice.WriteOnly)
        self.pixmap.save(buff, "PNG")
        result = ocr.ocr(ba.data(), cls=True)
        self.ocr_result.emit(result, self.rect)

from queue import Queue

import cv2
from PySide6 import QtCore
from PySide6.QtCore import QThread, Signal, QRect
from PySide6.QtGui import QPixmap, QImage
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
        result = ocr.ocr(ba.data(), det=True, rec=True, cls=True)
        self.ocr_result.emit(result, self.rect)

class QrcodeThread(QThread):

    qrcode_result = Signal(object)

    def __init__(self, pixmap: QPixmap):
        super().__init__()
        self.pixmap = pixmap

    def run(self) -> None:
        # 将QPixmap转换为OpenCV的图像格式
        qimage = self.pixmap.toImage()
        width = qimage.width()
        height = qimage.height()
        bytes_per_line = qimage.bytesPerLine()

        image_buffer = qimage.constBits()

        import numpy as np
        image = np.frombuffer(image_buffer, dtype=np.uint8).reshape((height, width, int(bytes_per_line / width)))

        # 将RGB图像转换为灰度图像
        gray = cv2.cvtColor(image, cv2.COLOR_RGBA2GRAY)  # 或者使用 COLOR_BGR2GRAY
        # 识别二维码
        import pyzbar.pyzbar as pyzbar
        decoded_objects = pyzbar.decode(gray)

        # 返回解码结果
        results = []
        for obj in decoded_objects:
            result = {
                'type': obj.type,
                'data': obj.data.decode('utf-8')
            }
            results.append(result)
        self.qrcode_result.emit(results)



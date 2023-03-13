from queue import Queue

import cv2
from PySide6 import QtCore
from PySide6.QtCore import QThread, Signal, QRect
from PySide6.QtGui import QPixmap, QImage
from paddleocr import PaddleOCR

ocr = PaddleOCR(use_angle_cls=True, lang="ch")


class OcrThread(QThread):
    ocr_result = Signal(list, object)

    def __init__(self, pixmap: QPixmap, rect: QRect):
        super().__init__()
        self.pixmap = pixmap
        self.rect = rect

    def run(self) -> None:
        ba = QtCore.QByteArray()
        buff = QtCore.QBuffer(ba)
        buff.open(QtCore.QIODevice.WriteOnly)
        self.pixmap.save(buff, "PNG")
        # 数组第一层: 每页
        # 数组第二层: 每文字块
        #       文字块[0]: 文字块的最小矩形区域的坐标(左上、右上、左下、右下)
        #       文字块[1]: 文字块的内容及可信度(介于0 到 1之间)
        result = ocr.ocr(ba.data(), det=True, rec=True, cls=True)
        self.ocr_result.emit(self.parsing_result(result), self.rect)

    def parsing_result(self, results):
        pages = []
        for pageIndex, pageBlock in enumerate(results):
            page = {
                "lines": []
            }
            for textLine, textBlock in enumerate(pageBlock):
                page['lines'].append({
                    "content": textBlock[1][0],
                    # 可信度 介于 0到1之间
                    "rate": float(textBlock[1][1]),
                    # 相对坐标区域 x0,y0为左上角坐标、x1,y1为右下角坐标
                    "rect": {
                        "x0": float(min(min(min(textBlock[0][0][0], textBlock[0][1][0]), textBlock[0][2][0]),
                                        textBlock[0][3][0])),
                        "y0": float(min(min(min(textBlock[0][0][1], textBlock[0][1][1]), textBlock[0][2][1]),
                                        textBlock[0][3][1])),
                        "x1": float(max(max(max(textBlock[0][0][0], textBlock[0][1][0]), textBlock[0][2][0]),
                                        textBlock[0][3][0])),
                        "y1": float(max(max(max(textBlock[0][0][1], textBlock[0][1][1]), textBlock[0][2][1]),
                                        textBlock[0][3][1]))
                    }
                })
            pages.append(page)
        return pages

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



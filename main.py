# This is a sample Python script.
import sys

# import paddle
# import cv2
from PySide6.QtWidgets import QApplication

from controller.reader import Reader

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # paddle.utils.run_check()
    app = QApplication(sys.argv)
    reader = Reader()
    reader.show()
    # app.setStyle(QStyleFactory.create('macOS'))
    sys.exit(app.exec())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

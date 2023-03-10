import os
import tempfile
import threading
from pathlib import Path
from typing import Union, Any

import PySide6.QtCore
import fitz
from PySide6.QtCore import QAbstractListModel, Qt
from PySide6.QtGui import QPixmap
from fitz import Pixmap


class ThumbModel(QAbstractListModel):

    def __init__(self, file: str = None, page_num: int = 0):
        super().__init__()
        self.file = file
        self.page_num = page_num
        # self.thumbnailThread = threading.Thread(target=self.generate_thumbnail)
        # self.thumbnailThread.start()
        self.thumbnail_page_files = []
        self.generate_thumbnail()

    def generate_thumbnail(self):
        tmp_folder = tempfile.mkdtemp()
        print(tmp_folder)
        dir_name, full_file_name = os.path.split(self.file)
        file_base_name = os.path.splitext(full_file_name)[0]
        tmp_file_base_name = str(Path(tmp_folder) / file_base_name)
        with fitz.open(self.file) as doc:
            for pageIndex in range(doc.page_count):
                page = doc.load_page(pageIndex)
                # 设置缩放比例, 指定像素宽高 如果按比例： 则为 x/100.0 、 y/100.0
                mat = fitz.Matrix(100 / page.bound()[2], 100 / page.bound()[3])
                # alpha 不透明
                pixmap: Pixmap = page.get_pixmap(matrix=mat, alpha=False)
                pixmap.save(f'{tmp_file_base_name}_{pageIndex}.png', 'png')
                self.thumbnail_page_files.append(f'{tmp_file_base_name}_{pageIndex}.png')

    def data(self, index: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex],
             role: int = ...) -> Any:
        row = index.row()
        col = index.column()
        if role == Qt.DisplayRole:
            return None # f'第{row + 1}页'
        elif role == Qt.DecorationRole:
            if self.thumbnail_page_files and row in range(len(self.thumbnail_page_files)) and self.thumbnail_page_files[row]:
                return QPixmap(self.thumbnail_page_files[row])
            return None

    def rowCount(self, parent: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex] = ...) -> int:
        return self.page_num

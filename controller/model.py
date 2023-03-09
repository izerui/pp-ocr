from typing import Union, Any

import PySide6.QtCore
from PySide6.QtCore import QAbstractListModel, Qt


class ThumbModel(QAbstractListModel):

    def __init__(self, images=[]):
        super().__init__()
        self.images = images

    def data(self, index: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex],
             role: int = ...) -> Any:
        row = index.row()
        col = index.column()
        if role == Qt.DisplayRole:
            return f'第{row + 1}页'
        elif role == Qt.DecorationRole:
            return None

    def rowCount(self, parent: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex] = ...) -> int:
        return len(self.images)

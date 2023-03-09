from typing import Union, Any

import PySide6.QtCore
from PySide6.QtCore import QAbstractListModel, Qt


class ThumbModel(QAbstractListModel):

    def __init__(self, file: str = None, total: int = 0, page: int = -1):
        super().__init__()
        self.file = file
        self.total = total
        self.page = page


    def getFile(self) -> str:
        return self.file

    def getTotal(self) -> int:
        return self.total

    def getPage(self) -> int:
        return self.page

    def data(self, index: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex],
             role: int = ...) -> Any:
        row = index.row()
        col = index.column()
        if role == Qt.DisplayRole:
            return f'第{row + 1}页'
        elif role == Qt.DecorationRole:
            return None

    def rowCount(self, parent: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex] = ...) -> int:
        return self.total

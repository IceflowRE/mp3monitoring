from PyQt5.QtCore import QAbstractTableModel, QVariant, Qt
from PyQt5.QtGui import QColor

import core


class DataTableModel(QAbstractTableModel):
    def __init__(self, header_data, parent=None):
        super(DataTableModel, self).__init__(parent)
        self.header_data = header_data

    def rowCount(self, parent=None, *args, **kwargs):
        return len(core.job_dict)

    def columnCount(self, parent=None, *args, **kwargs):
        return len(self.header_data)

    def flags(self, index):
        if not index.isValid():
            return None
        if index.column() == 0:  # active role checkable
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEnabled
        else:
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def headerData(self, col, orientation, role=None):
        """
        Header data is bold and centered.
        :param col:
        :param orientation:
        :param role:
        :return:
        """
        if orientation == Qt.Horizontal:
            if role == Qt.DisplayRole:
                return QVariant(self.header_data[col])
            elif role == Qt.TextAlignmentRole:
                return QVariant(Qt.AlignCenter)
            elif role == Qt.FontRole:
                font = self.parent().font()
                font.setBold(True)
                font.setPointSize(self.parent().font().pointSize() + 1)
                return QVariant(font)
        return QVariant()

    def data(self, index, role=None):
        if not index.isValid():
            return QVariant()

        job = list(core.job_dict.values())[index.row()]
        if role == Qt.TextAlignmentRole:
            return QVariant(Qt.AlignCenter)
        elif role == Qt.TextColorRole:
            if index.column() > 0 and not job.active:
                return QVariant(QColor(135, 135, 135))
        elif role == Qt.DisplayRole:
            if index.column() == 0:
                return QVariant(job.active)
            elif index.column() == 1:
                return QVariant(str(job.source_dir))
            elif index.column() == 2:
                return QVariant(str(job.target_dir))
            elif index.column() == 3:
                return QVariant(job.status)
            elif index.column() == 4:
                return QVariant(job.pause_s)

        return QVariant()

    def setData(self, index, any, role=None):
        pass

    def sort(self, p_int, order=None):
        pass

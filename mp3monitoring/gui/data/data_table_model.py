from PyQt5.QtCore import QAbstractTableModel, QVariant, Qt

import core


class DataTableModel(QAbstractTableModel):
    def __init__(self, header_data, parent=None):
        super(DataTableModel, self).__init__(parent)
        self.header_data = header_data  # active, source, target, status

    def rowCount(self, parent=None, *args, **kwargs):
        return len(core.job_dict)

    def columnCount(self, parent=None, *args, **kwargs):
        return len(self.header_data)

    def data(self, index, role=None):
        if not index.isValid():
            return QVariant()
        elif role != Qt.DisplayRole:
            return QVariant()

        job = list(core.job_dict.values())[index.row()]
        if index.row() == 0:
            item = QVariant(job.active)
        elif index.row() == 1:
            item = QVariant(job.source)
        elif index.row() == 2:
            item = QVariant(job.target)
        elif index.row() == 3:
            item = QVariant(job.status)
        else:
            item = QVariant('???')

        return item

    def setData(self, index, Any, role=None):
        pass  # TODO

    def headerData(self, col, orientation, role=None):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self.header_data[col])
        return QVariant()

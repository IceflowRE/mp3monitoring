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
        if index.column() == 0:  # active is editable
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable
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
                return self.header_data[col]
            elif role == Qt.TextAlignmentRole:
                return Qt.AlignCenter
            elif role == Qt.FontRole:
                font = self.parent().font()
                font.setBold(True)
                font.setPointSize(self.parent().font().pointSize() + 1)
                return font
        return QVariant()

    def data(self, index, role=None):
        if not index.isValid():
            return QVariant()

        job = list(core.job_dict.values())[index.row()]
        if role == Qt.TextAlignmentRole:
            return Qt.AlignCenter
        elif role == Qt.ForegroundRole:
            if index.column() > 0 and not job.active:
                return QColor(135, 135, 135)
        elif role == Qt.DisplayRole:
            if index.column() == 0:
                return job.active
            elif index.column() == 1:
                return str(job.source_dir)
            elif index.column() == 2:
                return str(job.target_dir)
            elif index.column() == 3:
                return job.status
            elif index.column() == 4:
                return job.pause_s

        return QVariant()

    def setData(self, index, data, role=None):
        # edit active state of threads
        if index.column() == 0:
            if not isinstance(data, bool):
                return False
            job = list(core.job_dict.values())[index.row()]
            job.active = data
            #self.dataChanged().emit()
            if data:
                job.thread.start()
            return True
        return False

    def sort(self, p_int, order=None):
        pass

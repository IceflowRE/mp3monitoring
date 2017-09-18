from PyQt5.QtCore import QAbstractTableModel, QTimer, QVariant, Qt
from PyQt5.QtGui import QColor

import core
from data import dynamic


class DataTableModel(QAbstractTableModel):
    def __init__(self, header_data, parent=None):
        super(DataTableModel, self).__init__(parent)
        self.header_data = header_data

        self.__timer = QTimer()
        self.__timer.timeout.connect(self.update_model)
        self.__timer.start(dynamic.GUI_UPDATE_TIME)

    def rowCount(self, parent=None, *args, **kwargs):
        return len(core.job_dict)

    def columnCount(self, parent=None, *args, **kwargs):
        return len(self.header_data)

    def flags(self, index):
        if not index.isValid():
            return None
        job = list(core.job_dict.values())[index.row()]
        if job.stopping and job.thread.isAlive():  # if thread is alive and should be stopped
            if index.column() == 0:  # active checkbox is not interactable
                return Qt.ItemIsSelectable
            return Qt.ItemIsSelectable | Qt.ItemIsEnabled
        else:
            if index.column() == 4:  # active and pause is editable
                return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable
            return Qt.ItemIsSelectable | Qt.ItemIsEnabled

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
        if role == Qt.ImCurrentSelection:
            print(index.row(), index.column())
        if role == Qt.TextAlignmentRole:
            return Qt.AlignCenter
        elif role == Qt.EditRole:
            if index.column() == 0:
                return not job.stopping
            elif index.column() == 4:
                return job.pause
        elif role == Qt.ForegroundRole:
            if job.stopping and job.thread.isAlive():
                return QColor(190, 190, 0)
            elif not job.thread.isAlive():
                return QColor(160, 0, 0)
            else:
                return QColor(0, 160, 0)
        elif role == Qt.DisplayRole:
            if index.column() == 0:  # return negate stopping
                return not job.stopping
            elif index.column() == 1:
                return str(job.source_dir)
            elif index.column() == 2:
                return str(job.target_dir)
            elif index.column() == 3:
                return job.status
            elif index.column() == 4:
                return str(job.pause)

        return QVariant()

    def setData(self, index, data, role=None):
        if index.column() == 0:  # edit active state
            if not isinstance(data, bool):
                return False
            job = list(core.job_dict.values())[index.row()]
            if data:
                if not job.start():
                    job.startup = False
                    return False
                job.startup = True
            else:
                job.startup = False
                job.stop()
            self.update_model()
            return True
        elif index.column() == 4:  # edit pause
            if not isinstance(data, int):
                return False
            job = list(core.job_dict.values())[index.row()]
            job.change_pause(data)
            self.update_model()
            return True
        return False

    def sort(self, p_int, order=None):
        pass

    def update_model(self):
        """
        Updates table, except pause column.
        :return:
        """
        self.layoutAboutToBeChanged.emit()
        # "- 2" TODO: work around for prevent that the pause values gets switched back to origin while editing
        self.dataChanged.emit(self.createIndex(0, 0), self.createIndex(self.rowCount(0), self.columnCount(0) - 2))
        self.layoutChanged.emit()

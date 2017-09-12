from PyQt5.QtCore import QAbstractTableModel, QVariant, Qt


class MyTableModel(QAbstractTableModel):
    def __init__(self, data, header_data, parent=None):
        QAbstractTableModel.__init__(self, parent)
        self.header_data = header_data
        self.data = data

    def rowCount(self, parent=None, *args, **kwargs):
        return len(self.data)

    def columnCount(self, parent=None, *args, **kwargs):
        if len(self.data) > 0:
            return len(self.data[0])
        return 0

    def data(self, index, role=None):
        if not index.isValid():
            return QVariant()
        elif role != Qt.DisplayRole:
            return QVariant()
        return QVariant(self.data[index.row()][index.column()])

    def setData(self, index, Any, role=None):
        pass         # not sure what to put here

    def headerData(self, col, orientation, role=None):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self.header_data[col])
        return QVariant()

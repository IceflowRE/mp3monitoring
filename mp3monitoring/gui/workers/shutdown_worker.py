import mp3monitoring.core
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot


class ShutdownWorker(QObject):
    finished = pyqtSignal()
    status = pyqtSignal(str)

    @pyqtSlot(name='shutdown')
    def shutdown(self):  # a slot takes no params
        mp3monitoring.core.shutdown(signal=self.status)
        self.finished.emit()

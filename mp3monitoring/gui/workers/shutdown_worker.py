from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot

import core


class ShutdownWorker(QObject):
    finished = pyqtSignal()
    status = pyqtSignal(str)

    @pyqtSlot(name='shutdown')
    def shutdown(self):  # a slot takes no params
        core.shutdown(signal=self.status)
        self.finished.emit()

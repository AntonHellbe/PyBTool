from PyQt4.QtCore import *
from output import Ui_MainWindow

class TestThread(QThread):

    def __init__(self, bt_instance):
        QThread.__init__(self)
        self.bt_instance = bt_instance
    
    def __del__(self):
        self.wait()
    
    def run(self):
        nearby_devices = self.bt_instance.discover_devices(duration=2, flush_cache=True, lookup_names=True)
        self.emit(SIGNAL("finished(PyQt_PyObject)"), nearby_devices)
    



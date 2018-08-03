import sys
from PyQt4 import QtGui
from PyQt4.QtCore import *
from main_window import Ui_MainWindow
from bluetoothservice import PyBluetooth
from BTReceiver import BTReceiverThread
from TestThread import TestThread

class Main(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect_btn_listeners()
        self.bt = PyBluetooth(self)
        self.worker_thread = BTReceiverThread()
        self.test_thread = TestThread(self.bt.bluetooth)
        self.connect(self.worker_thread, SIGNAL("appendToTerminal(QString)"), self.appendToTerminal)
        self.connect(self.test_thread, SIGNAL("finished(PyQt_PyObject)"), self.sendToUI)

    def connect_btn_listeners(self):
        self.ui.btn_scan.clicked.connect(self.callback_scan_button)
        self.ui.btn_connect.clicked.connect(self.callback_connect_button)
    

    def callback_connect_button(self):
        selected_device = str(self.ui.cb_device_connect.currentText())
        selected_device = selected_device.split("-")[0].strip()
        device_addr = self.bt.get_device_addr(selected_device)
        self.appendToTerminal("Connecting to device name: {} Address: {}".format(selected_device, device_addr))
        self.appendToTerminal("Trying to connect...")
        bt_socket = self.bt.connect_to_device(selected_device)
        if bt_socket is None:
            return

        if self.ui.rb_receive.isChecked:
            self.worker_thread.bt_socket = bt_socket
            self.worker_thread.start()
        else:
            return


    def callback_scan_button(self):
        self.ui.tb_output.append("Scanning for nearby devices...")
        self.ui.btn_scan.setEnabled(False)
        self.test_thread.start()
        #self.ui.btn_scan.setEnabled(False)
        #devices = self.bt.discover_devices()


        #for key, value in devices.items():
        #    self.ui.cb_device_connect.addItem(key + "-" + value)

        #self.ui.btn_scan.setEnabled(True)

    def scan_button_toggle_state(self):
        if self.ui.btn_scan.isEnabled:
            self.ui.btn_scan.setEnabled(False)
        else:
            self.ui.btn_scan.setEnabled(True)

    def appendToTerminal(self, line_to_append):
        self.ui.tb_output.append(line_to_append + "\n")

    def sendToUI(self, PyQt_PyObject):
        print("We are signalled!")
        mItems = dict(PyQt_PyObject)
        self.appendToTerminal("Found {} available devices".format(len(PyQt_PyObject)))
        for key, value in mItems.items():
            self.appendToTerminal(value + " - " + key)
            self.ui.cb_device_connect.addItem(value + "-" + key)
        
        self.ui.btn_scan.setEnabled(True)
            

        

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())

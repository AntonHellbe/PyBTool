from PyQt4 import QtGui
from PyQt4.QtCore import *
from output import Ui_MainWindow
from BTservice import PyBluetooth
from BTReceiver import BTReceiverThread
import sys


class Main(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect_btn_listeners()
        self.bt = PyBluetooth(self)

    def connect_btn_listeners(self):
        self.ui.btn_scan.clicked.connect(self.callback_scan_button)
        self.ui.btn_connect.clicked.connect(self.callback_connect_button)
        self.ui.btn_test_adr.clicked.connect(self.test_bt_address)
    

    def callback_connect_button(self):
        selected_device = str(self.ui.cb_device_connect.currentText())
        selected_device = selected_device.split(" ")
        name = "".join(selected_device[2:])
        print(name)
        if selected_device is None:
            return
        
        self.bt.connect_to_device(selected_device)
    
    def test_bt_address(self):
        addr = self.ui.te_device_adr.currentText()
        addr = "78:44:05:A9:52:3F"
        is_valid_addr = self.bt.check_bt_address(addr)
        if is_valid_addr:
            print("Address valid")
        else:
            print("Not valid")


    def callback_scan_button(self):
        self.ui.btn_scan.setEnabled(False)
        devices = self.bt.discover_devices()

    def scan_button_toggle_state(self):
        if self.ui.btn_scan.isEnabled:
            self.ui.btn_scan.setEnabled(False)
        else:
            self.ui.btn_scan.setEnabled(True)
    
    def update_output(self, string):
        self.ui.tb_output.append(string)

    def devices_discovered(self, dict):
        for key, value in dict.items():
            self.ui.cb_device_connect.addItem(key + " - " + value)
        self.ui.btn_scan.setEnabled(True)
            
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())

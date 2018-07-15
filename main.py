import sys
from PyQt4 import QtGui
from PyQt4.QtCore import *
from output import Ui_MainWindow
from bluetoothservice import PyBluetooth
from BTReceiver import BTReceiverThread

class Main(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect_btn_listeners()
        self.bt = PyBluetooth()
        self.worker_thread = BTReceiverThread()
        self.connect(self.worker_thread, SIGNAL("bt_data_received(QString)"), self.bt_data_received)

    def connect_btn_listeners(self):
        self.ui.btn_scan.clicked.connect(self.callback_scan_button)
        self.ui.btn_connect.clicked.connect(self.callback_connect_button)
    

    def callback_connect_button(self):
        #selected_device = str(self.ui.cb_device_connect.currentText())
        #selected_device = selected_device.split(" ")
        #name = selected_device[0] + " " + selected_device[1]
        #print(name)
        #if selected_device == "":
        #    return
        
        bt_socket = self.bt.connect_to_device("78:44:05:A9:52:3F")
        if bt_socket is not None:
            self.worker_thread.bt_socket = bt_socket
            self.worker_thread.start()
        else:
            

        print("Callback connect button called")




    def callback_scan_button(self):
        self.ui.btn_scan.setEnabled(False)
        devices = self.bt.discover_devices()


        for key, value in devices.items():
            self.ui.cb_device_connect.addItem(key + " - " + value)

        self.ui.btn_scan.setEnabled(True)

    def scan_button_toggle_state(self):
        if self.ui.btn_scan.isEnabled:
            self.ui.btn_scan.setEnabled(False)
        else:
            self.ui.btn_scan.setEnabled(True)
    
    def bt_data_received(self, QString):
        self.ui.tb_output.append(str(QString) + "\n")
            

        

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())

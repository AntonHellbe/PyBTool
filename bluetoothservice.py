import bluetooth
import sys
from time import sleep
from BTReceiver import BTReceiverThread
from PyQt4.QtCore import *
from PyQt4 import QtGui


class PyBluetooth(QObject):

    def __init__(self, ui):
        self.bluetooth = bluetooth
        self.available_devices = {}
        self.bt_socket = None
        self.ui = ui
        #self.connect(self.worker_thread, SIGNAL("sendToTerminal(QString)"), self.sendToTerminal)
    
    def set_pack_timeout(self, timeout):
        self.bluetooth.set_packet_timeout = timeout
    
    def find_device_name(self, addr, timeout):
        return self.bluetooth.lookup_name(addr=addr, timeout=timeout)
    
    def discover_devices(self):
        sleep(1)
        nearby_devices = self.bluetooth.discover_devices(duration=2, flush_cache=True, lookup_names=True)
        self.sendToTerminal("Found {} available devices".format(len(nearby_devices)))
        for addr, name in nearby_devices:
            self.available_devices[name] = addr

        return self.available_devices

    def connect_to_device(self, name):
        device_addr = self.available_devices[name]
        port = 1
        self.bt_socket = self.bluetooth.BluetoothSocket(self.bluetooth.RFCOMM)
        try:
            self.bt_socket.connect((device_addr, port))
            self.sendToTerminal("Accepted connection from {}".format(device_addr))
            return self.bt_socket
        except self.bluetooth.btcommon.BluetoothError as e:
            self.sendToTerminal(str(e))

        return None
    
    def sendToTerminal(self, QString):
        self.ui.appendToTerminal(QString)

    def get_device_addr(self, name):
        return self.available_devices[name]
        

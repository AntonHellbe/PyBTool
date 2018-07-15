import bluetooth
from time import sleep


class PyBluetooth():

    def __init__(self):
        self.bluetooth = bluetooth
        self.available_devices = {}
        self.bt_socket = None
    
    def set_pack_timeout(self, timeout):
        self.bluetooth.set_packet_timeout = timeout
    
    def find_device_name(self, addr, timeout):
        return self.bluetooth.lookup_name(addr=addr, timeout=timeout)
    
    def discover_devices(self):
        nearby_devices = bluetooth.discover_devices(duration=2, flush_cache=True, lookup_names=True)
        print("Found {} available devices".format(len(nearby_devices)))
        for addr, name in nearby_devices:
            self.available_devices[name] = addr

        return self.available_devices

    def connect_to_device(self, device_addr):
        #device_addr = self.available_devices[name]
        name = "JBL"
        print("Connecting to device name: {} Address: {}".format(name, device_addr))
        port = 1 #RFCOMM port?
        #passkey = "1111" #??????
        print("Trying to connect...")
        self.bt_socket = self.bluetooth.BluetoothSocket(self.bluetooth.RFCOMM)
        try:
            self.bt_socket.connect((device_addr, port))
            print("Accepted connection from {}".format(device_addr))
            return self.bt_socket
        except self.bluetooth.btcommon.BluetoothError as e:
            print(e)
            return None
        
        



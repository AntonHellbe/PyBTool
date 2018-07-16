from PyQt4.QtCore import *

class BTReceiverThread(QThread):

    def __init__(self):
        QThread.__init__(self)
        self.bt_socket = None
    
    def __del__(self):
        self.wait()
    
    def run(self):
        while(True):
            try:
                print("Got data")
                data = str(self.bt_socket.recv(1024))
                if len(data) == 0:
                    self.__del__()
                self.emit(SIGNAL("bt_data_received(QString)"), data)
            except IOError as e:
                print(e)
                self.__del__()



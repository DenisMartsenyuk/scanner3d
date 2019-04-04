from threading import Thread
from serial import Serial
from time import sleep
from queue import Queue
from config import Config


class SerialChat(Thread):
    def __init__(self, port, baudrate):
        Thread.__init__(self)
        self.serial = Serial()
        self.received = Queue()
        self.last_bytes = None

    def connect(self):
        self.serial.close()
        while not self.serial.is_open:
            try:
                self.serial.open()
            except:
                pass

    def run(self):
        while True:
            try:
                data = self.serial.read_until(Config.SerialChat.STOP_SIGNAL)
                print('<-', data)
            except:
                self.connect()

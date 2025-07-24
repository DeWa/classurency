import threading
import serial


class BarcodeScanner:
    def __init__(self, on_read=None):
        self.ser = serial.Serial("/dev/ttyACM0", 9600, timeout=1)
        self.thread = threading.Thread(target=self.read_loop, daemon=True)
        self.thread.start()

    def set_callback(self, callback):
        self.on_read = callback

    def read_loop(self):
        while True:
            data = self.ser.readline()
            if self.on_read and data:
                self.on_read(data.decode("utf-8").strip())


barcode_scanner = BarcodeScanner()

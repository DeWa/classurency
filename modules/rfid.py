from mfrc522 import SimpleMFRC522
import threading


class Rfid:
    def __init__(self, on_read=None):
        self.rfid = SimpleMFRC522()
        self.on_read = on_read
        self.thread = threading.Thread(target=self.read_loop, daemon=True)
        self.thread.start()

    def set_callback(self, callback):
        self.on_read = callback

    def read(self):
        id, text = self.rfid.read()
        return id, text

    def write(self, text):
        self.rfid.write(text)

    def read_loop(self):
        while True:
            id, text = self.read()
            if self.on_read:
                self.on_read(id, text)


rfid = Rfid()

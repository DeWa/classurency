from kivy.uix.screenmanager import Screen

class IdleScreen(Screen):
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)

    def on_rfid_read(self, id, text):
        #self.label.text = f"RFID Read: {id}, {text}"
        self.change_to_account_screen()

    def on_barcode_scanner_read(self, barcode):
        pass
        #self.label.text = f"Barcode: {barcode}"

    def on_enter(self):
        pass


    def change_to_account_screen(self):
        self.manager.transition.direction = "up"
        self.manager.transition.duration = 3
        self.manager.current = "account_screen"

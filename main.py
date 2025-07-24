from kivy.app import App
from kivy.config import Config
from kivy.core.window import Window
from kivy.clock import Clock

from views.idlescreen.idlescreen import IdleScreen
from views.accountscreen.accountscreen import AccountScreen
from views.shoppingscreen.shoppingscreen import ShoppingScreen

from modules.rfid import rfid
from modules.barcode_scanner import barcode_scanner

Config.set("graphics", "fullscreen", "auto")
START_SCREEN = "shopping_screen"


class ClassurencyApp(App):
    def on_start(self):
        Window.show_cursor = False
        # Give the window focus so that keyboard input is not
        # bleeding to the terminal
        Window.show()

        self.rfid = rfid
        self.rfid.set_callback(self.on_rfid_read)
        self.barcode_scanner = barcode_scanner
        self.barcode_scanner.set_callback(self.on_barcode_scanner_read)

        self.root.current = START_SCREEN

    def on_rfid_read(self, id, text):
        # Schedule the UI update on the main thread
        Clock.schedule_once(lambda dt: self.handle_rfid_read(id, text))

    def handle_rfid_read(self, id, text):
        current_screen = self.root.current_screen
        if hasattr(current_screen, "on_rfid_read"):
            current_screen.on_rfid_read(id, text)

    def on_barcode_scanner_read(self, barcode):
        Clock.schedule_once(
            lambda dt: self.handle_barcode_scanner_read(barcode))

    def handle_barcode_scanner_read(self, barcode):
        current_screen = self.root.current_screen
        if hasattr(current_screen, "on_barcode_scanner_read"):
            current_screen.on_barcode_scanner_read(barcode)


if __name__ == "__main__":
    ClassurencyApp().run()

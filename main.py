from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivy.clock import Clock
from screens.idlescreen import IdleScreen
from modules.rfid import rfid


class ClassurencyApp(App):
    def build(self):
        Window.show_cursor = False
        self.screen_manager = ScreenManager()
        self.screen_manager.add_widget(IdleScreen())
        self.rfid = rfid
        self.rfid.set_callback(self.on_rfid_read)
        return self.screen_manager

    def on_rfid_read(self, id, text):
        # Schedule the UI update on the main thread
        Clock.schedule_once(lambda dt: self.handle_rfid_read(id, text))

    def handle_rfid_read(self, id, text):
        current_screen = self.screen_manager.current_screen
        if hasattr(current_screen, "on_rfid_read"):
            current_screen.on_rfid_read(id, text)


if __name__ == "__main__":
    ClassurencyApp().run()

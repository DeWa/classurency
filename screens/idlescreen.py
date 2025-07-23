from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class IdleScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation="vertical")
        self.add_widget(self.layout)
        self.label = Label(text="This is idle screen")
        self.layout.add_widget(self.label)

    def on_rfid_read(self, id, text):
        self.label.text = f"RFID Read: {id}, {text}"

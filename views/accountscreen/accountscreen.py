from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

class KeycodeInput(BoxLayout):
    formatted_keycode = StringProperty("")

    def get_formatted_keycode(self):
        return StringProperty("*" * len(self.parent.keycode))

class AccountInfo(BoxLayout):
    pass

class AccountContainer(BoxLayout):
    def __init__(self, *args):
        super(AccountContainer, self).__init__(*args)
        self.widget = None
        self.account_number = None
        self.keycodeInput = KeycodeInput()
        self.accountInfo = AccountInfo()
    
    def change_sub_screen(self, state):
        if self.widget is not None:
            self.remove_widget(self.widget)

        if state == "account_info":
            self.widget = self.accountInfo
        else:
            self.widget = self.keycodeInput
        self.add_widget(self.widget)

    def clear_widget(self):
        if self.widget is not None:
            self.remove_widget(self.widget)
            self.widget = None


class AccountScreen(Screen):
    keycode = ""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.account_container = AccountContainer()
        self.add_widget(self.account_container)
    
    def on_enter(self):
        self.account_container.change_sub_screen("keycode_input")
    
    def on_correction(self):
        self.keycode = self.keycode[:-1]
        self.account_container.keycodeInput.formatted_keycode =  "*" * len(self.keycode)
    
    def on_pressing_cancel(self):
        self.keycode = ""
        self.account_container.clear_widget()
        self.manager.current = "idle_screen"

    def on_pressing_enter(self):
        self.account_container.change_sub_screen("account_info")
    
    def on_key_press(self, key):
        if len(self.keycode) == 4:
            return 
        else:
            self.keycode += key
            self.account_container.keycodeInput.formatted_keycode =  "*" * len(self.keycode)
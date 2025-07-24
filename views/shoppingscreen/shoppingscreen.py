from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from typing import Any, List, NamedTuple
from enum import Enum


class ShoppingState(Enum):
    CART = 1
    ASK_CARD = 2
    ASK_PIN = 3
    PAYMENT_END = 4


class CartItem(NamedTuple):
    name: str
    price: float


class CartItemLayout(BoxLayout):
    name: StringProperty = StringProperty("")
    price: StringProperty = StringProperty("")


class ConfirmationExitPopup(Popup):
    pass


class ConfirmationBuyPopup(Popup):
    pass


class CartState(BoxLayout):
    pass


class AskCardState(BoxLayout):
    pass


class AskPinState(BoxLayout):
    formatted_keycode = StringProperty("")
    keycode = ""


class PaymentEndState(BoxLayout):
    pass


class ShoppingContainer(BoxLayout):
    def __init__(self, *args):
        super(ShoppingContainer, self).__init__(*args)
        self.widget = None
        self.cart_state = CartState()
        self.ask_card_state = AskCardState()
        self.ask_pin_state = AskPinState()
        self.payment_end_state = PaymentEndState()

    def change_sub_screen(self, state: ShoppingState):
        if self.widget is not None:
            self.remove_widget(self.widget)

        if state == ShoppingState.CART:
            self.widget = self.cart_state
            self.parent.state = ShoppingState.CART
        elif state == ShoppingState.ASK_CARD:
            self.widget = self.ask_card_state
            self.parent.state = ShoppingState.ASK_CARD
        elif state == ShoppingState.ASK_PIN:
            self.widget = self.ask_pin_state
            self.parent.state = ShoppingState.ASK_PIN
        elif state == ShoppingState.PAYMENT_END:
            self.widget = self.payment_end_state
            self.parent.state = ShoppingState.PAYMENT_END
        self.add_widget(self.widget)


class ShoppingScreen(Screen):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.state = ShoppingState.CART
        self.cart: List[CartItem] = [
            CartItem(name="Item 1", price=10),  # Remove this
        ]
        self.confirmation_exit_popup: ConfirmationExitPopup = ConfirmationExitPopup()
        self.confirmation_buy_popup: ConfirmationBuyPopup = ConfirmationBuyPopup()
        self.shopping_container = ShoppingContainer()
        self.add_widget(self.shopping_container)

    def on_enter(self) -> None:
        self.shopping_container.cart_state.ids.cart_container.bind(
            minimum_height=self.shopping_container.cart_state.ids.cart_container.setter('height'))
        self.shopping_container.change_sub_screen(ShoppingState.CART)

    def on_pressing_cancel(self) -> None:
        self.confirmation_exit_popup.open()

    def on_pressing_buy(self) -> None:
        self.confirmation_buy_popup.open()

    def on_barcode_scanner_read(self, barcode: str) -> None:
        self.add_item_to_cart(barcode)

    def on_rfid_read(self, id, text) -> None:
        if self.state == ShoppingState.ASK_CARD:
            self.shopping_container.change_sub_screen(ShoppingState.ASK_PIN)

    def exit_confirmed(self) -> None:
        self.shopping_container.cart_state.ids.cart_container.clear_widgets()
        self.cart = []
        self.confirmation_exit_popup.dismiss()
        self.manager.current = "idle_screen"

    def buy_confirmed(self) -> None:
        self.confirmation_buy_popup.dismiss()
        self.shopping_container.change_sub_screen(ShoppingState.ASK_CARD)

    def add_item_to_cart(self, barcode: str) -> None:
        item: CartItem = CartItem(name=str(barcode), price=10)
        self.cart.append(item)
        new_cart_item_layout: CartItemLayout = CartItemLayout(
            name=item.name, price=f"{item.price}€")
        self.shopping_container.cart_state.ids.cart_container.add_widget(
            new_cart_item_layout)
        self.shopping_container.cart_state.ids.cart_scrollview.scroll_to(
            new_cart_item_layout, None, True)

    def on_key_press(self, key: str) -> None:
        print(key)

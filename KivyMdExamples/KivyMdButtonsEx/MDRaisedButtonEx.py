from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRaisedButton
class MyApp(MDApp):
    def build(self):
        screen = Screen()
        screen.add_widget(MDRaisedButton(text="submit",pos_hint={"center_x": 0.5, "center_y": 0.5}))
        return screen


if __name__ == '__main__':
    MyApp().run()

from kivy.uix.screenmanager import Screen

from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton


class MainApp(MDApp):
    def build(self):
        # self.theme_cls.primary_palette = "Red"  # "Purple", "Red"
        self.theme_cls.accent_palette = 'Blue'

        screen = Screen()
        screen.add_widget(
            MDRectangleFlatButton(
                text="Hello, World",
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )

        )
        return screen


MainApp().run()

# Available options are: ‘Red’, ‘Pink’, ‘Purple’, ‘DeepPurple’, ‘Indigo’,
# ‘Blue’, ‘LightBlue’, ‘Cyan’, ‘Teal’, ‘Green’, ‘LightGreen’, ‘Lime’, 
# ‘Yellow’, ‘Amber’, ‘Orange’, ‘DeepOrange’, ‘Brown’, ‘Gray’, ‘BlueGray’.
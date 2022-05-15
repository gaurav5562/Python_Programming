from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.rows = 3
        # self.cols=6
        self.add_widget(Label(text='First Name'))
        self.firstname = TextInput(multiline=False)
        self.add_widget(self.firstname)
        self.add_widget(Label(text='Last Name'))
        self.lastname = TextInput(multiline=False)
        self.add_widget(self.lastname)
        self.add_widget(Label(text='Password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)

class MyApp(App):

    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()
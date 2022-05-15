import kivy  
from kivy.app import App  
from kivy.uix.boxlayout import BoxLayout  
from kivy.lang import Builder 
# Builder.load_file('E:\\Program Self Exercise\\KivyEx\\Signin.kv') 
Builder.load_string(kv_string)
class SigninWindow(BoxLayout):  
  
    def __init__(self, **kwargs):  
        super().__init__(**kwargs)  
  
    def validate_user(self):  
        user = self.ids.username_field  
        pwd = self.ids.pwd_field  
        info = self.ids.info  
          
        uname = user.text  
        passwd = pwd.text  
  
        if uname == '' or passwd == '':  
            info.text = '[color=#FF0000]username and password are required[/color]'  
        else:  
            if uname == 'admin' and passwd == 'admin':  
                info.text = '[color=#00FF00]Logged In successfully!!![/color]'  
            else:  
                info.text = '[color=#FF0000]Invalid Username and Password[/color]'  
  
  
  
class SigninApp(App):  
    def build(self):  
        return SigninWindow()  
  
  
root = SigninApp()  
root.run()  
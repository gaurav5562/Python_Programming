import kivy  
from kivy.app import App  
from kivy.uix.button import Button  
from kivy.uix.label import Label  
from kivy.uix.popup import Popup  
from kivy.uix.gridlayout import GridLayout  
  
class Popup_Demo(App):  
  
    def build(self):  
  
        layout = GridLayout(cols = 1, padding = 10)  
          
        self.button = Button(text="Click Here to view Popup",  
        size_hint = (0.8, 0.2),  
        pos_hint = {"x":0.1, "y":0.1})  
          
        layout.add_widget(self.button)  
          
        self.button.bind(on_press = self.onButtonPress)   
          
        return layout  
  
    def onButtonPress(self, button):  
  
        layout  = GridLayout(cols = 1, padding = 10)  
          
        popupLabel  = Label(text  = "Welcome User")  
          
        closeButton = Button(text = "Close the pop-up window")  
          
        layout.add_widget(popupLabel)  
          
        layout.add_widget(closeButton) 
          
        popup = Popup(title = 'Demo Popup',  
          
          content = layout)
  
   
          
        popup.open() 
          
        closeButton.bind(on_press = popup.dismiss) 
  
root = Popup_Demo()  
root.run()  
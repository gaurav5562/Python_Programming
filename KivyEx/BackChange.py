# import kivy    
from kivy.app import App   
from kivy.uix.label import Label  #import Label Module  
from kivy.core.window import Window
Window.clearcolor=(1,0,0,1)    
   
class Label_Demo(App):   
    def build(self):   
         
        label1 = Label(text ="Gaurav", font_size = 120,color=(0,0,0,0.1)) #Disply label on the screen  
        return label1   
    
root=Label_Demo()  
root.run()
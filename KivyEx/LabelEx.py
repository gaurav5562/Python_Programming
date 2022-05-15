import kivy    
from kivy.app import App   
from kivy.uix.label import Label  #import Label Module  
    
   
class Label_Demo(App):   
    def build(self):   
         
        label1 = Label(text ="javaTpoint", font_size = 120) #Disply label on the screen  
        return label1   
    
root=Label_Demo()  
root.run()
import kivy  # import kivy module  
from kivy.app import App # import Kivy App module to create a Kivy interface  
from kivy.uix.image import Image # import image Module  
    
# kivy.require('1.11.1')  # version required to run Kivy Application    
    
   
class MyKivyApp(App): # Create a class MyKivyApp  
        
      
    def build(self):   
            
       return Image(source ="E:\\Program Self Exercise\\KivyEx\\img.jpg") #return an Image as a root widget         
    
    
   
MyKivyApp().run()
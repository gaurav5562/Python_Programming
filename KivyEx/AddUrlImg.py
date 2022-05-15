import kivy  # import kivy module  
from kivy.app import App # import Kivy App module to create a Kivy interface  
from kivy.uix.image import AsyncImage # import image Module  
    
kivy.require('1.11.1')  # version required to run Kivy Application    
      
   
class MyKivyApp(App): # Create a class MyKivyApp  
        
      
    def build(self):   
            
       return AsyncImage(source ="https://media.gettyimages.com/photos/stack-of-books-picture-id157482029?s=612x612") #return an Image as a root widget         
    
      #Copy the image link address.  
   
MyKivyApp().run() 
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import Screen
data_helper="""
Screen:
	GridLayout:
		cols:1
		spacing:20
		padding:80
		MDRectangleFlatButton:
			text:'Submit1'
			on_press:app.data_call()
		MDRectangleFlatButton:
			text:'Submit2'	
		MDRectangleFlatButton:
			text:'Submit3'	
		
"""
class Demo1app(MDApp):
	def build(self):
		screen=Builder.load_string(data_helper)
		return screen
	def data_call(self):
		print("self pressed")	
Demo1app().run()		
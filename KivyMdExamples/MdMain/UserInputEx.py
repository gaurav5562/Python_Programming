from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField,MDTextFieldRect,MDTextFieldRound

class ButtonEx(MDApp):
	def build(self):
		screen=Screen()
		first_name=MDTextField(text='enter',pos_hint={'center_x':0.4,'center_y':0.5},size_hint_x=None,width=100)
		screen.add_widget(first_name)
		last_name=MDTextFieldRect(text='enter',pos_hint={'center_x':0.7,'center_y':0.5},
			size_hint=(0.2,0.05))
		screen.add_widget(last_name)
		return screen

ButtonEx().run()	






from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatIconButton,MDIconButton,MDFloatingActionButton,MDFD

class ButtonEx(MDApp):
	def build(self):
		screen=Screen()
		btn=MDRectangleFlatIconButton(text='press',pos_hint={'center_x':0.5,'center_y':0.5},icon='download')
		screen.add_widget(btn)
		btn1=MDIconButton(icon='share')
		screen.add_widget(btn1)
		btn2=MDFloatingActionButton(pos_hint={'center_x':0.5,'center_y':0.5},icon='download')
		screen.add_widget(btn2)
		return screen

ButtonEx().run()		
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField,MDIcon
from kivy.lang import Builder
name_hint=''' 
MDTextField:
	hint_text:'enter name'
	helper_text:'Capital'
	helper_text_mode:'on_focus'# or use 'persistant'
	pos_hint:{'center_x':0.5,'center_y':0.5}
	size_hint_x:None
	width:200
	icon_right:'share'
	icon_right_color:app.theme_cls.primary_color

'''
class ButtonEx(MDApp):
	def build(self):
		self.theme_cls.primary_palette='Red'
		screen=Screen()
		name=Builder.load_string(name_hint)
		screen.add_widget(name)
		return screen

ButtonEx().run()	




	

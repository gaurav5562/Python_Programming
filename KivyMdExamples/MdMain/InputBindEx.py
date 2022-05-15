from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivy.lang import Builder
from importhint import username_hint
class ButtonEx(MDApp):
	def build(self):
		self.theme_cls.primary_palette='Red'
		screen=Screen()
		self.username=Builder.load_string(username_hint)
		screen.add_widget(self.username)
		btn=MDRectangleFlatButton(text='submit',pos_hint={'center_x':0.5,'center_y':0.7},
			on_release=self.show_data)
		screen.add_widget(btn)
		return screen
	def show_data(self,obj):
		print(self.username.text)
ButtonEx().run()	




	

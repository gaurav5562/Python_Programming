from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatIconButton

class ButtonEx(MDApp):
	def build(self):
		self.theme_cls.primary_palette='Red'
		self.theme_cls.primary_hue='200'
		#primary_hue={50,100,200,300,400,500,600,700,800,900,A100,A200,A400,A700} 
		screen=Screen()
		btn=MDRectangleFlatIconButton(text='press',pos_hint={'center_x':0.5,'center_y':0.5},icon='download')
		screen.add_widget(btn)
		return screen

ButtonEx().run()		
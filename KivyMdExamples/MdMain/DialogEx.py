from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatButton,MDFlatButton
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from importhint import username_hint
class DiaEx(MDApp):
	def build(self):
		self.theme_cls.primary_palette='Red'
		screen=Screen()
		self.username=Builder.load_string(username_hint)
		screen.add_widget(self.username)
		btn=MDRectangleFlatButton(text='submit',pos_hint={'center_x':0.5,'center_y':0.3},
			on_release=self.show_data)
		screen.add_widget(btn)
		return screen
	def show_data(self,obj):
		if self.username.text is '':
			data_string="please enter something"
		else:
			data_string=self.username.text+" " + "not good"	
		close_btn=MDFlatButton(text='close',on_release=self.close_dia)
		more_btn=MDFlatButton(text='more',on_release=self.more_dia)
		self.dialog=MDDialog( title="check name",text=data_string,
			size_hint=(0.5,1),buttons=[close_btn,more_btn])	
		self.dialog.open()
	def close_dia(self,obj):
		self.dialog.dismiss()
	def more_dia(self,obj):
		pass		

DiaEx().run()
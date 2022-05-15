from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
Builder.load_file('E:\\Program Self Exercise\\KivyEx\\Marvel.kv')
class Marvel(BoxLayout):
	def smash(self):
		self.ids.hulk.text = "Click Pressed"
		self.ids["Gaurav"].text = "Yes"
class MynewApp(App):
	def build(self):
		return Marvel()

MynewApp().run()
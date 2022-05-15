from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.uix.screen import Screen
from kivymd.uix.list import MDList,ThreeLineListItem,ThreeLineIconListItem
from kivymd.uix.list import IconLeftWidget,ImageLeftWidget
from kivy.uix.scrollview import ScrollView
from listdata import item_list

class OnelineEx(MDApp):
	def build(self):
		screen=Builder.load_string(item_list)
		return screen
	def on_start(self):
		for i in range(1,21):
			items=ThreeLineIconListItem(text='Item'+str(i),secondary_text='hello i am number'+str(i),
				tertiary_text=f'this is {i} number')
			self.root.item_list.container.add_widget(items)
			
OnelineEx().run()	
# ******************************One line list***********************************

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import MDList,OneLineListItem
from kivy.uix.scrollview import ScrollView
class OnelineEx(MDApp):
	def build(self):
		screen=Screen()
		my_list=MDList()
		scroll=ScrollView()
		scroll.add_widget(my_list)
		for i in range(20):
			items=OneLineListItem(text='Item'+str(i))
			my_list.add_widget(items)
		screen.add_widget(scroll)
		return screen
OnelineEx().run()	

# ******************************Two line list***********************************


# from kivymd.app import MDApp
# from kivymd.uix.screen import Screen
# from kivymd.uix.list import MDList,TwoLineListItem
# from kivy.uix.scrollview import ScrollView
# class OnelineEx(MDApp):
# 	def build(self):
# 		screen=Screen()
# 		my_list=MDList()
# 		scroll=ScrollView()
# 		scroll.add_widget(my_list)
# 		for i in range(1,21):
# 			items=TwoLineListItem(text='Item'+str(i),secondary_text='hello i am number'+str(i))
# 			my_list.add_widget(items)
# 		screen.add_widget(scroll)
# 		return screen
# OnelineEx().run()	

# ******************************Three line list***********************************


# from kivymd.app import MDApp
# from kivymd.uix.screen import Screen
# from kivymd.uix.list import MDList,ThreeLineListItem
# from kivy.uix.scrollview import ScrollView
# class OnelineEx(MDApp):
# 	def build(self):
# 		screen=Screen()
# 		my_list=MDList()
# 		scroll=ScrollView()
# 		scroll.add_widget(my_list)
# 		for i in range(1,21):
# 			items=ThreeLineListItem(text='Item'+str(i),secondary_text='hello i am number'+str(i),
# 				tertiary_text=f'this is {i} number')
# 			my_list.add_widget(items)
# 		screen.add_widget(scroll)
# 		return screen
# OnelineEx().run()	
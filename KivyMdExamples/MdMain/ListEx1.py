#  ******************************One line Icon list***********************************
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import MDList,OneLineListItem,OneLineIconListItem
from kivymd.uix.list import IconLeftWidget
from kivy.uix.scrollview import ScrollView
class OnelineEx(MDApp):
	def build(self):
		screen=Screen()
		my_list=MDList()
		scroll=ScrollView()
		scroll.add_widget(my_list)
		for i in range(1,21):
			icon_set=IconLeftWidget(icon='download')
			items=OneLineIconListItem(text='Item'+str(i))
			items.add_widget(icon_set)
			my_list.add_widget(items)
		screen.add_widget(scroll)
		return screen
OnelineEx().run()	


#  ******************************Two line Icon list***********************************
# from kivymd.app import MDApp
# from kivymd.uix.screen import Screen
# from kivymd.uix.list import MDList,TwoLineListItem,TwoLineIconListItem
# from kivymd.uix.list import IconLeftWidget
# from kivy.uix.scrollview import ScrollView
# class OnelineEx(MDApp):
# 	def build(self):
# 		screen=Screen()
# 		my_list=MDList()
# 		scroll=ScrollView()
# 		scroll.add_widget(my_list)
# 		for i in range(1,21):
# 			icon_set=IconLeftWidget(icon='download')
# 			items=TwoLineIconListItem(text='Item'+str(i),secondary_text='hello i am number'+str(i))
# 			items.add_widget(icon_set)
# 			my_list.add_widget(items)
# 		screen.add_widget(scroll)
# 		return screen
# OnelineEx().run()



#  ******************************Three line Icon list***********************************
# from kivymd.app import MDApp
# from kivymd.uix.screen import Screen
# from kivymd.uix.list import MDList,ThreeLineListItem,ThreeLineIconListItem
# from kivymd.uix.list import IconLeftWidget,ImageLeftWidget
# from kivy.uix.scrollview import ScrollView
# class OnelineEx(MDApp):
# 	def build(self):
# 		screen=Screen()
# 		my_list=MDList()
# 		scroll=ScrollView()
# 		scroll.add_widget(my_list)
# 		for i in range(1,21):
# 			image_set=ImageLeftWidget(source='dg.jpg')
# 			items=ThreeLineIconListItem(text='Item'+str(i),secondary_text='hello i am number'+str(i),
# 				tertiary_text=f'this is {i} number')
# 			items.add_widget(image_set)
# 			my_list.add_widget(items)
# 		screen.add_widget(scroll)
# 		return screen
# OnelineEx().run()	
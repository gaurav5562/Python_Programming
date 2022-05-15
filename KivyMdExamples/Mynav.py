from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
Window.size=(300,500)
screen_helper="""
Screen:
	NavigationLayout:
		ScreenManager:
			Screen:
				BoxLayout:
					orientation:"vertical"
					MDToolbar:
						title:"DemoApp"
						left_action_items:[["menu",lambda x :nav_drawer.set_state()]]#toggle_nav_drawer in place of set_state
						elevation:10
					MDList:
						OneLineListItem:
							text:'Item'
							on_press:app.print_function()
					ScrollView:		
		MDNavigationDrawer:
			id:nav_drawer	
			BoxLayout:
				orientation:"vertical"
				spacing:'8dp'
				padding:'8dp'
				Image:
					source:"E:\\Program Self Exercise\\KivyMdExamples\\MdMain\\dg.jpg"
				MDLabel:
					text:"Hello"
					font_style:"Subtitle1"
					size_hint_y:None
					height:self.texture_size[1]
				MDLabel:
					text:"email"
					font_style:"Caption"	
					size_hint_y:None
					height:self.texture_size[1]
				ScrollView:
					MDList:
						OneLineIconListItem:
							text:"hello1"
							IconLeftWidget:
								icon:'android'				
						OneLineIconListItem:
							text:"hello2"
							IconLeftWidget:
								icon:'android'		


"""

class Demo(MDApp):
	def build(self):
		self.theme_cls.primary_palette="Red"
		screen=Builder.load_string(screen_helper)
		return screen
	def navigation_draw(self):
		print("navigation_draw()")
	def share_app(self):
		print("share_app()")
	def print_function(self):
		print("pressed")			
Demo().run()		
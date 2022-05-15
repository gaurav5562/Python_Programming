from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
Window.size=(300,500)
screen_helper="""
Screen:
	BoxLayout:
		orientation:"vertical"
		MDToolbar:
			title:"DemoApp"
			left_action_items:[["menu",lambda x :app.navigation_draw()]]
			right_action_items:[["share-variant",lambda x :app.share_app()]]
			elevation:11
		MDLabel:
			text:"Hello"
			halign:'center'
		
		MDBottomAppBar:
			MDToolbar:
				left_action_items:[["menu",lambda x :app.navigation_draw()]]
				right_action_items:[["share-variant",lambda x :app.share_app()]]
				mode:"end"	# or "free-end"	
				type:"bottom"
				on_action_button:app.navigation_draw()
				icon:'more'
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
Demo().run()		
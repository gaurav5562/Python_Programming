from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen,ScreenManager
screen_helper="""
ScreenManager :
	WelcomeScreen:
    MenuScreen:
<WelcomeScreen>:
	name:'welcome'
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
								on_press: root.manager.current='menu'
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
							OneLineListItem:
								text:"hello1"				
							OneLineListItem:
								text:"hello2"
								
<MenuScreen>:
	name:'menu'
	MDLabel:
		text:'Hello'
		pos_hint:{'center_x':0.95,'center_y':0.7}
	MDRectangleFlatButton:
		text:'Menu'
		pos_hint:{'center_x':0.5,'center_y':0.5}
		on_press: root.manager.current='profile'

"""
class MenuScreen(Screen):
	pass

class WelcomeScreen(Screen):
	pass	
se=ScreenManager()
se.add_widget(MenuScreen(name='welcome'))
se.add_widget(MenuScreen(name='menu'))

class DemoApp(MDApp):
	def build(self):
		screen=Builder.load_string(screen_helper)
		return screen
DemoApp().run()		

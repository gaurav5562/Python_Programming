from kivymd.app import MDApp
from kivymd.uix.label import MDLabel,MDIcon
class LabelEx(MDApp):
	def build(self):
		# label=MDLabel(text="Hello World",halign='center',theme_text_color='Error')
		# theme_text_color=Primary,Secondary,Hint,Error
		label=MDLabel(text="Hello World",halign='center',theme_text_color='Custom',
			text_color=(0,1,0,1),font_style='H1')
		icon_label=MDIcon(icon='share')
		return icon_label
if __name__ == '__main__':
			LabelEx().run()		

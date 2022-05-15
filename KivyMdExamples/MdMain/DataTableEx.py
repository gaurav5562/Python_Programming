from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import Screen 
from kivy.metrics import dp
class dat_table(MDApp):
	def build(self):
		screen=Screen()
		self.table=MDDataTable(#check=True,
								rows_num=50,
								# size_hint=(0.5, 0.5),
								# use_pagination=True,
								column_data=[("No.",dp(11)),
										("State",dp(28)),
										("Capital",dp(30))
									  ],
						  row_data=[("1","Andhra Pradesh","Hyderabad"),
						  			("2","Arunachal Pradesh","Itanagar"),
						  			("3","Assam","Dispur"),
						  			("4","Bihar","Patna"),
						  			("5","Chhattisgarh","Raipur"),
						  			("6","Goa","Panaji"),
						  			("7","Gujrat","Gandhinagar"),
						  			("8","Harayana","Chandigarh"),
						  			("9","Himanchal Pradesh","Shimla"),
						  			("10","Jharkhand","Ranchi"),
						  			("11","Karnataka","Bengaluru"),
						  			("12","Kerala","Thiruvananthapuram"),
						  			("13","Madhya Pradesh","Bhopal"),
						  			("14","Maharashtra","Mumbai"),
						  			("15","Manipur","Imphal"),
						  			("16","Meghalaya","Shillong"),
						  			("17","Mizoram","Aizawl"),
						  			("18","Nagaland","Kohima"),
						  			("19","Odisha","Bhubaneswar"),
						  			("20","Punjab","Chandigarh"),
						  			("21","Rajasthan","Jaipur"),
						  			("22","Sikkam","Gangtok"),
						  			("23","Tamil Nadu","Chennai"),						  			
						  			("24","Telangana","Hyderabad"),
						  			("25","Tripura","Agartala"),
						  			("26","Uttar Pradesh","Lucknow"),
						  			("27","Uttarakhand","Dehradun , Gairsain(Summer)"),						  		
						  			("28","West Bengal","Kolkata"),
						  			("----------","-----------","-------------"),
						  			("1","Andaman abd Nicobar","Port Blair"),
						  			("2","Chandigarh","Chandigarh"),
						  			("3","Dadra and Nagar Haveli","Daman"),
						  			("4","Delhi","New Delhi"),
						  			("5","Lakshadweep","Kavaratti"),
						  			("6","Jammu and Kashmir","Srinagar(Summer) , Jammu(Winter)"),
						  			("7","Ladakh","Leh"),
						  			("8","Puducherry","Puducherry"),
						  			
								   ]		  
						 )
		self.table.bind(on_check_press=self.check_press)
		self.table.bind(on_row_press=self.row_press)
		screen.add_widget(self.table)
		return screen
	def check_press(self,instance_table,current_row):
		print(instance_table,current_row)
	def row_press(self,instance_table,instance_row):
		print(instance_table,instance_row)		
dat_table().run()
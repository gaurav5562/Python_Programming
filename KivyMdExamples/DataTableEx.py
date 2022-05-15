from kivy.metrics import dp

from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable

class Example1(MDApp):
    def build(self):
        self.data_tables = MDDataTable(
            size_hint=(0.5, 0.5),
            use_pagination=True,
            # check=True,
            column_data=[
                ("Column 1", dp(50)),
                ("Column 2", dp(50)),
            ],
            row_data=[
                (f"{i + 1}", "2.23")
                for i in range(50)
            ],
        )
        self.data_tables.bind(on_row_press=self.on_row_press)
        self.data_tables.bind(on_check_press=self.on_check_press)

    def on_start(self):
        self.data_tables.open()

    def on_row_press(self, instance_table, instance_row):
        '''Called when a table row is clicked.'''

        print(instance_table, instance_row)

    def on_check_press(self, instance_table, current_row):
        '''Called when the check box in the table row is checked.'''

        print(instance_table, current_row)


Example1().run()
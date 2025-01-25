from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout as PopupBox
from kivy.uix.button import Button
import csv
from kivy.core.clipboard import Clipboard

import visualizer.calendar

from .transactionlist import TransactionList
from .graphs import Graphs

import visualizer

class WidgetPopup(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Widgets"
        self.size_hint = (0.5, 0.5)
        self.content = self.create_widget_content()

    def create_widget_content(self):
        content = PopupBox(orientation='vertical')

        content.add_widget(Button(text="List", font_size=32, height=80, 
                                  on_press=self.show_widget1))
        
        content.add_widget(Button(text="Graphs", font_size=32, height=80,
                                  on_press=self.show_widget2))

        content.add_widget(Button(text="Copy CSV file", font_size=32, height=80,
                                  on_press=self.show_widget3))
        
        return content
    
    def show_widget1(self, instance):
        popup = TransactionList(file_path="data_csv/data.csv")
        popup.open()

    def show_widget2(self, instance):
        visualizer.total_gen()
        visualizer.calendar_gen()
        
        popup = Graphs(file_path="data_csv/data.csv")
        popup.open()

    def show_widget3(self, instance):
        source_path = "data_csv/data.csv"  # 원본 CSV 파일 경로

        try:
            # CSV 파일 읽기
            with open(source_path, mode='r', encoding='utf-8') as file:
                reader = csv.reader(file)
                csv_content = "\n".join([",".join(row) for row in reader])
            
            # 클립보드에 복사
            Clipboard.copy(csv_content)
            self.show_success_popup()
        except Exception as e:
            # 에러 팝업 표시
            self.show_error_popup(str(e))

    def show_success_popup(self):
        success_popup = Popup(
            title="Copied!",
            content=PopupBox(
                orientation="vertical",
                children=[
                    Button(
                        text="CSV content copied to clipboard!",
                        font_size=16,
                        size_hint_y=None,
                        height=100,
                        on_press=lambda x: success_popup.dismiss()
                    )
                ]
            ),
            size_hint=(0.8, 0.4)
        )
        success_popup.open()

    def show_error_popup(self, error_message):
        error_popup = Popup(
            title="Error",
            content=PopupBox(
                orientation="vertical",
                children=[
                    Button(
                        text=f"Error:\n{error_message}",
                        font_size=16,
                        size_hint_y=None,
                        height=100,
                        on_press=lambda x: error_popup.dismiss()
                    )
                ]
            ),
            size_hint=(0.8, 0.4)
        )
        error_popup.open()
"""
Seth Gersbach
prac 08
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class dynamic_label(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.info = ["seth", "gersbach", "20"]

    def build(self):
        self.title = "dynamic labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        return self.root

    def create_widgets(self):
        """Create buttons from dictionary entries and add them to the GUI."""
        for name in self.info:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


dynamic_label().run()

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = float(1.60934)


class ConvertMilesKm(App):
    message = StringProperty()

    def build(self):
        self.title = "Convert Miles Km"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def convert_values(self):
        value = self.validate_input()
        result = value * MILES_TO_KM
        self.root.ids.display.text = str(result)

    def validate_input(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0

    def increment_change(self, change):
        value = self.validate_input() + change
        self.root.ids.input_miles.text = str(value)
        self.convert_values()




ConvertMilesKm().run()

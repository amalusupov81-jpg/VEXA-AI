from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

Window.clearcolor = (0.04, 0.02, 0.08, 1)

class VexaAI(App):
    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=15,
            spacing=10
        )

        title = Label(
            text="[b]VEXA AI[/b]",
            markup=True,
            font_size=32,
            color=(0.7, 0.3, 1, 1),
            size_hint_y=0.2
        )

        self.chat = Label(
            text="Привет! Я VEXA AI 💜",
            color=(1, 1, 1, 1)
        )

        self.input = TextInput(
            hint_text="Напиши сообщение...",
            size_hint_y=0.15,
            multiline=False
        )

        button = Button(
            text="ОТПРАВИТЬ",
            background_color=(0.5, 0.1, 0.8, 1),
            size_hint_y=0.15
        )

        button.bind(on_press=self.send_message)

        layout.add_widget(title)
        layout.add_widget(self.chat)
        layout.add_widget(self.input
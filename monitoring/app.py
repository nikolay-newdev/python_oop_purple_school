from textual.app import App

from monitoring.screens.mainscreen import MainScreen

class MonitoringApp(App):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_mount(self):
        main_screen = MainScreen()
        self.push_screen(main_screen)

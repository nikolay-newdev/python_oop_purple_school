from textual.screen import Screen
from textual.widgets import Header, Footer, Input, Button, DataTable, Label
from textual.containers import Vertical, Horizontal

class MainScreen(Screen):
    CSS = """
    #box {padding: 0 10}
    #url_input {width: 8fr}
    #time_interval {width: 2fr}
    #add_button {width: 2fr;  background: green; color: white}
    #connections_table {height: 50h}
    #status_bar {margin-bottom: 1; color: green}


"""

    BINDINGS = [
        ('q', 'quit', 'Выход')
    ]

    def compose(self):
        yield Header()
        with Vertical(id='box'):

            with Horizontal(id='toolbar'):
                yield Input(placeholder='https://example.com', id='url_input')
                yield Input(placeholder='Interval', id='time_interval')
                yield Button('Add', id="add_button")

            yield Label("Статус: Готов к работе", id="status_bar")
            yield DataTable(id='connections_table')

        yield Footer()

    def on_mount(self):
        self.title = "MonitorApp"
        table = self.query_one("#connections_table")
        table.add_columns("URL", "Interval(s)", "Status", "HTTP", "Last Checked")
        table.add_row("some site", "2 min", "OK", "200", "just now")

    def action_quit(self):
        self.app.exit()
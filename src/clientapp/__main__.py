import toga
from toga.style import Pack
from toga.style.expression import COLUMN


class ClientApp(toga.App):

    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=20))

        welcome_label = toga.Label(
            "App Working Successfully! 🎉",
            style=Pack(padding=(0, 0, 15, 0)),
        )

        main_box.add(welcome_label)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return ClientApp("Client App", "com.example.clientapp")


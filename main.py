import toga
from toga.style import Pack
from toga.style.expression import COLUMN, ROW


def build(app):
    box = toga.Box(style=Pack(direction=COLUMN, padding=20))
    label = toga.Label(
        'Hello Harsh! App Successfully Running!',
        style=Pack(padding=(0, 0, 10, 0))
    )
    box.add(label)
    return box


def main():
    return toga.App('Harsh App', 'org.example.harshc', startup=build)


if __name__ == '__main__':
    main()


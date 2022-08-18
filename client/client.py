import sys

from PyQt5 import QtWidgets as widgets

import tcp_client


class Window(widgets.QWidget):
    def __init__(self):
        super().__init__()

        self.resize(1920, 1080)

        self.setWindowTitle("Send It!")

        # Create a QHBoxLayout instance
        main_layout = widgets.QHBoxLayout()

        contact_list = widgets.QListWidget()
        contact_list.resize(100, -1)
        main_layout.addWidget(contact_list)
        message_layout = widgets.QVBoxLayout()
        main_layout.addLayout(message_layout)

        main_layout.setStretch(0, 1)
        main_layout.setStretch(1, 7)

        self.message_history = widgets.QTextEdit()
        self.message_history.setReadOnly(True)
        message_layout.addWidget(self.message_history)

        typing_layout = widgets.QHBoxLayout()

        self.current_message_text = widgets.QTextEdit()
        typing_layout.addWidget(self.current_message_text)
        send_button = widgets.QPushButton("Send")
        typing_layout.addWidget(send_button)

        send_button.clicked.connect(self.send_button_cb)

        typing_layout.setStretch(0, 7)
        typing_layout.setStretch(1, 1)

        message_layout.addLayout(typing_layout)

        message_layout.setStretch(0, 3)
        message_layout.setStretch(1, 1)

        self.setLayout(main_layout)

    def send_button_cb(self):
        print('Clicked send!')
        message = self.current_message_text.toPlainText()
        print(message)
        self.message_history.append(f'Me: {message}')
        self.current_message_text.setPlainText('')


def main():
    app = widgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

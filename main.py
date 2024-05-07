import sys
from backend import Chatbot

from PyQt6.QtWidgets import QMainWindow, QTextEdit, QLineEdit, QPushButton, QApplication


class ChatBotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(700, 500)

        #Chat Area
        self.chatArea = QTextEdit(self)
        self.chatArea.setGeometry(10, 10, 480, 320)
        self.chatArea.setReadOnly(True)

        #Input Field
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 480, 40)

        #Button
        self.button = QPushButton("Send", self)
        self.button.setGeometry(500, 340, 100, 40)
        self.button.clicked.connect(self.send_message)

        self.show()
        self.chatbot = Chatbot()

    def send_message(self):
        user_input = self.input_field.text().strip()
        self.chatArea.append(f'Me: {user_input}\n')
        self.input_field.clear()

        response = self.chatbot.get_response(user_input)
        self.chatArea.append(f"Bot: {response}\n")


app = QApplication(sys.argv)
main_window = ChatBotWindow()
sys.exit(app.exec())

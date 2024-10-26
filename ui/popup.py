from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QPushButton
import sys

class CustomPopup(QDialog):
    def __init__(self, text):
        super().__init__()
        self.initUI(text)

    def initUI(self, text):
        self.setWindowTitle("")
        layout = QVBoxLayout()

        label = QLabel(text)
        layout.addWidget(label)

        button = QPushButton("Close")
        button.clicked.connect(self.close)
        layout.addWidget(button)

        self.setLayout(layout)


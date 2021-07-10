import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QPushButton


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My window")
        self.setGeometry(0, 0, 480, 320)

        self.label_1 = QLabel("Button pushed:", self)
        self.label_1.resize(150, 32)
        self.label_1.move(50, 50)

        self.label_2 = QLabel("0 times.", self)
        self.label_2.resize(150, 32)
        self.label_2.move(230, 50)

        self.button = QPushButton("Push me", self)
        self.button.resize(100, 32)
        self.button.move(150, 130)

        # self.button.clicked is considered a method by Pycharm instead a property.
        # Therefore, calling a connect method is wrongly highlighted as an error.
        self.button.clicked.connect(self.update_counter)

        self.counter = 0

    def update_counter(self):
        self.counter = self.counter + 1
        self.label_2.setText(f"{self.counter} times.")


if __name__ == "__main__":
    my_app = QApplication(sys.argv)
    window = MyWindow()
    window.show()

    my_app.exec_()
    sys.exit(0)

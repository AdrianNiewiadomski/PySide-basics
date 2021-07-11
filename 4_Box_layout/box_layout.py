import sys
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGroupBox, QPushButton


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My window in PySide2")
        self.setGeometry(0, 0, 640, 320)

        self.crete_h_box_layout()

        v_box_layout = QVBoxLayout()
        v_box_layout.addWidget(self.group_box)
        self.setLayout(v_box_layout)

    def crete_h_box_layout(self):
        self.group_box = QGroupBox()

        h_box_layout = QHBoxLayout()

        button1 = QPushButton("Button 1", self)
        button1.setMaximumHeight(30)
        h_box_layout.addWidget(button1)

        button2 = QPushButton("Button 2", self)
        button2.setMaximumHeight(30)
        h_box_layout.addWidget(button2)

        self.group_box.setLayout(h_box_layout)


if __name__ == "__main__":
    my_app = QApplication(sys.argv)
    window = MyWindow()
    window.show()

    my_app.exec_()
    sys.exit(0)
import sys
import time
from PySide2.QtWidgets import QApplication, QWidget


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My first window in PySide2")
        x_position = 0
        y_position = 0
        width_of_window = 640
        height_of_window = 320
        self.setGeometry(x_position, y_position, width_of_window, height_of_window)

        # The resize of the window may be disabled.
        # self.setMinimumWidth(640)
        # self.setMaximumWidth(640)
        # self.setMinimumHeight(320)
        # self.setMaximumHeight(320)


if __name__ == "__main__":
    my_app = QApplication(sys.argv)
    window = MyWindow()
    window.show()

    time.sleep(3)
    # You may resize window.
    window.resize(640, 640)

    my_app.exec_()
    sys.exit(0)
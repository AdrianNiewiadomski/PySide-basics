import sys

from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

my_app = QApplication(sys.argv)


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My window")
        self.setGeometry(0, 0, 480, 320)

        self._setup_buttons()

    def _setup_buttons(self):
        self.button1 = QPushButton("Show message box 1", self)
        self.button1.resize(200, 32)
        self.button1.move(150, 50)
        self.button1.clicked.connect(self.show_message_box_1)

        self.button2 = QPushButton("Show message box 2", self)
        self.button2.resize(200, 32)
        self.button2.move(150, 90)
        self.button2.clicked.connect(self.show_message_box_2)

        self.button3 = QPushButton("Show message box 3", self)
        self.button3.resize(200, 32)
        self.button3.move(150, 130)
        self.button3.clicked.connect(self.show_message_box_3)

        self.button4 = QPushButton("Show message box 4", self)
        self.button4.resize(200, 32)
        self.button4.move(150, 170)
        self.button4.clicked.connect(self.show_message_box_4)

    def show_message_box_1(self):
        print("show_message_box called")
        msgBox = QMessageBox()
        msgBox.setText("The document has been modified.")
        msgBox.exec_()

    def show_message_box_2(self):
        msgBox = QMessageBox()
        msgBox.setText("The document has been modified.")
        msgBox.setInformativeText("Do you want to save your changes?")
        msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
        msgBox.setDefaultButton(QMessageBox.Save)
        ret = msgBox.exec_()
        self.perform_some_action(ret)

    @staticmethod
    def perform_some_action(ret):
        if ret == QMessageBox.Save:
            print("Save was clicked")
        elif ret == QMessageBox.Discard:
            print("Don't save was clicked")
        elif ret == QMessageBox.Cancel:
            print("cancel was clicked")
        else:
            print("should never be reached")

    def show_message_box_3(self):
        ret = QMessageBox.warning(self, self.tr("My Application"),
                                  self.tr("The document has been modified.\n" + \
                                          "Do you want to save your changes?"),
                                  QMessageBox.Save | QMessageBox.Discard
                                  | QMessageBox.Cancel,
                                  QMessageBox.Save)
        self.perform_some_action(ret)


    def show_message_box_4(self):
        user_info = QMessageBox.question(self, "confirmation", "Quit the app?", QMessageBox.Yes | QMessageBox.No)

        if user_info == QMessageBox.Yes:
            my_app.quit()


if __name__ == "__main__":

    window = MyWindow()
    window.show()

    my_app.exec_()
    sys.exit(0)

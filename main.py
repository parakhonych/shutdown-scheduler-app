import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from UI_main_window import Ui_MainWindow



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.functions = {
            "Shutdown": "/s",
            "Log off": "/l",
            "Restart": "/r",
        }
        for value in self.functions:
            self.combo_box_function.addItem(value)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()
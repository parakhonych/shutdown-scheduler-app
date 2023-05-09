import sys
import os
from PyQt6.QtWidgets import QMainWindow, QApplication
from UI_main_window import Ui_MainWindow
from PyQt6.QtCore import QTimer

TIME_UNITS = {
    "hour": 3600,
    "minute": 60,
    "second": 1
}


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.functions = {
            "Shutdown": "/s",
            "Restart": "/r",
        }
        for value in self.functions:
            self.combo_box_function.addItem(value)

        self.button_start.clicked.connect(self.start)
        self.button_stop.clicked.connect(self.stop)
        self.button_exit.clicked.connect(self.close)
        self.action_exit.triggered.connect(self.close)

    def start(self):
        self.button_stop.setEnabled(True)
        self.button_start.setEnabled(False)
        self.time = self.spin_box_hours.value()*TIME_UNITS['hour'] + self.spin_box_minutes.value() * TIME_UNITS['minute'] \
                    + self.spin_box_seconds.value()
        os.system(f'shutdown {self.functions[self.combo_box_function.currentText()]} /t {self.time}')
        self.timer = QTimer()
        self.timer.timeout.connect(self.__update_label)
        self.timer.start(1000)  # Update label every 1000 ms (1 second)


    def __update_label(self):
        self.time += -1
        hours = self.time//TIME_UNITS['hour']
        minutes = self.time % TIME_UNITS['hour']//TIME_UNITS['minute']
        seconds = self.time % TIME_UNITS['hour'] % TIME_UNITS['minute']
        self.label_time.setText(f"{hours:02}h:{minutes:02}m:{seconds:02}s")
        if self.time == 0:
            self.timer.stop()

    def stop(self):
        self.button_stop.setEnabled(False)
        self.button_start.setEnabled(True)
        self.timer.stop()
        os.system(f'shutdown /a')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()
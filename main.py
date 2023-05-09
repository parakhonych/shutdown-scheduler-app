import sys
import os
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox
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
        self.spin_box_hours.valueChanged.connect(self.live_show_timer)
        self.spin_box_minutes.valueChanged.connect(self.live_show_timer)
        self.spin_box_seconds.valueChanged.connect(self.live_show_timer)
        self.action_autor.triggered.connect(self.autor)
        self.action_about.triggered.connect(self.about)
        self.action_help.triggered.connect(self.help)


    def start(self):
        self.button_stop.setEnabled(True)
        self.button_start.setEnabled(False)
        self.time = self.spin_box_hours.value()*TIME_UNITS['hour'] \
                    + self.spin_box_minutes.value() * TIME_UNITS['minute'] + self.spin_box_seconds.value()
        os.system(f'shutdown {self.functions[self.combo_box_function.currentText()]} /t {self.time}')
        self.timer = QTimer()
        self.timer.timeout.connect(self.__update_label)
        self.timer.start(1000)  # Update label every 1000 ms (1 second)

    def live_show_timer(self):
        self.time = self.spin_box_hours.value() * TIME_UNITS['hour'] + \
                    self.spin_box_minutes.value() * TIME_UNITS['minute'] + self.spin_box_seconds.value()
        self.__time_dispay()

    def __update_label(self):
        self.time += -1
        self.__time_dispay()
        if self.time == 0:
            self.timer.stop()

    def __time_dispay(self):
        hours = self.time // TIME_UNITS['hour']
        minutes = self.time % TIME_UNITS['hour'] // TIME_UNITS['minute']
        seconds = self.time % TIME_UNITS['hour'] % TIME_UNITS['minute']
        self.label_time.setText(f"{hours:02}h:{minutes:02}m:{seconds:02}s")

    def stop(self):
        self.button_stop.setEnabled(False)
        self.button_start.setEnabled(True)
        self.timer.stop()
        os.system(f'shutdown /a')

    def help(self):
        text = """              
                <p style="text-align: center">
                    <table>
                        <tr><td>The application can be used to set a countdown until the computer </td></tr>
                        <tr><td>shutdown or reboot, with the ability to track how much time is left.</td></tr>
                        <tr><td>To use the program, you should first set the desired time using the </td></tr>
                        <tr><td>appropriate combo boxes, and then click the START button. If you want to</td></tr>
                        <tr><td>cancel this action, just press the STOP button. It is worth noting that the </td></tr>
                        <tr><td>EXIT button closes the program but does not cancel the already set off timer.</td></tr>     
                    </table>
               """
        QMessageBox.information(self, "About", text)

    def about(self):
        text = """              
                                                <p style="text-align: center">
                                               <table>
                                                   <tr><td>Program name:</td><td>Shutdown scheduler app</td></tr>
                                                   <tr><td>Version:</td><td>1.0.0</td></tr>
                                               </table>
                                              """

        QMessageBox.information(self, "About", text)

    def autor(self):
        text = """              
                                        <p style="text-align: center">
                                       <table>
                                           <tr><td>Autor:</td><td>Volodymyr Parakhonych</td></tr>
                                           <tr><td>GitHub:</td><td><a href='https://github.com/vparakhonych'> vparakhonych </a></td></tr>
                                           <tr><td>Linkedin:</td><td><a href='https://www.linkedin.com/in/parakhonych/'>parakhonych</a></td></tr>
                                       </table>
                                      """

        QMessageBox.information(self, "Autor", text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()
import sys
import os

from PyQt5 import QtCore
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QTimer

'''

Interrompere lo spegnimento del PC: shutdown /a

'''

# Variabile globale
DURATION_INT = 300

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Dichiarazione variabili
        self.time_left_int = DURATION_INT
        self.widget_counter_int = 0

        # Temporizza lo spegnimento fatto dal terminale/cmd
        os.system('shutdown /s /t '+str(DURATION_INT))
        # Carica .ui ed esegui la funzione self.timer_start()
        self.changeScreen("mainWin.ui",self.timer_start)

    def changeScreen(self, fileUi, nextFunct=""):
        # Memorizza la funzione da chiamare
        self.__nextFunct = nextFunct
        # Carica file ui
        uic.loadUi(fileUi, self)
        # Se la funzione successiva è impostata chiamala
        if self.__nextFunct != "":
            self.__nextFunct()
        # Mostra GUI
        self.show()

    def timer_start(self):
        # Imposta un Timer di PyQt5
        self.my_qtimer = QTimer(self)
        # Ad ogni secondo chiama la funzione self.updateTimer()
        self.my_qtimer.timeout.connect(self.updateTimer)
        # Starta il timer dopo 1000 msec (1 sec)
        self.my_qtimer.start(1000)

    def updateTimer(self):
        # Decrementa il timer e aggiorna il widget
        self.time_left_int = self.time_left_int-1
        self.lcdNumber.display(self.time_left_int)

# Start
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


'''

Interrompere lo spegnimento del PC: shutdown /a

'''
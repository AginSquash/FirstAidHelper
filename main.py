import sys
from PyQt5 import QtWidgets

# UI_generated

import HelpScreen

class FirstAidHelper(QtWidgets.QMainWindow, HelpScreen.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button.clicked.connect(self.p)

    def p(self):
        print("OKKK")

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = FirstAidHelper()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
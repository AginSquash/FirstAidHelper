import sys

from PyQt5 import QtGui, QtWidgets, QtCore #import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QListWidget
from PyQt5.Qt import pyqtSignal, QLabel

# UI_generated
import HelpScreen
import MainScreen
import QuickHelper


class MainMenu(QMainWindow, MainScreen.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushFAH_button.clicked.connect(self.OpenFAH)
        self.pushQH_button.clicked.connect(self.OpenQH)

    def OpenQH(self):
        self.close()
        self.QH = OpenQuickHelper()
        self.QH.show()

    def OpenFAH(self):
        print("OK!")
        self.close()
        self.fah = FirstAidHelper()
        self.fah.show()
        
class OpenQuickHelper(QMainWindow, QuickHelper.Ui_QuickHelper):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loadingList()
        self.pushBackButton.clicked.connect(self.toMainMenu)

    def loadingList(self):
        self.list = self.listWidget

        for n in range(100):
            self.list.addItem(str(n))

        self.list.itemActivated.connect(self.itemActivated_event)

    def itemActivated_event(self, item):
        print(item.text())

    def toMainMenu(self):
        self.close()
        self.mainmenu = MainMenu()
        self.mainmenu.show()

class FirstAidHelper(QMainWindow, HelpScreen.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button_goBack.clicked.connect(self.goBack)
        self.button.clicked.connect(self.CreateRequest)

    def CreateRequest(self):
        name = self.name_in.toPlainText()
        adress = self.adress_in.toPlainText()
        symptom = self.symptom_in.toPlainText()

        json_request = '''
        {
            "name": $name,
            "adress": $adress,
            "symptom": $symptom
        }
        '''

        json_request = json_request.replace("$name", name).replace("$adress", adress).replace("$symptom", symptom)

        print(json_request)

        btn = QtWidgets.QPushButton("Скорая скоро приедет. Нажмите для продолжения.", self)
        btn.clicked.connect(self.goBack)
        btn.setGeometry(QtCore.QRect(0, 350, 375, 60))
        btn.show()
        #self.goBack()

    def goBack(self):
        self.close()
        self.mainmenu = MainMenu()
        self.mainmenu.show()


def main():
    app = QApplication(sys.argv)
    window = MainMenu()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()

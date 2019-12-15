import sys
from PyQt5 import QtWidgets

# UI_generated
import HelpScreen
import MainScreen

class MainMenu(QtWidgets.QMainWindow, MainScreen.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.closeWindow)

    def closeWindow(self):
        self.close()
        

class FirstAidHelper(QtWidgets.QMainWindow, HelpScreen.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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

        self.close()
        self.mainmenu = MainMenu()
        self.mainmenu.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = FirstAidHelper()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
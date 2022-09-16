from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        
        self.setWindowTitle("bla")
        self.setGeometry(400, 300, 600, 400)
        
        self.text = QtWidgets.QLabel(self)
        
        #self.text = QtWidgets.QLabel(self)
        #self.text.setText("blabla")
        #self.text.move(100, 100)
        
        self.buton = QtWidgets.QPushButton(self)
        self.buton.move(200, 200)
        self.buton.setText("bla")
        self.buton.clicked.connect(self.btn)


    def btn(self):
        print("bla")
        self.text.setText("blabla")
        self.text.move(100, 100)
def aplic():
    app = QApplication(sys.argv)
    window = Window()
    
    window.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    aplic()

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(492, 463)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 461, 41))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setKerning(False)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.but0 = QtWidgets.QPushButton(self.centralwidget)
        self.but0.setGeometry(QtCore.QRect(30, 370, 111, 60))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.but0.setFont(font)
        self.but0.setObjectName("but0")
        self.butrav = QtWidgets.QPushButton(self.centralwidget)
        self.butrav.setGeometry(QtCore.QRect(160, 370, 111, 60))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.butrav.setFont(font)
        self.butrav.setObjectName("butrav")
        self.but1 = QtWidgets.QPushButton(self.centralwidget)
        self.but1.setGeometry(QtCore.QRect(30, 300, 111, 60))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.but1.setFont(font)
        self.but1.setObjectName("but1")
        self.but2 = QtWidgets.QPushButton(self.centralwidget)
        self.but2.setGeometry(QtCore.QRect(160, 300, 111, 60))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.but2.setFont(font)
        self.but2.setObjectName("but2")
        self.but3 = QtWidgets.QPushButton(self.centralwidget)
        self.but3.setGeometry(QtCore.QRect(300, 300, 111, 60))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.but3.setFont(font)
        self.but3.setObjectName("but3")
        self.but4 = QtWidgets.QPushButton(self.centralwidget)
        self.but4.setGeometry(QtCore.QRect(30, 220, 111, 60))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.but4.setFont(font)
        self.but4.setObjectName("but4")
        self.but5 = QtWidgets.QPushButton(self.centralwidget)
        self.but5.setGeometry(QtCore.QRect(160, 220, 111, 60))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.but5.setFont(font)
        self.but5.setObjectName("but5")
        self.but6 = QtWidgets.QPushButton(self.centralwidget)
        self.but6.setGeometry(QtCore.QRect(300, 220, 111, 60))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.but6.setFont(font)
        self.but6.setObjectName("but6")
        self.but7 = QtWidgets.QPushButton(self.centralwidget)
        self.but7.setGeometry(QtCore.QRect(30, 150, 111, 60))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.but7.setFont(font)
        self.but7.setObjectName("but7")
        self.but8 = QtWidgets.QPushButton(self.centralwidget)
        self.but8.setGeometry(QtCore.QRect(160, 150, 111, 60))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.but8.setFont(font)
        self.but8.setObjectName("but8")
        self.but9 = QtWidgets.QPushButton(self.centralwidget)
        self.but9.setGeometry(QtCore.QRect(300, 150, 111, 60))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.but9.setFont(font)
        self.but9.setObjectName("but9")
        self.butpl = QtWidgets.QPushButton(self.centralwidget)
        self.butpl.setGeometry(QtCore.QRect(410, 150, 75, 41))
        self.butpl.setObjectName("butpl")
        self.butmin = QtWidgets.QPushButton(self.centralwidget)
        self.butmin.setGeometry(QtCore.QRect(410, 190, 75, 41))
        self.butmin.setObjectName("butmin")
        self.batdel = QtWidgets.QPushButton(self.centralwidget)
        self.batdel.setGeometry(QtCore.QRect(410, 270, 75, 41))
        self.batdel.setObjectName("batdel")
        self.batmno = QtWidgets.QPushButton(self.centralwidget)
        self.batmno.setGeometry(QtCore.QRect(410, 230, 75, 41))
        self.batmno.setObjectName("batmno")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "wow"))
        self.label.setText(_translate("MainWindow", "0"))
        self.but0.setText(_translate("MainWindow", "0"))
        self.butrav.setText(_translate("MainWindow", "="))
        self.but1.setText(_translate("MainWindow", "1"))
        self.but2.setText(_translate("MainWindow", "2"))
        self.but3.setText(_translate("MainWindow", "3"))
        self.but4.setText(_translate("MainWindow", "4"))
        self.but5.setText(_translate("MainWindow", "5"))
        self.but6.setText(_translate("MainWindow", "6"))
        self.but7.setText(_translate("MainWindow", "7"))
        self.but8.setText(_translate("MainWindow", "8"))
        self.but9.setText(_translate("MainWindow", "9"))
        self.butpl.setText(_translate("MainWindow", "+"))
        self.butmin.setText(_translate("MainWindow", "-"))
        self.batdel.setText(_translate("MainWindow", "/"))
        self.batmno.setText(_translate("MainWindow", "*"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
from PyQt5 import QtCore, QtGui, QtWidgets
from AddCarUI import Ui_CarAddition
from VerifyCarUI import Ui_VerifyCar


class Ui_MainWindow(object):
    def openAddCar(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_CarAddition()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
        
    def openVerifyCar(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_VerifyCar()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(636, 500)
        MainWindow.setFixedSize(636, 500)
            
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setContentsMargins(0, 0, 0, 0)
        self.Background = QtWidgets.QLabel(self.centralwidget)
        self.Background.setGeometry(QtCore.QRect(0, 0, 640, 480))
        self.Background.setText("")
        self.Background.setPixmap(QtGui.QPixmap("Interface/Background.png"))
        self.Background.setObjectName("Background")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.openAddCar())
        self.pushButton.setGeometry(QtCore.QRect(90, 270, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.openVerifyCar())
        self.pushButton_2.setGeometry(QtCore.QRect(410, 270, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 120, 251, 41))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 636, 21))
        self.menubar.setMouseTracking(True)
        self.menubar.setAcceptDrops(True)
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.hide()
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Add Car"))
        self.pushButton_2.setText(_translate("MainWindow", "Verify Car"))
        self.label_2.setText(_translate("MainWindow", "Parking Lot Access "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

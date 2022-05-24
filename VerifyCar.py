from PyQt5 import QtCore, QtGui, QtWidgets
from Warning import Ui_Dialog
from CameraDetection import vidRec
from OneCar import reco


class Ui_VerifyCar(object):
    def Popup(self):
        self.MainWindow = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
    def camUse(self):
        self.Popup()
        vidRec()
    def imgUse(self):
        reco()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Verify Car")
        MainWindow.resize(640, 480)
        MainWindow.setFixedSize(640, 480) 
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 641, 501))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Interface/Background.png"))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.camUse())
        self.pushButton_2.setGeometry(QtCore.QRect(410, 240, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.imgUse())
        self.pushButton.setGeometry(QtCore.QRect(90, 240, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 90, 251, 41))
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.hide()
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Verify Car"))
        self.pushButton_2.setText(_translate("MainWindow", "Use Camera"))
        self.pushButton.setText(_translate("MainWindow", "Use Image"))
        self.label_2.setText(_translate("MainWindow", "Verification "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_VerifyCar()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

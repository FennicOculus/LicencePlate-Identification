from PyQt5 import QtCore, QtGui, QtWidgets
from PlateDetection import Seg
from PlateExtraction import addCar

class Ui_CarAddition(object):
    def Manual(self):
        addCar()
    def auto(self):
        Seg()
    def setupUi(self, CarAddition):
        CarAddition.setObjectName("CarAddition")
        CarAddition.resize(640, 480)
        CarAddition.setFixedSize(640, 480) 
        CarAddition.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(CarAddition)
        self.centralwidget.setObjectName("centralwidget")
        self.Background = QtWidgets.QLabel(self.centralwidget)
        self.Background.setGeometry(QtCore.QRect(0, 0, 641, 441))
        self.Background.setText("")
        self.Background.setTextFormat(QtCore.Qt.AutoText)
        self.Background.setPixmap(QtGui.QPixmap("Interface/Background.png"))
        self.Background.setObjectName("Background")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 90, 251, 41))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.auto())
        self.pushButton_4.setGeometry(QtCore.QRect(60, 240, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.Manual())
        self.pushButton_3.setGeometry(QtCore.QRect(380, 240, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        CarAddition.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CarAddition)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        CarAddition.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CarAddition)
        self.statusbar.setObjectName("statusbar")
        CarAddition.setStatusBar(self.statusbar)

        self.retranslateUi(CarAddition)
        QtCore.QMetaObject.connectSlotsByName(CarAddition)

    def retranslateUi(self, CarAddition):
        _translate = QtCore.QCoreApplication.translate
        CarAddition.setWindowTitle(_translate("CarAddition", "Add Car"))
        self.label_3.setText(_translate("CarAddition", "Adding Car"))
        self.pushButton_4.setText(_translate("CarAddition", "Automatic"))
        self.pushButton_3.setText(_translate("CarAddition", "Manual"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CarAddition = QtWidgets.QMainWindow()
    ui = Ui_CarAddition()
    ui.setupUi(CarAddition)
    CarAddition.show()
    sys.exit(app.exec_())

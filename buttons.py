from PyQt5 import QtCore, QtGui, QtWidgets
from cvpart import ImageDetection 

class Ui_Buttons(object):
    def __init__(self):
        self.image_detector = ImageDetection()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.but1 = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.but1.setFont(font)
        self.but1.setObjectName("but1")

        self.but1.clicked.connect(lambda: self.image_detector.video_one())

        self.verticalLayout.addWidget(self.but1)
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.but2 = QtWidgets.QPushButton(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.but2.setFont(font)
        self.but2.setObjectName("but2")

        self.but2.clicked.connect(lambda: self.image_detector.manual_video())


        self.verticalLayout_2.addWidget(self.but2)
        self.horizontalLayout.addWidget(self.frame_4)
        self.horizontalLayout_2.addWidget(self.frame)


        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.but3 = QtWidgets.QPushButton(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.but3.setFont(font)
        self.but3.setObjectName("but3")

        self.verticalLayout_3.addWidget(self.but3)
        self.horizontalLayout.addWidget(self.frame_5)
        self.horizontalLayout_2.addWidget(self.frame_5)


        MainWindow.setCentralWidget(self.centralwidget)


        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.but1.setText(_translate("MainWindow", "Live Detection"))
        self.but2.setText(_translate("MainWindow", "Manual Detection"))
        self.but3.setText(_translate("MainWindow", "Image Detection"))


if __name__ == "_main_":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Buttons()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

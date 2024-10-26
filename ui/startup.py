from PyQt5 import QtCore, QtGui, QtWidgets
from ui.register import Ui_OtherWindow1
from ui.login import Ui_OtherWindow2

class Ui_MainWindoww(object):
    def openWindow1(self, MainWindow):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_OtherWindow1()
        self.ui.setupUi(self.window, MainWindow)
        MainWindow.close()
        self.window.show()

    def openWindow2(self, MainWindow):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_OtherWindow2()
        self.ui.setupUi(self.window, MainWindow)
        MainWindow.close()
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(962, 449)
        MainWindow.setStyleSheet("background-color: #2E2E2E;")  # Dark background
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        # Title Frame
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.title = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        self.title.setFont(font)
        self.title.setStyleSheet("color: #FFFFFF;")  # White text
        self.horizontalLayout.addWidget(self.title)
        self.verticalLayout_3.addWidget(self.frame)

        # Main Button Frame
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        # Login Section
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName("verticalLayout")

        self.og = QtWidgets.QLabel(self.frame_3)
        font.setPointSize(24)
        self.og.setFont(font)
        self.og.setStyleSheet("color: #FFFFFF;")  # White text
        self.verticalLayout.addWidget(self.og)

        self.loginBut = QtWidgets.QPushButton(self.frame_3)
        self.loginBut.setStyleSheet("""
            background-color: #007BFF;  /* Blue button */
            color: #FFFFFF;              /* White text */
            border: none;
            padding: 10px;
            font-size: 20px;
        """)
        self.loginBut.setObjectName("loginBut")
        self.loginBut.clicked.connect(lambda: self.openWindow2(MainWindow))
        self.verticalLayout.addWidget(self.loginBut)

        self.horizontalLayout_2.addWidget(self.frame_3)

        # Signup Section
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.new_2 = QtWidgets.QLabel(self.frame_4)
        self.new_2.setFont(font)
        self.new_2.setStyleSheet("color: #FFFFFF;")  # White text
        self.verticalLayout_2.addWidget(self.new_2)

        self.signupBut = QtWidgets.QPushButton(self.frame_4)
        self.signupBut.setStyleSheet("""
            background-color: #28A745;  /* Green button */
            color: #FFFFFF;              /* White text */
            border: none;
            padding: 10px;
            font-size: 20px;
        """)
        self.signupBut.setObjectName("signupBut")
        self.signupBut.clicked.connect(lambda: self.openWindow1(MainWindow))
        self.verticalLayout_2.addWidget(self.signupBut)

        self.horizontalLayout_2.addWidget(self.frame_4)
        self.verticalLayout_3.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 962, 26))
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
        self.title.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">RAJ SOIN WARRIORS</p></body></html>"))
        self.og.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">OG Member?</p></body></html>"))
        self.loginBut.setText(_translate("MainWindow", "LOGIN"))
        self.new_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">New?</p></body></html>"))
        self.signupBut.setText(_translate("MainWindow", "SIGNUP"))

import sys




def startApp():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindoww()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
from PyQt5 import QtCore, QtGui, QtWidgets
import re

class Ui_OtherWindow1(object):
    def backWindow(self, MainWindow):
        from startup import Ui_MainWindoww
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindoww()
        self.ui.setupUi(self.window)
        MainWindow.close()
        self.window.show()

    def buttons(self, MainWindow):
        from buttons import Ui_Buttons
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Buttons()
        self.ui.setupUi(self.window)
        MainWindow.close()
        self.window.show()

    def is_valid_email(self, email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    def submit_data(self, MainWindow):
        email_text = self.email.text()  # Retrieve text from email field
        password_text = self.passw.text()  # Retrieve text from password field
    
        if not self.is_valid_email(email_text):
            QtWidgets.QMessageBox.warning(None, "Invalid Input", "Please enter a valid email address.")
            return

        if not password_text:
            QtWidgets.QMessageBox.warning(None, "Invalid Input", "Password cannot be empty.")
            return

        QtWidgets.QMessageBox.information(None, "Success", "Registration Successful!")
        self.buttons(MainWindow)

    def setupUi(self, MainWindow, previous_window=None):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(931, 750)
        MainWindow.setStyleSheet("background-color: #2A2A2A;")  # Dark background color
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        # Back Button
        self.backBut = QtWidgets.QPushButton(self.centralwidget)
        self.backBut.setStyleSheet("QPushButton { background-color: #4A90E2; color: white; border: none; padding: 10px; border-radius: 5px; }"
                                    "QPushButton:hover { background-color: #357ABD; }")
        self.backBut.setFont(QtGui.QFont("Bahnschrift SemiBold", 20))
        self.backBut.setObjectName("backBut")
        self.backBut.clicked.connect(lambda: self.backWindow(MainWindow))
        self.verticalLayout.addWidget(self.backBut)

        # Title
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.loginSignup = QtWidgets.QLabel(self.frame)
        self.loginSignup.setFont(QtGui.QFont("Arial", 22))
        self.loginSignup.setStyleSheet("color: white;")  # White text color
        self.loginSignup.setAlignment(QtCore.Qt.AlignCenter)
        self.loginSignup.setObjectName("loginSignup")
        self.horizontalLayout.addWidget(self.loginSignup)
        self.verticalLayout.addWidget(self.frame)

        # Input Fields Frame
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")

        # Email Input
        self.frame_9 = QtWidgets.QFrame(self.frame_2)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.emailLabel = QtWidgets.QLabel(self.frame_9)
        self.emailLabel.setFont(QtGui.QFont("Bahnschrift SemiBold", 18))
        self.emailLabel.setStyleSheet("color: white;")  # White text color
        self.verticalLayout_9.addWidget(self.emailLabel)
        self.email = QtWidgets.QLineEdit(self.frame_9)
        self.email.setFont(QtGui.QFont("Bahnschrift SemiBold", 16))
        self.email.setStyleSheet("QLineEdit { padding: 10px; border-radius: 5px; background-color: #4A4A4A; color: white; }")
        self.verticalLayout_9.addWidget(self.email)
        self.verticalLayout_8.addWidget(self.frame_9)

        # Password Input
        self.frame_7 = QtWidgets.QFrame(self.frame_2)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.passLabel = QtWidgets.QLabel(self.frame_7)
        self.passLabel.setFont(QtGui.QFont("Bahnschrift SemiBold", 18))
        self.passLabel.setStyleSheet("color: white;")  # White text color
        self.verticalLayout_5.addWidget(self.passLabel)
        self.passw = QtWidgets.QLineEdit(self.frame_7)
        self.passw.setFont(QtGui.QFont("Bahnschrift SemiBold", 16))
        self.passw.setStyleSheet("QLineEdit { padding: 10px; border-radius: 5px; background-color: #4A4A4A; color: white; }")
        self.passw.setEchoMode(QtWidgets.QLineEdit.Password)
        self.verticalLayout_5.addWidget(self.passw)
        self.verticalLayout_8.addWidget(self.frame_7)

        # Submit Button
        self.frame_12 = QtWidgets.QFrame(self.frame_2)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_12)
        self.submitBut = QtWidgets.QPushButton(self.frame_12)
        self.submitBut.setStyleSheet("QPushButton { background-color: #4CAF50; color: white; border: none; padding: 10px; border-radius: 5px; }"
                                      "QPushButton:hover { background-color: #45A049; }")
        self.submitBut.setFont(QtGui.QFont("Bahnschrift SemiBold", 20))
        self.submitBut.setObjectName("submitBut")
        self.submitBut.clicked.connect(lambda: self.submit_data(MainWindow))
        self.verticalLayout_12.addWidget(self.submitBut)
        self.verticalLayout_8.addWidget(self.frame_12)

        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 931, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Registration"))
        self.backBut.setText(_translate("MainWindow", "Back"))
        self.loginSignup.setText(_translate("MainWindow", "SIGNUP"))
        self.emailLabel.setText(_translate("MainWindow", "Email"))
        self.passLabel.setText(_translate("MainWindow", "Password"))
        self.submitBut.setText(_translate("MainWindow", "Submit"))

if __name__ == "_main_":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_OtherWindow1()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
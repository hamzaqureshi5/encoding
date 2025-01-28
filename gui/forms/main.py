# Form implementation generated from reading ui file 'mainV0.1.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(791, 450)
        MainWindow.setMinimumSize(QtCore.QSize(791, 450))
        MainWindow.setMaximumSize(QtCore.QSize(791, 450))
        MainWindow.setStyleSheet(" background-color: #f0f0f0;\n"
"            ")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 0, 791, 551))
        self.frame.setMinimumSize(QtCore.QSize(791, 551))
        self.frame.setMaximumSize(QtCore.QSize(791, 551))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.groupBox = QtWidgets.QGroupBox(parent=self.frame)
        self.groupBox.setGeometry(QtCore.QRect(0, 40, 761, 71))
        self.groupBox.setStyleSheet(" QGroupBox {\n"
"                border: 2px solid #0078D7;\n"
"                border-radius: 8px;\n"
"                margin-top: 10px;\n"
"                background-color: #ffffff;\n"
"                font-size: 12pt;\n"
"                font-weight: bold;\n"
"                color: #0078D7;\n"
"            }\n"
"QGroupBox::title {\n"
"                subcontrol-origin: margin;\n"
"                subcontrol-position: top left;\n"
"                padding: 0 5px;\n"
"            }")
        self.groupBox.setObjectName("groupBox")
        self.iccid_dec_btn = QtWidgets.QPushButton(parent=self.groupBox)
        self.iccid_dec_btn.setGeometry(QtCore.QRect(660, 30, 91, 31))
        self.iccid_dec_btn.setStyleSheet(" QPushButton {\n"
"                background-color: #0078D7;\n"
"                color: white;\n"
"                border-radius: 6px;\n"
"                padding: 5px 10px;\n"
"                font-size: 10pt;\n"
"                font-weight: bold;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #005a9e;\n"
"            }\n"
"            ")
        self.iccid_dec_btn.setObjectName("iccid_dec_btn")
        self.iccid_input = QtWidgets.QLineEdit(parent=self.groupBox)
        self.iccid_input.setGeometry(QtCore.QRect(10, 30, 260, 30))
        self.iccid_input.setStyleSheet(" QLineEdit {\n"
"                border: 1px solid #d3d3d3;\n"
"                border-radius: 5px;\n"
"                padding: 5px;\n"
"                background-color: #ffffff;\n"
"                font-family: \"Segoe UI\";\n"
"                font-size: 10pt;\n"
"            }")
        self.iccid_input.setMaxLength(20)
        self.iccid_input.setObjectName("iccid_input")
        self.iccid_output = QtWidgets.QLineEdit(parent=self.groupBox)
        self.iccid_output.setGeometry(QtCore.QRect(280, 30, 260, 30))
        self.iccid_output.setStyleSheet(" QLineEdit {\n"
"                border: 1px solid #d3d3d3;\n"
"                border-radius: 5px;\n"
"                padding: 5px;\n"
"                background-color: #ffffff;\n"
"                font-family: \"Segoe UI\";\n"
"                font-size: 10pt;\n"
"            }")
        self.iccid_output.setReadOnly(True)
        self.iccid_output.setObjectName("iccid_output")
        self.iccid_enc_btn = QtWidgets.QPushButton(parent=self.groupBox)
        self.iccid_enc_btn.setGeometry(QtCore.QRect(560, 30, 91, 31))
        self.iccid_enc_btn.setStyleSheet(" QPushButton {\n"
"                background-color: #0078D7;\n"
"                color: white;\n"
"                border-radius: 6px;\n"
"                padding: 5px 10px;\n"
"                font-size: 10pt;\n"
"                font-weight: bold;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #005a9e;\n"
"            }\n"
"            ")
        self.iccid_enc_btn.setObjectName("iccid_enc_btn")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.frame)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 200, 761, 201))
        self.groupBox_2.setStyleSheet(" QGroupBox {\n"
"                border: 2px solid #0078D7;\n"
"                border-radius: 8px;\n"
"                margin-top: 10px;\n"
"                background-color: #ffffff;\n"
"                font-size: 12pt;\n"
"                font-weight: bold;\n"
"                color: #0078D7;\n"
"            }\n"
"QGroupBox::title {\n"
"                subcontrol-origin: margin;\n"
"                subcontrol-position: top left;\n"
"                padding: 0 5px;\n"
"            }")
        self.groupBox_2.setObjectName("groupBox_2")
        self.enc_keys_conv_btn = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.enc_keys_conv_btn.setGeometry(QtCore.QRect(640, 150, 91, 31))
        self.enc_keys_conv_btn.setStyleSheet(" QPushButton {\n"
"                background-color: #0078D7;\n"
"                color: white;\n"
"                border-radius: 6px;\n"
"                padding: 5px 10px;\n"
"                font-size: 10pt;\n"
"                font-weight: bold;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #005a9e;\n"
"            }\n"
"            ")
        self.enc_keys_conv_btn.setObjectName("enc_keys_conv_btn")
        self.ki = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.ki.setGeometry(QtCore.QRect(10, 30, 281, 30))
        self.ki.setStyleSheet(" QLineEdit {\n"
"                border: 1px solid #d3d3d3;\n"
"                border-radius: 5px;\n"
"                padding: 5px;\n"
"                background-color: #ffffff;\n"
"                font-family: \"Segoe UI\";\n"
"                font-size: 10pt;\n"
"            }")
        self.ki.setMaxLength(32)
        self.ki.setObjectName("ki")
        self.op = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.op.setGeometry(QtCore.QRect(300, 30, 281, 30))
        self.op.setStyleSheet(" QLineEdit {\n"
"                border: 1px solid #d3d3d3;\n"
"                border-radius: 5px;\n"
"                padding: 5px;\n"
"                background-color: #ffffff;\n"
"                font-family: \"Segoe UI\";\n"
"                font-size: 10pt;\n"
"            }")
        self.op.setMaxLength(32)
        self.op.setObjectName("op")
        self.k4 = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.k4.setGeometry(QtCore.QRect(10, 80, 571, 30))
        self.k4.setStyleSheet(" QLineEdit {\n"
"                border: 1px solid #d3d3d3;\n"
"                border-radius: 5px;\n"
"                padding: 5px;\n"
"                background-color: #ffffff;\n"
"                font-family: \"Segoe UI\";\n"
"                font-size: 10pt;\n"
"            }")
        self.k4.setMaxLength(64)
        self.k4.setObjectName("k4")
        self.opc = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.opc.setGeometry(QtCore.QRect(10, 130, 281, 30))
        self.opc.setStyleSheet(" QLineEdit {\n"
"                border: 1px solid #d3d3d3;\n"
"                border-radius: 5px;\n"
"                padding: 5px;\n"
"                background-color: #ffffff;\n"
"                font-family: \"Segoe UI\";\n"
"                font-size: 10pt;\n"
"            }")
        self.opc.setReadOnly(True)
        self.opc.setObjectName("opc")
        self.eki = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.eki.setGeometry(QtCore.QRect(300, 130, 281, 30))
        self.eki.setStyleSheet(" QLineEdit {\n"
"                border: 1px solid #d3d3d3;\n"
"                border-radius: 5px;\n"
"                padding: 5px;\n"
"                background-color: #ffffff;\n"
"                font-family: \"Segoe UI\";\n"
"                font-size: 10pt;\n"
"            }")
        self.eki.setReadOnly(True)
        self.eki.setObjectName("eki")
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.frame)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 120, 761, 71))
        self.groupBox_3.setStyleSheet(" QGroupBox {\n"
"                border: 2px solid #0078D7;\n"
"                border-radius: 8px;\n"
"                margin-top: 10px;\n"
"                background-color: #ffffff;\n"
"                font-size: 12pt;\n"
"                font-weight: bold;\n"
"                color: #0078D7;\n"
"            }\n"
"QGroupBox::title {\n"
"                subcontrol-origin: margin;\n"
"                subcontrol-position: top left;\n"
"                padding: 0 5px;\n"
"            }")
        self.groupBox_3.setObjectName("groupBox_3")
        self.imsi_enc_btn = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.imsi_enc_btn.setGeometry(QtCore.QRect(560, 30, 91, 31))
        self.imsi_enc_btn.setStyleSheet(" QPushButton {\n"
"                background-color: #0078D7;\n"
"                color: white;\n"
"                border-radius: 6px;\n"
"                padding: 5px 10px;\n"
"                font-size: 10pt;\n"
"                font-weight: bold;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #005a9e;\n"
"            }\n"
"            ")
        self.imsi_enc_btn.setObjectName("imsi_enc_btn")
        self.imsi_input = QtWidgets.QLineEdit(parent=self.groupBox_3)
        self.imsi_input.setGeometry(QtCore.QRect(10, 30, 261, 30))
        self.imsi_input.setStyleSheet(" QLineEdit {\n"
"                border: 1px solid #d3d3d3;\n"
"                border-radius: 5px;\n"
"                padding: 5px;\n"
"                background-color: #ffffff;\n"
"                font-family: \"Segoe UI\";\n"
"                font-size: 10pt;\n"
"            }")
        self.imsi_input.setMaxLength(15)
        self.imsi_input.setObjectName("imsi_input")
        self.imsi_output = QtWidgets.QLineEdit(parent=self.groupBox_3)
        self.imsi_output.setGeometry(QtCore.QRect(280, 30, 261, 30))
        self.imsi_output.setStyleSheet(" QLineEdit {\n"
"                border: 1px solid #d3d3d3;\n"
"                border-radius: 5px;\n"
"                padding: 5px;\n"
"                background-color: #ffffff;\n"
"                font-family: \"Segoe UI\";\n"
"                font-size: 10pt;\n"
"            }")
        self.imsi_output.setReadOnly(True)
        self.imsi_output.setObjectName("imsi_output")
        self.imsi_dec_btn = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.imsi_dec_btn.setGeometry(QtCore.QRect(660, 30, 91, 31))
        self.imsi_dec_btn.setStyleSheet(" QPushButton {\n"
"                background-color: #0078D7;\n"
"                color: white;\n"
"                border-radius: 6px;\n"
"                padding: 5px 10px;\n"
"                font-size: 10pt;\n"
"                font-weight: bold;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #005a9e;\n"
"            }\n"
"            ")
        self.imsi_dec_btn.setObjectName("imsi_dec_btn")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(300, 10, 151, 31))
        self.label.setStyleSheet("QLabel {\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 12pt;\n"
"    font-weight: bold;\n"
"    color: White;\n"
"   background-color: #0078D7;/* Or set a specific color if needed */\n"
"    padding: 5px;\n"
"    border-radius: 5px; /* Optional for rounded corners */\n"
"}")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 791, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile_Menu = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile_Menu.setObjectName("menuFile_Menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(parent=MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtGui.QAction(parent=MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile_Menu.addAction(self.actionOpen)
        self.menuFile_Menu.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile_Menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "ICCID"))
        self.iccid_dec_btn.setText(_translate("MainWindow", "Decode"))
        self.iccid_enc_btn.setText(_translate("MainWindow", "Encode"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Encryption Keys"))
        self.enc_keys_conv_btn.setText(_translate("MainWindow", "Convert"))
        self.groupBox_3.setTitle(_translate("MainWindow", "IMSI"))
        self.imsi_enc_btn.setText(_translate("MainWindow", "Encode"))
        self.imsi_dec_btn.setText(_translate("MainWindow", "Decode"))
        self.label.setText(_translate("MainWindow", "Encoder-Decoder"))
        self.menuFile_Menu.setTitle(_translate("MainWindow", "File Menu"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

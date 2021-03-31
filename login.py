# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

################################################################################
##
## EFit - Fitness management system
## Main executable file
## By ErtonDev
## Login
##
################################################################################

## MODULES
################################################################################
import io
import os
import subprocess
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import *
from pathlib import Path

## SETUP
################################################################################
# client's path to find every resource in client's directories
client_path = Path(__file__)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QIcon(str((client_path / "../images/logo_efit.png").resolve())))
        MainWindow.resize(400, 550)
        MainWindow.setMinimumSize(QtCore.QSize(400, 550))
        MainWindow.setMaximumSize(QtCore.QSize(400, 550))

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 246, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 119, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 159, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 154, 6))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 246, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 246, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 119, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 159, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 154, 6))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 246, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 119, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 246, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 119, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 159, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 119, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 119, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(145, 145, 145))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        MainWindow.setPalette(palette)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.hola = QtWidgets.QLabel(self.centralwidget)
        self.hola.setGeometry(QtCore.QRect(0, 30, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.hola.setFont(font)
        self.hola.setScaledContents(True)
        self.hola.setAlignment(QtCore.Qt.AlignCenter)
        self.hola.setObjectName("hola")

        self.userLine = QtWidgets.QFrame(self.centralwidget)
        self.userLine.setGeometry(QtCore.QRect(40, 310, 321, 20))
        self.userLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.userLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.userLine.setObjectName("userLine")

        self.passLine = QtWidgets.QFrame(self.centralwidget)
        self.passLine.setGeometry(QtCore.QRect(40, 400, 321, 20))
        self.passLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.passLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.passLine.setObjectName("passLine")

        self.userText = QtWidgets.QLineEdit(self.centralwidget)
        self.userText.setEnabled(True)
        self.userText.setGeometry(QtCore.QRect(70, 290, 290, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.userText.setFont(font)
        self.userText.setText("")
        self.userText.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.userText.setObjectName("userText")

        self.passText = QtWidgets.QLineEdit(self.centralwidget)
        self.passText.setEnabled(True)
        self.passText.setGeometry(QtCore.QRect(70, 380, 290, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.passText.setFont(font)
        self.passText.setText("")
        self.passText.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passText.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.passText.setObjectName("passText")

        self.userLabel = QtWidgets.QLabel(self.centralwidget)
        self.userLabel.setGeometry(QtCore.QRect(40, 270, 321, 17))
        self.userLabel.setObjectName("userLabel")

        self.passLabel = QtWidgets.QLabel(self.centralwidget)
        self.passLabel.setGeometry(QtCore.QRect(40, 360, 321, 17))
        self.passLabel.setObjectName("passLabel")

        self.btnLogin = QtWidgets.QPushButton(self.centralwidget)
        self.btnLogin.setGeometry(QtCore.QRect(240, 430, 121, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.btnLogin.setFont(font)
        self.btnLogin.setAutoFillBackground(False)
        self.btnLogin.setAutoDefault(False)
        self.btnLogin.setDefault(True)
        self.btnLogin.setFlat(False)
        self.btnLogin.setObjectName("btnLogin")

        self.btnRegister = QtWidgets.QPushButton(self.centralwidget)
        self.btnRegister.setGeometry(QtCore.QRect(240, 470, 121, 21))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.btnRegister.setFont(font)
        self.btnRegister.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnRegister.setFlat(True)
        self.btnRegister.setObjectName("btnRegister")

        self.foto = QtWidgets.QLabel(self.centralwidget)
        self.foto.setGeometry(QtCore.QRect(40, 90, 311, 181))
        self.foto.setText("")
        self.foto.setPixmap(QtGui.QPixmap(str((client_path / "../images/undraw_Login_re_4vu2.png").resolve())))
        self.foto.setScaledContents(True)
        self.foto.setObjectName("foto")

        self.userIcon = QtWidgets.QLabel(self.centralwidget)
        self.userIcon.setGeometry(QtCore.QRect(40, 290, 21, 21))
        self.userIcon.setText("")
        self.userIcon.setPixmap(QtGui.QPixmap(str((client_path / "../images/profile.png").resolve())))
        self.userIcon.setScaledContents(True)
        self.userIcon.setObjectName("userIcon")

        self.passIcon = QtWidgets.QLabel(self.centralwidget)
        self.passIcon.setGeometry(QtCore.QRect(40, 380, 21, 21))
        self.passIcon.setText("")
        self.passIcon.setPixmap(QtGui.QPixmap(str((client_path / "../images/lock.png").resolve())))
        self.passIcon.setScaledContents(True)
        self.passIcon.setObjectName("passIcon")

        self.info = QtWidgets.QLabel(self.centralwidget)
        self.info.setGeometry(QtCore.QRect(40, 430, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.info.setFont(font)
        self.info.setScaledContents(True)
        self.info.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.info.setWordWrap(True)
        self.info.setObjectName("info")

        self.userLine.raise_()
        self.passLine.raise_()
        self.userText.raise_()
        self.passText.raise_()
        self.userLabel.raise_()
        self.passLabel.raise_()
        self.btnLogin.raise_()
        self.btnRegister.raise_()
        self.foto.raise_()
        self.hola.raise_()
        self.userIcon.raise_()
        self.passIcon.raise_()
        self.info.raise_()

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 22))
        self.menubar.setObjectName("menubar")
        self.menuAyuda = QtWidgets.QMenu(self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        self.menuEFit = QtWidgets.QMenu(self.menubar)
        self.menuEFit.setObjectName("menuEFit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionManual = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("file")
        self.actionManual.setIcon(icon)
        self.actionManual.setObjectName("actionManual")
        self.actionAutor = QtWidgets.QAction(MainWindow)
        self.actionAutor.setObjectName("actionAutor")
        self.actionInformacion = QtWidgets.QAction(MainWindow)
        self.actionInformacion.setObjectName("actionInformacion")
        self.actionDetalles = QtWidgets.QAction(MainWindow)
        self.actionDetalles.setObjectName("actionDetalles")
        self.actionDesarrollador = QtWidgets.QAction(MainWindow)
        self.actionDesarrollador.setObjectName("actionDesarrollador")
        self.menuAyuda.addAction(self.actionManual)
        self.menuEFit.addAction(self.actionInformacion)
        self.menuEFit.addAction(self.actionDetalles)
        self.menuEFit.addSeparator()
        self.menuEFit.addAction(self.actionDesarrollador)
        self.menubar.addAction(self.menuEFit.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # funcionalidad
        # botones
        self.btnLogin.clicked.connect(self.goto_login)
        self.btnRegister.clicked.connect(self.goto_register)
        # toolbar
        self.actionManual.triggered.connect(lambda: self.action_clicked("Manual"))
        self.actionInformacion.triggered.connect(lambda: self.action_clicked("Información"))
        self.actionDetalles.triggered.connect(lambda: self.action_clicked("Detalles"))
        self.actionDesarrollador.triggered.connect(lambda: self.action_clicked("Desarrollador"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EFit Login"))
        self.hola.setText(_translate("MainWindow", "¡Hola!"))
        self.userText.setPlaceholderText(_translate("MainWindow", "pablito123"))
        self.passText.setPlaceholderText(_translate("MainWindow", "9876pppp"))
        self.userLabel.setText(_translate("MainWindow", "Nombre de usuario"))
        self.passLabel.setText(_translate("MainWindow", "Contraseña"))
        self.btnLogin.setStatusTip(_translate("MainWindow", "Inicia sesión"))
        self.btnLogin.setText(_translate("MainWindow", "Inicia sesión"))
        self.btnRegister.setStatusTip(_translate("MainWindow", "Registrate"))
        self.btnRegister.setText(_translate("MainWindow", "o registrate..."))
        self.info.setText(_translate("MainWindow", "Las cuentas de EFit no se almacenan en la nube, pero gracias a ella podrás crear varias sesiones en el mismo dispositivo."))
        self.menuAyuda.setTitle(_translate("MainWindow", "Ayuda"))
        self.menuEFit.setTitle(_translate("MainWindow", "EFit"))
        self.actionManual.setText(_translate("MainWindow", "Manual"))
        self.actionManual.setStatusTip(_translate("MainWindow", "Guía de uso de la ventana"))
        self.actionAutor.setText(_translate("MainWindow", "Autor"))
        self.actionInformacion.setText(_translate("MainWindow", "Información"))
        self.actionInformacion.setStatusTip(_translate("MainWindow", "Información del software"))
        self.actionDetalles.setText(_translate("MainWindow", "Detalles"))
        self.actionDetalles.setStatusTip(_translate("MainWindow", "Detalles de desarrollo", "0"))
        self.actionDesarrollador.setText(_translate("MainWindow", "Desarrollador"))
        self.actionDesarrollador.setStatusTip(_translate("MainWindow", "Información sobre el desarrollador"))

    def action_clicked(self, action):
        if action == "Manual":
            actionManualPop = QMessageBox()
            actionManualPop.setWindowTitle(action)
            actionManualPop.setText("Introduce tus datos rellenando los espacios en blanco.")
            actionManualPop.setIcon(QMessageBox.Information)
            actionManualPop.setStandardButtons(QMessageBox.Close|QMessageBox.Ok)
            actionManualPop.setDefaultButton(QMessageBox.Ok)
            actionManualPop.setDetailedText("Introduce tu nombre de usuario ya existente en el espacio correspondiente. Haz lo mismo con tu contraseña. En caso de no tener una cuenta introduce tus datos y pulsa *o registrarse...*. Esto creará una nueva cuenta a tu nombre en tu dispositivo.")
            actionManualPop_exe = actionManualPop.exec_()
        if action == "Información":
            actionInformaciónPop = QMessageBox()
            actionInformaciónPop.setWindowTitle(action)
            actionInformaciónPop.setText("EFit es un software de fitness para hacer deporte en casa monitorizando tu rendimiento y actividad física.")
            actionInformaciónPop.setIcon(QMessageBox.Information)
            actionInformaciónPop.setStandardButtons(QMessageBox.Close|QMessageBox.Ok)
            actionInformaciónPop.setDefaultButton(QMessageBox.Ok)
            actionInformaciónPop_exe = actionInformaciónPop.exec_()
        if action == "Detalles":
            actionDetallesPop = QMessageBox()
            actionDetallesPop.setWindowTitle(action)
            actionDetallesPop.setText("Desarrollado con Python.")
            actionDetallesPop.setIcon(QMessageBox.Information)
            actionDetallesPop.setStandardButtons(QMessageBox.Close|QMessageBox.Ok)
            actionDetallesPop.setDefaultButton(QMessageBox.Ok)
            actionDetallesPop.setDetailedText("import PyQT5\nimport io")
            actionDetallesPop_exe = actionDetallesPop.exec_()
        if action == "Desarrollador":
            actionDesarrolladorPop = QMessageBox()
            actionDesarrolladorPop.setWindowTitle(action)
            actionDesarrolladorPop.setText("ErtonDev")
            actionDesarrolladorPop.setIcon(QMessageBox.Information)
            actionDesarrolladorPop.setStandardButtons(QMessageBox.Close|QMessageBox.Ok)
            actionDesarrolladorPop.setDefaultButton(QMessageBox.Ok)
            actionDesarrolladorPop_exe = actionDesarrolladorPop.exec_()

    def goto_login(self):
        userInput = self.userText.text().lower()
        passInput = self.passText.text().lower()

        try:
            openAccount = io.open((client_path / f"../accounts/{userInput}.txt").resolve(), 'r')
            readAccount = openAccount.readlines()
            openAccount.close()
            if passInput + '\n' == readAccount[0] or passInput == readAccount[0]:
                # to remember who signed in:
                rememberUser = io.open((client_path / '../running_data/actual_client.txt').resolve(), 'w')
                rememberUser.write(str(userInput))
                rememberUser.close()

                ## OPENS MAIN WINDOW
                ############################################################
                # subprocess module allows secondary tasks
                subprocess.Popen(['python3', (client_path / '../main.py').resolve()]) # Opens main window
                sys.exit('login.py') # Closes

            else:
                loginPop = QMessageBox()
                loginPop.setWindowTitle("Error")
                loginPop.setText("Error al iniciar sesión.")
                loginPop.setIcon(QMessageBox.Warning)
                loginPop.setStandardButtons(QMessageBox.Close|QMessageBox.Ok)
                loginPop.setDefaultButton(QMessageBox.Ok)
                loginPop.setDetailedText("El nombre de usuario / contraseña es incorrecto.")
                loginPop_exe = loginPop.exec_()
        except FileNotFoundError:
            loginPop = QMessageBox()
            loginPop.setWindowTitle("Error")
            loginPop.setText("Error al iniciar sesión.")
            loginPop.setIcon(QMessageBox.Warning)
            loginPop.setStandardButtons(QMessageBox.Close|QMessageBox.Ok)
            loginPop.setDefaultButton(QMessageBox.Ok)
            loginPop.setDetailedText("El nombre de usuario / contraseña es incorrecto.")
            loginPop_exe = loginPop.exec_()

    def goto_register(self):
        userInput = self.userText.text().lower()
        passInput = self.passText.text().lower()

        if userInput == "" or passInput == "":
            registerPop = QMessageBox()
            registerPop.setWindowTitle("Error")
            registerPop.setText("Error al registrarse.")
            registerPop.setIcon(QMessageBox.Warning)
            registerPop.setStandardButtons(QMessageBox.Close|QMessageBox.Ok)
            registerPop.setDefaultButton(QMessageBox.Ok)
            registerPop.setDetailedText("Introduce tus credenciales.")
            registerPop_exe = registerPop.exec_()
        else:
            try:
                checkRepe = io.open((client_path / f"../accounts/{userInput}.txt").resolve(), 'r')
                checkRepe.close()
                registerPop = QMessageBox()
                registerPop.setWindowTitle("Error")
                registerPop.setText("Error al registrarse.")
                registerPop.setIcon(QMessageBox.Warning)
                registerPop.setStandardButtons(QMessageBox.Close|QMessageBox.Ok)
                registerPop.setDefaultButton(QMessageBox.Ok)
                registerPop.setDetailedText("Este nombre de ususario ya existe.")
                registerPop_exe = registerPop.exec_()
            except FileNotFoundError:
                # creates the account
                creaCuenta = io.open((client_path / f"../accounts/{userInput}.txt").resolve(), 'w')
                creaContra = passInput
                creaCuenta.write(creaContra)
                creaCuenta.close()

                # creates repositories for account's info
                creaRepositorio = os.makedirs(str((client_path / f"../accounts_data/{userInput}_info").resolve()), exist_ok = True)

                # creates files for account's info
                creaSafeBrazos = io.open((client_path / f"../accounts_data/{userInput}_info/safe_{userInput}_brazos.txt").resolve(), 'w')
                creaSafeBrazos.write("0")
                creaSafeBrazos.close()

                creaSafeEspalda = io.open((client_path / f"../accounts_data/{userInput}_info/safe_{userInput}_espalda.txt").resolve(), 'w')
                creaSafeEspalda.write("0")
                creaSafeEspalda.close()

                creaSafePectoral = io.open((client_path / f"../accounts_data/{userInput}_info/safe_{userInput}_pectoral.txt").resolve(), 'w')
                creaSafePectoral.write("0")
                creaSafePectoral.close()

                creaSafeAbdomen = io.open((client_path / f"../accounts_data/{userInput}_info/safe_{userInput}_abdomen.txt").resolve(), 'w')
                creaSafeAbdomen.write("0")
                creaSafeAbdomen.close()

                creaSafePiernas = io.open((client_path / f"../accounts_data/{userInput}_info/safe_{userInput}_piernas.txt").resolve(), 'w')
                creaSafePiernas.write("0")
                creaSafePiernas.close()

                creaSafeFlexibilidad = io.open((client_path / f"../accounts_data/{userInput}_info/safe_{userInput}_flexibilidad.txt").resolve(), 'w')
                creaSafeFlexibilidad.write("0")
                creaSafeFlexibilidad.close()

                creaSafeVelocidad = io.open((client_path / f"../accounts_data/{userInput}_info/safe_{userInput}_velocidad.txt").resolve(), 'w')
                creaSafeVelocidad.write("0")
                creaSafeVelocidad.close()

                creaSafeFuerza = io.open((client_path / f"../accounts_data/{userInput}_info/safe_{userInput}_fuerza.txt").resolve(), 'w')
                creaSafeFuerza.write("0")
                creaSafeFuerza.close()

                # prepares popup to notify client
                registerPop = QMessageBox()
                registerPop.setWindowTitle("Registro completo")
                registerPop.setText("¡Tu cuenta ha sido creada con éxito!")
                registerPop.setIcon(QMessageBox.Information)
                registerPop.setStandardButtons(QMessageBox.Close|QMessageBox.Ok)
                registerPop.setDefaultButton(QMessageBox.Ok)
                registerPop.setDetailedText(f"Nombre de usuario: {userInput}\nContraseña: {passInput}")
                registerPop_exe = registerPop.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

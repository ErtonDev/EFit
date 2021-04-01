# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_train.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

################################################################################
##
## EFIT - Fitness manager
## Secondary window, comes from main.py
## By ErtonDev
##
################################################################################

## MODULES
################################################################################
import io
from PySide2 import QtCore, QtGui, QtWidgets
from pathlib import Path

## SETUP
################################################################################
client_path = Path()

def cleanRunningData():
    # elimina los datos del último entrenamiento que se quería registrar para preparar el nuevo y que no interfiera
    open_running_data = io.open((client_path / "../running_data/preview_train.txt").resolve(), 'w')
    open_running_data.write("")
    open_running_data.close()

    # lo mismo para los archivos encargados de la suma de puntos de actividad
    open_running_abdomen = io.open((client_path / "../running_data/client_abdomen.txt").resolve(), 'w')
    open_running_abdomen.write("0")
    open_running_abdomen.close()

    open_running_brazos = io.open((client_path / "../running_data/client_brazos.txt").resolve(), 'w')
    open_running_brazos.write("0")
    open_running_brazos.close()

    open_running_espalda = io.open((client_path / "../running_data/client_espalda.txt").resolve(), 'w')
    open_running_espalda.write("0")
    open_running_espalda.close()

    open_running_flexibilidad = io.open((client_path / "../running_data/client_flexibilidad.txt").resolve(), 'w')
    open_running_flexibilidad.write("0")
    open_running_flexibilidad.close()

    open_running_fuerza = io.open((client_path / "../running_data/client_fuerza.txt").resolve(), 'w')
    open_running_fuerza.write("0")
    open_running_fuerza.close()

    open_running_pectoral = io.open((client_path / "../running_data/client_pectoral.txt").resolve(), 'w')
    open_running_pectoral.write("0")
    open_running_pectoral.close()

    open_running_piernas = io.open((client_path / "../running_data/client_piernas.txt").resolve(), 'w')
    open_running_piernas.write("0")
    open_running_piernas.close()

    open_running_velocidad = io.open((client_path / "../running_data/client_velocidad.txt").resolve(), 'w')
    open_running_velocidad.write("0")
    open_running_velocidad.close()

cleanRunningData()

## CLIENT
################################################################################
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 450)
        MainWindow.setMinimumSize(QtCore.QSize(550, 450))
        MainWindow.setMaximumSize(QtCore.QSize(550, 450))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(96, 186, 12))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(96, 186, 12))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(145, 145, 145))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        MainWindow.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(str((client_path / "../images/logo_efit_NEW.png").resolve())), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(10, 10, 531, 31))
        font = QtGui.QFont()
        font.setFamily("Garuda")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.subtitle = QtWidgets.QLabel(self.centralwidget)
        self.subtitle.setGeometry(QtCore.QRect(50, 40, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Gayathri")
        font.setPointSize(14)
        font.setItalic(False)
        self.subtitle.setFont(font)
        self.subtitle.setObjectName("subtitle")
        self.line1 = QtWidgets.QFrame(self.centralwidget)
        self.line1.setGeometry(QtCore.QRect(240, 50, 301, 20))
        self.line1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line1.setObjectName("line1")
        self.line2 = QtWidgets.QFrame(self.centralwidget)
        self.line2.setGeometry(QtCore.QRect(10, 50, 31, 20))
        self.line2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line2.setObjectName("line2")
        self.modalitySel = QtWidgets.QComboBox(self.centralwidget)
        self.modalitySel.setGeometry(QtCore.QRect(10, 80, 181, 25))
        self.modalitySel.setStyleSheet("QComboBox {\n"
"    selection-background-color: rgb(96, 186, 12);\n"
"}\n"
"QComboBox:hover {\n"
"    background-color: rgb(131, 191, 75);\n"
"}")
        self.modalitySel.setObjectName("modalitySel")
        self.modalitySel.addItem("", ["Flexiones cerradas", "Pesas", "Dominadas cerradas"])
        self.modalitySel.addItem("", ["Dominadas abiertas"])
        self.modalitySel.addItem("", ["Flexiones abiertas"])
        self.modalitySel.addItem("", ["Crunch", "V's", "Abdominales inferiores"])
        self.modalitySel.addItem("", ["Sentadillas", "Sentadillas con salto"])
        self.modalitySel.addItem("", ["Estiramientos", "Calentamiento", "Burpies"])
        self.typeSel = QtWidgets.QComboBox(self.centralwidget)
        self.typeSel.setGeometry(QtCore.QRect(200, 80, 181, 25))
        self.typeSel.setStyleSheet("QComboBox {\n"
"    selection-background-color: rgb(96, 186, 12);\n"
"}\n"
"QComboBox:hover {\n"
"    background-color: rgb(131, 191, 75);\n"
"}")
        self.typeSel.setObjectName("typeSel")
        self.cantSel = QtWidgets.QSpinBox(self.centralwidget)
        self.cantSel.setGeometry(QtCore.QRect(390, 80, 71, 26))
        self.cantSel.setObjectName("cantSel")
        self.cantSel.setMaximum(9999)
        self.explanation1 = QtWidgets.QLabel(self.centralwidget)
        self.explanation1.setGeometry(QtCore.QRect(10, 110, 181, 17))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(True)
        self.explanation1.setFont(font)
        self.explanation1.setObjectName("explanation1")
        self.explanation2 = QtWidgets.QLabel(self.centralwidget)
        self.explanation2.setGeometry(QtCore.QRect(200, 110, 181, 17))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(True)
        self.explanation2.setFont(font)
        self.explanation2.setObjectName("explanation2")
        self.explanation3 = QtWidgets.QLabel(self.centralwidget)
        self.explanation3.setGeometry(QtCore.QRect(390, 110, 151, 17))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(True)
        self.explanation3.setFont(font)
        self.explanation3.setObjectName("explanation3")
        self.line3 = QtWidgets.QFrame(self.centralwidget)
        self.line3.setGeometry(QtCore.QRect(10, 130, 531, 16))
        self.line3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line3.setObjectName("line3")
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(10, 140, 231, 141))
        self.image.setText("")
        self.image.setPixmap(QtGui.QPixmap(str((client_path / "../images/undraw_finish_line_katerina_limpitsouni_xy20.png").resolve())))
        self.image.setScaledContents(True)
        self.image.setObjectName("image")
        self.addBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addBtn.setGeometry(QtCore.QRect(470, 80, 71, 26))
        self.addBtn.setDefault(True)
        self.addBtn.setObjectName("addBtn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 150, 291, 287))
        self.label.setStyleSheet("QLabel {\n"
"    color: rgba(0, 0, 0, 0.5);\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0.011, stop:0 rgba(241, 241, 241, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-radius: 10px;\n"
"    padding-left: 5;\n"
"    padding-top: 5;\n"
"}\n"
"QLabel:hover {\n"
"    color: rgb(0, 0, 0)\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.mainBtn = QtWidgets.QPushButton(self.centralwidget)
        self.mainBtn.setGeometry(QtCore.QRect(10, 410, 231, 25))
        self.mainBtn.setDefault(True)
        self.mainBtn.setObjectName("mainBtn")
        self.cantSel_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.cantSel_2.setGeometry(QtCore.QRect(10, 310, 231, 26))
        self.cantSel_2.setObjectName("cantSel_2")
        self.cantSel_2.setMaximum(9999)
        self.cantSel_3 = QtWidgets.QSpinBox(self.centralwidget)
        self.cantSel_3.setGeometry(QtCore.QRect(10, 370, 231, 26))
        self.cantSel_3.setObjectName("cantSel_3")
        self.cantSel_3.setMaximum(9999)
        self.explanation1_2 = QtWidgets.QLabel(self.centralwidget)
        self.explanation1_2.setGeometry(QtCore.QRect(10, 290, 231, 17))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(True)
        self.explanation1_2.setFont(font)
        self.explanation1_2.setObjectName("explanation1_2")
        self.explanation1_4 = QtWidgets.QLabel(self.centralwidget)
        self.explanation1_4.setGeometry(QtCore.QRect(10, 350, 231, 17))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(True)
        self.explanation1_4.setFont(font)
        self.explanation1_4.setObjectName("explanation1_4")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 300, 231, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 360, 231, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        MainWindow.setCentralWidget(self.centralwidget)

        ## BACKEND
        ################################################################################
        self.retranslateUi(MainWindow)
        self.modalitySel.currentIndexChanged.connect(self.updateCombo)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.updateCombo(self.modalitySel.currentIndex())

        self.addBtn.clicked.connect(lambda: self.addExercise(str(self.modalitySel.currentText()), str(self.typeSel.currentText()), int(self.cantSel.value())))
        self.mainBtn.clicked.connect(self.registerTrain)

    # actualiza las comboboxes para mostrar los ejercicios de cada categoría.
    def updateCombo(self, index):
        self.typeSel.clear()
        exercise = self.modalitySel.itemData(index)
        if exercise:
            self.typeSel.addItems(exercise)

    # actualiza la preview del entrenamiento
    def updatePreview(self):
        read_preview = io.open((client_path / "../running_data/preview_train.txt").resolve(), 'r')
        preview = read_preview.read()

        # aplica cambios para mostrar la preview
        self.label.setText(preview)

    # añade un ejercicio al entrenamiento
    def addExercise(self, category = "", exercise = "", cant = 0):

        # comprueba que el cliente haya hecho un ejercicio mínimo, si no no hace nada
        if cant != 0:
            ## Aplica a la preview

            # write preview, primero mira si ya hay una linea escrita
            check_lines = io.open((client_path / "../running_data/preview_train.txt").resolve(), 'r')
            line_one = check_lines.readlines()
            check_lines.close()

            # ahora decide si se cambia de línea y la escribe
            try:
                if line_one[0] == "":
                    # no enter
                    write_preview = io.open((client_path / "../running_data/preview_train.txt").resolve(), 'a')
                    write_preview.write(f"{exercise}: {cant}")
                    write_preview.close()

                else:
                    # enter
                    write_preview = io.open((client_path / "../running_data/preview_train.txt").resolve(), 'a')
                    write_preview.write(f"\n{exercise}: {cant}")
                    write_preview.close()

            except IndexError:
                # no enter
                write_preview = io.open((client_path / "../running_data/preview_train.txt").resolve(), 'a')
                write_preview.write(f"{exercise}: {cant}")
                write_preview.close()

            # update preview
            self.updatePreview()

            ## Aplica a los puntos antes de sumarse del cliente
            try:
                # mira la cantidad actual, que al principio siempre será 0
                client_file = io.open((client_path / f"../running_data/client_{category.lower()}.txt").resolve(), 'r')
                actual_val = client_file.read()
                client_file.close()

                # haz la suma y aplica los cambios
                prepare_sum = io.open((client_path / f"../running_data/client_{category.lower()}.txt").resolve(), 'w')
                prepare_sum.write("")
                prepare_sum.write(int(actual_val) + cant)
                prepare_sum.close()

            except FileNotFoundError:
                # que significaría que el ejercicio del cliente está en la categoría Otros
                pass

    # registra el entrenamiento
    def registerTrain(self):
        pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Nuevo Entrenamiento"))
        self.title.setText(_translate("MainWindow", "¡Hora de registrar tu último entrenamiento!"))
        self.subtitle.setText(_translate("MainWindow", "¿Has sudado mucho?"))
        self.modalitySel.setItemText(0, _translate("MainWindow", "Brazos"))
        self.modalitySel.setItemText(1, _translate("MainWindow", "Espalda"))
        self.modalitySel.setItemText(2, _translate("MainWindow", "Pectoral"))
        self.modalitySel.setItemText(3, _translate("MainWindow", "Abdomen"))
        self.modalitySel.setItemText(4, _translate("MainWindow", "Piernas"))
        self.modalitySel.setItemText(5, _translate("MainWindow", "Otros"))
        self.explanation1.setText(_translate("MainWindow", "Categoría"))
        self.explanation2.setText(_translate("MainWindow", "Ejercicio"))
        self.explanation3.setText(_translate("MainWindow", "Cantidad o segundos"))
        self.addBtn.setText(_translate("MainWindow", "Añadir"))
        self.label.setText(_translate("MainWindow", "Añade un ejercicio a tu entrenamiento para previsualizarlo. Cierra esta ventana para cancelar el registro y que no se apliquen los cambios."))
        self.mainBtn.setText(_translate("MainWindow", "Registra tu entrenamiento"))
        self.explanation1_2.setText(_translate("MainWindow", "Tiempo de entrenamiento: minutos"))
        self.explanation1_4.setText(_translate("MainWindow", "Tiempo desde el último: días"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

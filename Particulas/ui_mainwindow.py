# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(273, 432)
        MainWindow.setStyleSheet(u"")
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.red = QSpinBox(self.centralwidget)
        self.red.setObjectName(u"red")
        self.red.setGeometry(QRect(92, 230, 131, 20))
        self.red.setMaximum(255)
        self.red.setValue(0)
        self.green = QSpinBox(self.centralwidget)
        self.green.setObjectName(u"green")
        self.green.setGeometry(QRect(92, 256, 131, 20))
        self.green.setMaximum(255)
        self.blue = QSpinBox(self.centralwidget)
        self.blue.setObjectName(u"blue")
        self.blue.setGeometry(QRect(92, 282, 131, 20))
        self.blue.setMaximum(255)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(70, 260, 16, 16))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(70, 280, 16, 16))
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(50, 10, 161, 21))
        self.label_9.setStyleSheet(u"font: 75 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 85, 0);\n"
"color: rgb(44, 124, 22);")
        self.label_9.setIndent(2)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 50, 186, 171))
        self.formLayout_2 = QFormLayout(self.widget)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.id = QLineEdit(self.widget)
        self.id.setObjectName(u"id")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.id)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label)

        self.origen_X1 = QLineEdit(self.widget)
        self.origen_X1.setObjectName(u"origen_X1")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.origen_X1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.origen_Y1 = QLineEdit(self.widget)
        self.origen_Y1.setObjectName(u"origen_Y1")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.origen_Y1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.destino_X2 = QLineEdit(self.widget)
        self.destino_X2.setObjectName(u"destino_X2")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.destino_X2)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_7)

        self.destino_Y2 = QLineEdit(self.widget)
        self.destino_Y2.setObjectName(u"destino_Y2")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.destino_Y2)

        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_10)

        self.velocidad = QLineEdit(self.widget)
        self.velocidad.setObjectName(u"velocidad")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.velocidad)

        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_11)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(70, 230, 16, 16))
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(40, 210, 51, 16))
        self.label_8.setStyleSheet(u"\n"
"font: 11pt \"MS Reference Sans Serif\";")
        self.inserta = QPushButton(self.centralwidget)
        self.inserta.setObjectName(u"inserta")
        self.inserta.setGeometry(QRect(80, 330, 111, 23))
        self.inserta.setStyleSheet(u"background-color: rgb(44, 124, 22);\n"
"color: rgb(255, 255, 255);")
        self.muestra = QPushButton(self.centralwidget)
        self.muestra.setObjectName(u"muestra")
        self.muestra.setGeometry(QRect(80, 360, 111, 23))
        self.muestra.setStyleSheet(u"background-color: rgb(44, 124, 22);\n"
"color: rgb(255, 255, 255);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 273, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Particulas", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"b", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"g", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Part\u00edculas</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Origen X", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Origen Y", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Destino X", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Destino Y", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Id", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"r", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Color", None))
        self.inserta.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.muestra.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi


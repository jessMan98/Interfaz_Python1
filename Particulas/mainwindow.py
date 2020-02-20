from PySide2.QtWidgets import QMainWindow, QFileDialog, QTableWidgetItem, QMessageBox
from ui_mainwindow import Ui_MainWindow
from PySide2.QtCore import Slot
import json
import math


class MainWindow(QMainWindow):
    # lista de Particulas
    particles = []
    dis = 0

    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.inserta.clicked.connect(self.add)
        self.ui.muestra.clicked.connect(self.shows)

        self.ui.actionAbrir.triggered.connect(self.abrir)
        self.ui.actionGuardar.triggered.connect(self.guardar)

        self.ui.mostrar.clicked.connect(self.muestra_tabla)
        self.ui.busca.clicked.connect(self.busqueda)

    def calculoEuclidiano(self, x_uno, y_uno, x_dos, y_dos):
        a = math.pow((x_dos - x_uno), 2)
        b = math.pow((y_dos - y_uno), 2)

        return math.sqrt(a + b)

    def clean(self):
        self.ui.id.clear()
        self.ui.origen_X1.clear()
        self.ui.origen_Y1.clear()
        self.ui.destino_X2.clear()
        self.ui.destino_Y2.clear()
        self.ui.velocidad.clear()
        self.ui.red.setValue(0)
        self.ui.green.setValue(0)
        self.ui.blue.setValue(0)

    @Slot()
    def busqueda(self):
        particula = []

        id = int(self.ui.busca_linea.text())

        for item in self.particles:
            if id == item['id']:
                particula.append(item)

        if len(particula) == 0:
            QMessageBox.information(self, "Particulas", "No se encontro la particula :(")
        else:
            self.particulas_tabla(particula)

    @Slot()
    def muestra_tabla(self):
        self.particulas_tabla(self.particles)

    def particulas_tabla(self, particulas):
        # limpiamos la tabla
        self.ui.tabla.clear()

        # cantidad de columnas que vamos a poner
        self.ui.tabla.setColumnCount(10)
        # numero de filas por tabla
        self.ui.tabla.setRowCount(len(particulas))

        # etiquetas para los headers de la tabla
        labels = ['ID', 'OrigenX', 'OrigenY', 'DestinoX', 'DestinoY', 'Velocidad', 'Red', 'Green', 'Blue','Distancia']
        self.ui.tabla.setHorizontalHeaderLabels(labels)


        # contador de filas
        row = 0
        for particula in particulas:
            id = QTableWidgetItem(str(particula['id']))
            origenX = QTableWidgetItem(str(particula['origen']['x']))
            origenY = QTableWidgetItem(str(particula['origen']['y']))
            destinoX = QTableWidgetItem(str(particula['destino']['x']))
            destinoY = QTableWidgetItem(str(particula['destino']['y']))
            velocidad = QTableWidgetItem(str(particula['velocidad']))
            r = QTableWidgetItem(str(particula['color']['red']))
            g = QTableWidgetItem(str(particula['color']['green']))
            b = QTableWidgetItem(str(particula['color']['blue']))
            self.dis = self.calculoEuclidiano(particula['origen']['x'], particula['origen']['y'], particula['destino']['x'], particula['destino']['y'])
            d = QTableWidgetItem(str(self.dis))

            self.ui.tabla.setItem(row, 0, id)
            self.ui.tabla.setItem(row, 1, origenX)
            self.ui.tabla.setItem(row, 2, origenY)
            self.ui.tabla.setItem(row, 3, destinoX)
            self.ui.tabla.setItem(row, 4, destinoY)
            self.ui.tabla.setItem(row, 5, velocidad)
            self.ui.tabla.setItem(row, 6, r)
            self.ui.tabla.setItem(row, 7, g)
            self.ui.tabla.setItem(row, 8, b)
            self.ui.tabla.setItem(row, 9, d)

            row += 1

    @Slot()
    def add(self):
        id = int(self.ui.id.text())
        oX = int(self.ui.origen_X1.text())
        oY = int(self.ui.origen_Y1.text())
        dX = int(self.ui.destino_X2.text())
        dY = int(self.ui.destino_Y2.text())
        velocity = int(self.ui.velocidad.text())
        r = int(self.ui.red.value())
        g = int(self.ui.green.value())
        b = int(self.ui.blue.value())

        # diccionario
        particulas = {
            "id": id,
            "origen": {
                "x": oX,
                "y": oY,
            },
            "destino": {
                "x": dX,
                "y": dY,
            },
            "velocidad": velocity,
            "color": {
                "red": r,
                "green": g,
                "blue": b
            }
        }

        self.particles.append(particulas)
        self.clean()

    @Slot()
    def shows(self):
        print(" ")

        for i in self.particles:
            print(i)
            self.dis = self.calculoEuclidiano(i['origen']['x'], i['origen']['y'], i['destino']['x'], i['destino']['y'])
            print(self.dis)

            #insertamos llave y valor en el plainText
            for x, v in i.items():
                self.ui.salidaDatos.insertPlainText(x + ":" + str(v) + "\n")

            self.ui.salidaDatos.insertPlainText("Distancia: " + str(self.dis) + '\n\n')

    @Slot()
    def abrir(self):
        ubicacion = QFileDialog.getOpenFileName(self, "Abrir Archivo", ".", "JSON(*.json)")

        # recuperar datos
        with open(ubicacion[0], 'r') as archivo:
            # carga el archivo a la lista
            self.particles = json.load(archivo)

    @Slot()
    def guardar(self):
        ubicacion = QFileDialog.getSaveFileName(self, "Guarda Particulas", ".", "JSON(*.json)")

        # creacion del archivo
        with open(ubicacion[0], 'w') as archivo:
            # vacia la informacion al archivo
            json.dump(self.particles, archivo, indent=5)

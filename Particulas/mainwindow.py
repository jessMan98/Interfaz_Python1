from PySide2.QtWidgets import QMainWindow, QFileDialog
from ui_mainwindow import Ui_MainWindow
from PySide2.QtCore import Slot
import json
import math


class MainWindow(QMainWindow):
    # lista de Particulas
    particles = []

    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.inserta.clicked.connect(self.add)
        self.ui.muestra.clicked.connect(self.shows)

        self.ui.actionAbrir.triggered.connect(self.abrir)
        self.ui.actionGuardar.triggered.connect(self.guardar)

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
            print("Distancia Euclidiana: ", self.calculoEuclidiano(i['origen']['x'], i['origen']['y'],
                                                                   i['destino']['x'], i['destino']['y']))

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

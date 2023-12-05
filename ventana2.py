import math
import sys

from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QLabel, QHBoxLayout, QApplication, QScrollArea, QWidget, QGridLayout, \
    QVBoxLayout, QButtonGroup, QPushButton

from cliente import Cliente
from ventana3 import Ventana3

from ventana4 import Ventana4


class Ventana2(QMainWindow):

    def __init__(self, parent=None):
        super(Ventana2, self).__init__(parent)




        #self.ventanaAnterior = anterior

        self.setWindowTitle("Usuarios registrados")

        # Poner el icono
        self.setWindowIcon(QIcon('imagenes/cliente.jpg'))

        # Establecemos ancho y alto
        self.ancho = 900
        self.alto = 600

        # Establecemos el tamaño de la ventana
        self.resize(self.ancho, self.alto)

        # Para que no se pueda mover el tamaño de la ventana
        # Se fija el ancho y el alto
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        # Imagen de fondo
        self.imagen = QLabel(self)
        self.imagenPantalla = QPixmap('imagenes/man.png')

        # Establecemos el modo para escalar la imagen
        self.imagen.setPixmap(self.imagenPantalla)
        self.imagen.setScaledContents(True)

        # El tamaño de la imagen se adapta al tamaño de su contenedor
        self.resize(self.imagen.width(), self.imagen.height())

        # Establecemos la ventana imagen como la ventana central
        self.setCentralWidget(self.imagen)

        # Establecemos un layout
        self.vertical = QVBoxLayout()

        self.letrero1 = QLabel()
        self.letrero1.setText("Usuarios registrados")
        self.letrero1.setFont(QFont("Andale Mono", 20))
        self.letrero1.setStyleSheet("color : blue;")

        self.vertical.addWidget(self.letrero1)

        self.vertical.addStretch()

        # creamos un scroll
        self.scrollArea = QScrollArea()

        # lo ponemos transparente
        self.scrollArea.setStyleSheet('background-color: transparent;')

        self.scrollArea.setWidgetResizable(True)

        # crea ventana contenedora para cada celda
        self.contenedora = QWidget()

        self.cuadricula = QGridLayout(self.contenedora)

        self.scrollArea.setWidget(self.contenedora)

        self.vertical.addWidget(self.scrollArea)

        # abrimos el archivo de lectura
        self.file = open('datos/clientes.txt', 'rb')

        # lista vacia para guardar usuarios
        self.usuarios = []

        contador = 0
        while self.file and contador < 10:
            # recorremos el archivo, linea por linea
            linea = self.file.readline().decode('UTF-8')
            print(linea)
            contador += 1

            lista = linea.split(';')
            if linea == '':
                break
            u = Cliente(
                lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[7], lista[8], lista[9],
                lista[10])

            self.usuarios.append(u)

        self.file.close()

        # tenemos la lista usuarios con todos los usuarios

        self.numeroUsuarios = len(self.usuarios)

        self.contador = 0

        # definimos la cantidad de elementos para mostrar por columna
        self.elementosPorColumna = 3

        # calculamos el # de filas
        self.numeroFilas = math.ceil(self.numeroUsuarios / self.elementosPorColumna) + 1

        # controlamos todos lo botones por variable
        self.botones = QButtonGroup()

        # definimos el controlador de botones
        # debe agrupar a todos lo botones internos
        self.botones.setExclusive(False)

        for fila in range(1, self.numeroFilas):
            for columna in range(self.elementosPorColumna + 1):

                # Validamos que se estan ingresando la cantidad de usuarios correcya:
                if self.contador < self.numeroUsuarios:
                    # en cada celda de la cuadricula de la ventana:
                    self.ventanaAuxiliar = QWidget()

                    # Se determina el alto y ancho:
                    self.ventanaAuxiliar.setFixedHeight(100)
                    self.ventanaAuxiliar.setFixedWidth(200)

                    # Creamos un layout vertical para cada elemento de la cuadricula
                    self.verticalCuadricula = QVBoxLayout()

                    # Creamos un boton por cada usuario mostrando la cédula:
                    self.botonAccion = QPushButton(self.usuarios[self.contador].documento)

                    # Establecemos el ancho del botón
                    self.botonAccion.setFixedWidth(150)
                    # Estilo del botón
                    self.botonAccion.setStyleSheet("background-color: #3164f4;"
                                                   "color: #FFFFFF;"
                                                   "padding: 10px;")
                    # Agregamos el layout al layout para que se vea
                    self.verticalCuadricula.addWidget(self.botonAccion)

                    # Agregamos el boton al grupo, su cédula como ID:
                    self.botones.addButton(self.botonAccion, int(self.usuarios[self.contador].documento))

                    # Agregamos un espacio en blanco
                    self.verticalCuadricula.addStretch()

                    # A la ventana le asignamos el layout vertical:
                    self.ventanaAuxiliar.setLayout(self.verticalCuadricula)

                    # A la ventana le asignamos el layout vertical:
                    self.cuadricula.addWidget(self.ventanaAuxiliar, fila, columna)

                    # Aumentamos el contador
                    self.contador += 1

        self.botones.idClicked.connect(self.metodo_accionBotones)

        # -------------------- BOTÓN TABULAR----------------------
        self.botonFormaTabular = QPushButton("Forma tabular")

        # Establecemos el ancho del botón
        self.botonFormaTabular.setFixedWidth(110)
        # Le ponemos estilos
        self.botonFormaTabular.setStyleSheet("background-color: #3164f4;"
                                             "color: #FFFFFF;"
                                             "padding: 10px;"
                                             "margin-top: 10px;")

        self.botonFormaTabular.clicked.connect(self.metodo_botonFormaTabular)

        # Agregaos el botón al layout
        self.vertical.addWidget(self.botonFormaTabular)

        # -------------------- BOTÓN VOLVER ----------------------
        self.botonVolver = QPushButton("Volver")

        # Establecemos el ancho del botón
        self.botonVolver.setFixedWidth(110)
        # Le ponemos estilos
        self.botonVolver.setStyleSheet("background-color: #3164f4;"
                                       "color: #FFFFFF;"
                                       "padding: 10px;"
                                       "margin-top: 10px;")

        self.botonVolver.clicked.connect(self.metodo_botonVolver)

        # Agregaos el botón al layout
        self.vertical.addWidget(self.botonVolver)

        # ------------------- PONER AL FINAL --------------------

        self.imagen.setLayout(self.vertical)

        # Metodo para controlar las acciones de los botones

    def metodo_accionBotones(self, cedulaUsuario):
        #print(cedulaUsuario)
        self.hide()
        self.ventana4 = Ventana4(self, cedulaUsuario)
        self.ventana4.show()


    def metodo_botonVolver(self):
        from ventana1 import Ventana1
        self.hide()
        self.ventana1 = Ventana1()
        self.ventana1.show()

    def metodo_botonFormaTabular(self):
        self.hide()
        self.ventana3 = Ventana3(self)
        self.ventana3.show()

        # Hacer que la aplicación se genere


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Crar un objeto de tipo Ventana1 con el nombre ventana 1
    ventana2 = Ventana2()

    # Hacer que el objeto se muestre
    ventana2.show()

    sys.exit(app.exec_())
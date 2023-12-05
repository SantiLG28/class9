import sys

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QVBoxLayout, QScrollArea, QWidget, QGridLayout, \
    QTableWidget, QTableWidgetItem, QPushButton, QApplication
from PyQt5 import QtGui

from cliente import Cliente
# from ventana2 import Ventana2


class Ventana3(QMainWindow):

    def __init__(self, parent=None):
        super(Ventana3, self).__init__(parent)

        # Creamos un atributo que guarde la ventana anterior
        #self.ventanaAnterior = anterior

        # poner el titulo
        self.setWindowTitle("Usuarios Registrados")

        # Ponemos el icono
        self.setWindowIcon(QtGui.QIcon('imagenes/cliente.jpg'))

        # Establecemos las propiedades de ancho por alto
        self.ancho = 900
        self.alto = 600

        # Establecemos el tamaño de la venata
        self.resize(self.ancho, self.alto)

        # Centrar la ventana en la pantalla
        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        # Fijar el tamaño de la ventana para evitar cambiarlo
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        # Establecemos el fondo principal
        self.fondo = QLabel(self)

        # Definimos la imagen de fondo
        self.imagenFondo = QPixmap('imagenes/empresa.jpg')

        # Definimos la iamgen de fondo
        self.fondo.setPixmap(self.imagenFondo)

        # Establecemos el modo para escalar la imagen
        self.fondo.setScaledContents(True)

        # Hacemos que se adapte al tamaño de la imagen
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        # Establecemos la ventana de fondo como ventana central
        self.setCentralWidget(self.fondo)



        # Abrimos el archivo en modo de lectura
        self.file = open('datos/clientes.txt', 'rb')

        # Lista vacia para guardar los usuarios
        self.usuarios = []

        # Recorremos el archivo, linea por linea
        while self.file:
            linea = self.file.readline().decode('UTF-8')
            # Obtenemos del string una lista con 11 datos separados por :
            lista = linea.split(";")
            # Se para si ya no hay msa registros en el archivo
            if linea == '':
                break
            # Creamos un objeto de tipo cliente llamado u
            u = Cliente(
                lista[0],
                lista[1],
                lista[2],
                lista[3],
                lista[4],
                lista[5],
                lista[6],
                lista[7],
                lista[8],
                lista[9],
                lista[10],
            )
            # Metemos el objeto en la lista de usuario:
            self.usuarios.append(u)

        # Cerramos el archivo
        self.file.close()

        # En este punto tenemos la lista usuarios con los usuarios

        # Obtenemos el numero de usuarios registrados
        # Consultamos el tamaño de la lista usuarios
        self.numeroUsuarios = len(self.usuarios)

        # Contador de elementos para controlar a los usuarios en la tabla
        self.contador = 0



        # Establecemos la distribucion de los elementos en layout vertical
        self.vertical = QVBoxLayout()

        # Hacemos el letrero
        self.letrero1 = QLabel()

        # Le escribimos el texto
        self.letrero1.setText("Usuarios Registrados")

        # Le asignamos el tipo de letra
        self.letrero1.setFont(QFont("Andale Mono", 20))

        # Le asignamos color de texto
        self.letrero1.setStyleSheet("color: #000080;")

        # Agregamos el letrero en la primera fila
        self.vertical.addWidget(self.letrero1)


        # Ponemos un espacio despues
        self.vertical.addStretch()



        # Creamos un scroll
        self.scrollArea = QScrollArea()

        # Hacemos que el scroll se adapte a diferentes tamaños
        self.scrollArea.setWidgetResizable(True)



        # Creamos una tabla
        self.tabla = QTableWidget()

        # Definimos numero de columnas que tendra la tabla
        self.tabla.setColumnCount(11)

        # Definimos el ancho de cada columna
        self.tabla.setColumnWidth(0,150)
        self.tabla.setColumnWidth(1, 150)
        self.tabla.setColumnWidth(2, 150)
        self.tabla.setColumnWidth(3, 150)
        self.tabla.setColumnWidth(4, 150)
        self.tabla.setColumnWidth(5, 150)
        self.tabla.setColumnWidth(6, 150)
        self.tabla.setColumnWidth(7, 150)
        self.tabla.setColumnWidth(8, 150)
        self.tabla.setColumnWidth(9, 150)
        self.tabla.setColumnWidth(10, 150)

        # Definimos el texto de la cabecera
        self.tabla.setHorizontalHeaderLabels(['Nombre',
                                              'Usuario',
                                              'Password',
                                              'Documento',
                                              'Correo',
                                              'Pregunta 1',
                                              'Respuesta 1',
                                              'Pregunta 2',
                                              'Respuesta 2',
                                              'Pregunta 3',
                                              'Respuesta 3'])

        # Establecemos el numero de filas
        self.tabla.setRowCount(self.numeroUsuarios)

        # Llenamos la tabla
        for u in self.usuarios:
            self.tabla.setItem(self.contador,0, QTableWidgetItem(u.nombreCompleto))
            self.tabla.setItem(self.contador, 1, QTableWidgetItem(u.usuario))
            self.tabla.setItem(self.contador, 2, QTableWidgetItem(u.password))
            self.tabla.setItem(self.contador, 3, QTableWidgetItem(u.documento))
            self.tabla.setItem(self.contador, 4, QTableWidgetItem(u.correo))
            self.tabla.setItem(self.contador, 5, QTableWidgetItem(u.pregunta1))
            self.tabla.setItem(self.contador, 6, QTableWidgetItem(u.respuesta1))
            self.tabla.setItem(self.contador, 7, QTableWidgetItem(u.pregunta2))
            self.tabla.setItem(self.contador, 8, QTableWidgetItem(u.respuesta2))
            self.tabla.setItem(self.contador, 9, QTableWidgetItem(u.pregunta3))
            self.tabla.setItem(self.contador, 10, QTableWidgetItem(u.respuesta3))
            self.contador += 1




        # Metemos la tabla en el scroll
        self.scrollArea.setWidget(self.tabla)

        # Metemos en el layout vertical el scroll
        self.vertical.addWidget(self.scrollArea)

        # Ponemos un espacio despues
        self.vertical.addStretch()



        # BOTON VOLVER
        # Hacemos el boton para devolver a la ventana anterior
        self.botonVolver = QPushButton("Volver")

        # Establecemos el ancho del boton
        self.botonVolver.setFixedWidth(90)

        # Le ponemos los estilos
        self.botonVolver.setStyleSheet("background-color: #3164f4;"
                                       "color: #FFFFFF;"
                                       "padding: 10px;"
                                       "margin-top: 10px;")

        self.botonVolver.clicked.connect(self.metodo_botonVolver)

        # Agregamos el boton botonContnuar al layout ladoDerecho
        self.vertical.addWidget(self.botonVolver)



        # --- OJO IMPORTANTE PONER AL FINAL ---

        # indicamos que el layout principal del fondo es horizontal
        self.fondo.setLayout(self.vertical)



    def metodo_botonVolver(self):
        from ventana2 import Ventana2
        self.hide()
        self.ventana2 = Ventana2()
        self.ventana2.show()



if __name__ == '__main__':
    # Hacemos que la aplicacion de genere
    app = QApplication(sys.argv)


    # Crear un objeto de tipo Ventana1 con el nombre ventana1
    ventana3 = Ventana3()

    # Hacemos que el objeto ventana 1 se vea
    ventana3.show()

    # codigo para terminar la aplicación
    sys.exit(app.exec_())


import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QLabel, QHBoxLayout, QFormLayout, QLineEdit, QApplication, QPushButton, \
    QDialog, QDialogButtonBox, QVBoxLayout
from PyQt5 import QtGui , QtCore

from cliente import Cliente


class Ventana4(QMainWindow):

    def __init__(self, anterior, cedula):
        super(Ventana4, self).__init__(None)

        self.ventanaAnterior = anterior

        self.cedulaUsuario = cedula

        self.setWindowTitle("Editar usuario")

        # Poner el icono
        self.setWindowIcon(QtGui.QIcon("imagenes\mochila.png"))

        # Establecemos ancho y alto
        self.ancho = 900
        self.alto = 600

        # Establecemos el tamaño de la ventana
        self.resize(self.ancho, self.alto)

        # Para que no se pueda mover el tamaño de la ventana
        # Se fija el ancho y el alto
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        #  de fondo
        self.fondo = QLabel(self)

        self.fondo.setStyleSheet("background-color: #FFFFFF;")

        self.setCentralWidget(self.fondo)

        self.horizontal = QHBoxLayout()

        # Establecemos las margenes
        self.horizontal.setContentsMargins(30, 30, 30, 30)

        # ------------------- Layout izquierda --------------------

        self.ladoIzquierdo = QFormLayout()

        self.letrero1 = QLabel()
        self.letrero1.setText("Editar: Información cliente")
        self.letrero1.setFont(QFont("Andale Mono", 18))
        self.letrero1.setStyleSheet("color: #FFFFFF;" "background-color: #6C8CE5;")

        self.ladoIzquierdo.addRow(self.letrero1)

        self.letrero2 = QLabel()
        self.letrero2.setFixedWidth(340)
        self.letrero2.setText(
            "Por favor ingrese la información del cliente"
            "\nen el formulario de abajo. Los campos marcados"
            "\ncon asteriscos son obligatorios."
        )
        self.letrero2.setFont(QFont("Andale Mono", 9))
        self.letrero2.setStyleSheet(
             "color: white;"
            "background-color: #6C8CE5;"
            "margin-bottom: 2px;"
            "margin-top: 2px;"
            "padding-bottom: 5px;"  # Ajusta el valor según tus necesidades
            "border: 2px solid #FFFFFF;"
            "border-left: none;"
            "border-right: none;"
            "border-top: none;")

        self.ladoIzquierdo.addRow(self.letrero2)

        self.nombreCompleto = QLineEdit()
        self.nombreCompleto.setFixedWidth(250)

        self.ladoIzquierdo.addRow("Nombre Completo*",self.nombreCompleto)

        self.usuario = QLineEdit()
        self.usuario.setFixedWidth(250)

        self.ladoIzquierdo.addRow("Usuario*", self.usuario)

        self.password = QLineEdit()
        self.password.setFixedWidth(250)
        # para que no deje ver la contraseña
        self.password.setEchoMode(QLineEdit.Password)
        self.ladoIzquierdo.addRow("Password*", self.password)

        self.password2 = QLineEdit()
        self.password2.setFixedWidth(250)
        # para que no deje ver la contraseña
        self.password2.setEchoMode(QLineEdit.Password)
        self.ladoIzquierdo.addRow("Password*", self.password2)

        self.documento = QLineEdit()
        self.documento.setFixedWidth(250)
        self.ladoIzquierdo.addRow("Documento*", self.documento)

        self.correo = QLineEdit()
        self.correo.setFixedWidth(250)
        self.ladoIzquierdo.addRow("Correo*", self.correo)

        # boton editar
        self.botonEditar = QPushButton("Editar")
        self.botonEditar.setFixedWidth(90)
        self.botonEditar.setStyleSheet("background-color:#3164f4;"
                                          "color:  white;"
                                          "padding: 10px;"
                                          "margin-top: 40px;")

        self.botonEditar.clicked.connect(self.accion_botonEditar)

        # boton limpiar
        self.BotonLimpiar = QPushButton("Limpiar")
        self.BotonLimpiar.setFixedWidth(90)
        self.BotonLimpiar.setStyleSheet("background-color: #3164f4;"
                                        "color: #FFFFFF;"
                                        "padding: 10px;"
                                        "margin-top: 40px;")
        self.BotonLimpiar.clicked.connect(self.accion_BotonLimpiar)

        self.ladoIzquierdo.addRow(self.botonEditar, self.BotonLimpiar)

        # boton eliminar
        self.botonEliminar = QPushButton("Eliminar")
        self.botonEliminar.setFixedWidth(90)
        self.botonEliminar.setStyleSheet("background-color: #3164f4;"
                                        "color: #FFFFFF;"
                                        "padding: 10px;"
                                        "margin-top: 40px;")
        self.botonEliminar.clicked.connect(self.accion_botonEliminar)

        self.ladoIzquierdo.addRow(self.botonEliminar)

        # boton volver
        self.botonVolver = QPushButton("Volver")
        self.botonVolver.setFixedWidth(90)
        self.botonVolver.setStyleSheet("background-color: #3164f4;"
                                         "color: #FFFFFF;"
                                         "padding: 10px;"
                                         "margin-top: 40px;")
        self.botonVolver.clicked.connect(self.accion_botonVolver)

        self.ladoIzquierdo.addRow(self.botonVolver)

        #Agregamos el layout lado IZQ al layout horizontal
        self.horizontal.addLayout(self.ladoIzquierdo)

        # ------------------- Layout Derecho --------------------
        # creamos el layout derecho
        self.ladoDerecho = QFormLayout()

        # asigna margen
        self.ladoDerecho.setContentsMargins(20, 0, 0, 0)

        # hacemos letrero
        self.letrero3 = QLabel()
        self.letrero3.setText("Editar: Recuperar contraseña")
        self.letrero3.setFont(QFont("Andale Mono", 18))
        self.letrero3.setStyleSheet("color: #FFFFFF;" "background-color: #6C8CE5;")

        self.ladoDerecho.addRow(self.letrero3)

        # hacemos letrero
        self.letrero4 = QLabel()

        self.letrero4.setFixedWidth(360)

        self.letrero4.setText('Por favor ingrese la informacion para recuperar'
                              '\nla contraseña. Los campos marcados con asteriscos'
                              '\nson obligatorios.')

        self.letrero4.setFont(QFont("Andale Mono", 9))

        self.letrero4.setStyleSheet(
             "color: white;"
            "background-color: #6C8CE5;"
            "margin-bottom: 2px;"
            "margin-top: 2px;"
            "padding-bottom: 5px;"  
            "border: 2px solid #FFFFFF;"
            "border-left: none;"
            "border-right: none;"
            "border-top: none;")

        # agregamos el letrero
        self.ladoDerecho.addRow(self.letrero4)

        # ----1

        # hacemos la pregunta 1
        self.labelPregunta1 = QLabel('Pregunta de verificacion 1*')

        # agregamos
        self.ladoDerecho.addRow(self.labelPregunta1)

        # hacemos el campo para responder
        self.pregunta1 = QLineEdit()
        self.pregunta1.setFixedWidth(320)

        # agregamos el letrero
        self.ladoDerecho.addRow(self.pregunta1)

        # hacemos el de respuesta
        self.labelRespuesta1 = QLabel('Respuesta de verificacion 1*')

        # agregamos el letrero
        self.ladoDerecho.addRow(self.labelRespuesta1)

        # hacemos el campo para responder
        self.respuesta1 = QLineEdit()
        self.respuesta1.setFixedWidth(320)

        # agregamos el letrero
        self.ladoDerecho.addRow(self.respuesta1)

        # ----2

        # hacemos la pregunta \2
        self.labelPregunta2 = QLabel('Pregunta de verificacion 2*')

        # agregamos
        self.ladoDerecho.addRow(self.labelPregunta2)

        # hacemos el campo para responder
        self.pregunta2 = QLineEdit()
        self.pregunta2.setFixedWidth(320)

        # agregamos el letrero
        self.ladoDerecho.addRow(self.pregunta2)

        # hacemos el de respuesta
        self.labelRespuesta2 = QLabel('Respuesta de verificacion 2*')

        # agregamos el letrero
        self.ladoDerecho.addRow(self.labelRespuesta2)

        # hacemos el campo para responder
        self.respuesta2 = QLineEdit()
        self.respuesta2.setFixedWidth(320)

        # agregamos el letrero
        self.ladoDerecho.addRow(self.respuesta2)

        # ----3

        # hacemos la pregunta 3
        self.labelPregunta3 = QLabel('Pregunta de verificacion 3*')

        # agregamos
        self.ladoDerecho.addRow(self.labelPregunta3)

        # hacemos el campo para responder
        self.pregunta3 = QLineEdit()
        self.pregunta3.setFixedWidth(320)

        # agregamos el letrero
        self.ladoDerecho.addRow(self.pregunta3)

        # hacemos el de respuesta
        self.labelRespuesta3 = QLabel('Respuesta de verificacion 3*')

        # agregamos el letrero
        self.ladoDerecho.addRow(self.labelRespuesta3)

        # hacemos el campo para responder
        self.respuesta3 = QLineEdit()
        self.respuesta3.setFixedWidth(320)

        # agregamos el letrero
        self.ladoDerecho.addRow(self.respuesta3)



        # agregamos el layout ladoderecho al layout horizontal
        self.horizontal.addLayout(self.ladoDerecho)

        # ------------------- PONER AL FINAL --------------------

        self.fondo.setLayout(self.horizontal)

        # ------------CONSTRUCTOR DE LA VENTANA EMERGENTE-----------

        self.ventanaDialogo = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)

        self.ventanaDialogo.resize(300, 150)
        self.botonAceptar = QDialogButtonBox.Ok
        self.opciones = QDialogButtonBox(self.botonAceptar)
        self.opciones.accepted.connect(self.ventanaDialogo.accept)

        self.ventanaDialogo.setWindowModality(Qt.ApplicationModal)

        self.vertical = QVBoxLayout()

        self.mensaje = QLabel('')
        self.mensaje.setStyleSheet("color: #FFFFFF;" "background-color: #3164f4;")
        self.vertical.addWidget(self.mensaje)
        self.vertical.addWidget(self.opciones)

        self.ventanaDialogo.setLayout(self.vertical)

        self.cargar_datos()


    def accion_botonEditar(self):
        self.datosCorrectos =  True

        self.ventanaDialogo.setWindowTitle("Formulario de edición")

        if(
            self.password.text() != self.password2.text()):
            self.datosCorrectos = False

            self.mensaje.setText("Los passwords no son iguales")

            self.ventanaDialogo.exec_()

        if (
                self.nombreCompleto.text() == ''
                or self.usuario.text() == ''
                or self.password.text() == ''
                or self.password2.text() == ''
                or self.documento.text() == ''
                or self.correo.text() == ''
                or self.pregunta1.text() == ''
                or self.respuesta1.text() == ''
                or self.pregunta2.text() == ''
                or self.respuesta2.text() == ''
                or self.pregunta3.text() == ''
                or self.respuesta3.text() == ''
        ):
            self.datosCorrectos = False

            self.mensaje.setText('Debe seccionar un usuario con documento valido')

            self.ventanaDialogo.exec_()

            self.metodo_botonVolver()

        if  self.datosCorrectos:
            self.file = open('datos/clientes.txt', 'rb')
            usuarios = []

            while self.file:
                linea = self.file.readline().decode('UTF-8')

                lista = linea.split(';')
                if linea == '':
                    break

                u = Cliente(
                    lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[7], lista[8], lista[9],
                    lista[10])

                usuarios.append(u)

            self.file.close()

            # Variable para controlar que existe el documento
            existeDocumento = False

            # buscamos en la lista por usuario si existe cc
            # es la cc de la venta anterior
            for u in usuarios:
                # comparamos el documento
                if int(u.documento) == self.cedulaUsuario:
                    u.usuario=self.usuario.text()
                    u.password=self.password.text()
                    u.correo=self.correo.text()
                    u.pregunta1=self.pregunta1.text()
                    u.respuesta1=self.respuesta1.text()
                    u.pregunta2=self.pregunta2.text()
                    u.respuesta2=self.respuesta2.text()
                    u.pregunta3=self.pregunta3.text()
                    u.respuesta3=self.respuesta3.text()

                    existeDocumento = True

                    break

            if (not existeDocumento
            ):
                self.mensaje.setText("No existe un usuario con este documento:\n"
                                     + str(self.cedulaUsuario))

                self.ventanaDialogo.exec_()

            self.file = open('datos/clientes.txt', 'wb')

            for u in usuarios:
                self.file.write(bytes(u.nombreCompleto+ ';'
                                      + u.usuario+ ';'
                                      + u.password + ';'
                                      + u.documento + ';'
                                      + u.correo+ ';'
                                      + u.pregunta1 + ';'
                                      + u.respuesta1 + ';'
                                      + u.pregunta2+ ';'
                                      + u.respuesta2+ ';'
                                      + u.pregunta3+ ';'
                                      + u.respuesta3, encoding='UTF-8'))

            self.file.close()

            if(existeDocumento):
                self.mensaje.setText("Usuario se actualizo correctamente")
                self.ventanaDialogo.exec_()
                self.accion_BotonLimpiar()
                self.accion_botonVolver()

            self.file = open('datos/clientes.txt', 'rb')
            while self.file:
                linea = self.file.readline().decode('UTF-8')
                print(linea)
                if linea == '':
                    break
            self.file.close()


    def accion_BotonLimpiar(self):
        self.nombreCompleto.setText('')
        self.usuario.setText('')
        self.password.setText('')
        self.password2.setText('')
        self.documento.setText('')
        self.correo.setText('')
        self.pregunta1.setText('')
        self.respuesta1.setText('')
        self.pregunta2.setText('')
        self.respuesta2.setText('')
        self.pregunta3.setText('')
        self.respuesta3.setText('')


    def accion_botonEliminar(self):

        self.datosCorrectos = True

        self.eliminar = False

        if (
                self.nombreCompleto.text() == ''
                or self.usuario.text() == ''
                or self.password.text() == ''
                or self.password2.text() == ''
                or self.documento.text() == ''
                or self.correo.text() == ''
                or self.pregunta1.text() == ''
                or self.respuesta1.text() == ''
                or self.pregunta2.text() == ''
                or self.respuesta2.text() == ''
                or self.pregunta3.text() == ''
                or self.respuesta3.text() == ''
        ):
            self.datosCorrectos = False

            self.mensaje.setText('Debe seccionar un usuario con documento valido')

            self.ventanaDialogo.exec_()

            self.accion_botonVolver()

        if self.datosCorrectos:


            self.ventanaDialogoEliminar = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)

            self.ventanaDialogoEliminar.resize(300, 150)

            self.ventanaDialogoEliminar.setWindowModality(Qt.ApplicationModal)

            self.verticalEliminar = QVBoxLayout()

            self.mensajeEliminar = QLabel('Esta seguro quedesea eliminar este registro?')
            self.mensaje.setStyleSheet("color: #FFFFFF;" "background-color: #3164f4;")
            self.verticalEliminar.addWidget(self.mensajeEliminar)

            self.opcionesEliminar = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
            self.opcionesBox = QDialogButtonBox(self.opcionesEliminar)

            self.opcionesBox.accepted.connect(self.ok_opcion)
            self.opcionesBox.rejected.connect(self.cancel_opcion)

            self.verticalEliminar.addWidget(self.opcionesBox)

            self.ventanaDialogoEliminar.setLayout(self.verticalEliminar)

            self.ventanaDialogoEliminar.exec_()

        if self.eliminar:
            self.file = open("datos/clientes.txt", "rb")

            usuarios = []

            while self.file:
                linea = self.file.readline().decode('UTF-8')

                lista = linea.split(';')
                if linea == '':
                    break

                u = Cliente(
                    lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[7], lista[8], lista[9],
                    lista[10])

                usuarios.append(u)

            self.file.close()

            existeDocumento = False

            for u in usuarios:

                if int(u.documento) == self.cedulaUsuario:
                    usuarios.remove(u)
                    existeDocumento = True
                    break

            self.file = open('datos/clientes.txt', 'wb')

            for u in usuarios:
                self.file.write(bytes(u.nombreCompleto + ';'
                                      + u.usuario + ';'
                                      + u.password + ';'
                                      + u.documento + ';'
                                      + u.correo + ';'
                                      + u.pregunta1 + ';'
                                      + u.respuesta1 + ';'
                                      + u.pregunta2 + ';'
                                      + u.respuesta2 + ';'
                                      + u.pregunta3 + ';'
                                      + u.respuesta3, encoding='UTF-8'))

            self.file.close()

            if(existeDocumento):
                self.mensaje.setText("Usuario eliminado correctamente")
                self.ventanaDialogo.exec_()
                self.accion_BotonLimpiar()
                self.accion_botonVolver()

    def ok_opcion(self):
        self.ventanaDialogoEliminar.close()
        self.eliminar = True

    def cancel_opcion(self):
        self.ventanaDialogoEliminar.close()

    def accion_botonVolver(self):
        self.hide()
        self.ventanaAnterior.show()

    def cargar_datos(self):

        self.file = open("datos/clientes.txt","rb")

        usuarios = []

        while self.file:
            linea = self.file.readline().decode('UTF-8')

            lista = linea.split(';')
            if linea == '':
                break

            u = Cliente(
                lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[7], lista[8], lista[9],
                lista[10])

            usuarios.append(u)

        self.file.close()

        # Variable para controlar que existe el documento
        existeDocumento = False

        # buscamos en la lista por usuario si existe cc
        # es la cc de la venta anterior
        for u in usuarios:
    # comparamos el documento
            if int(u.documento) == self.cedulaUsuario:
                self.nombreCompleto.setText(u.nombreCompleto)
                self.nombreCompleto.setReadOnly(True)
                self.usuario.setText(u.usuario)
                self.password.setText(u.password)
                self.password2.setText(u.password)
                self.documento.setText(u.documento)
                self.documento.setReadOnly(True)
                self.correo.setText(u.correo)
                self.pregunta1.setText(u.pregunta1)
                self.respuesta1.setText(u.respuesta1)
                self.pregunta2.setText(u.pregunta2)
                self.respuesta2.setText(u.respuesta2)
                self.pregunta3.setText(u.pregunta3)
                self.respuesta3.setText(u.respuesta3)

                existeDocumento = True

                break

        if (not existeDocumento
        ):
            self.mensaje.setText("No existe un usuario con este documento:\n"
                                 + str(self.cedulaUsuario))

            self.ventanaDialogo.exec_()

            self.metodo_botonVolver()



if __name__ == "__main__":    # Hacer que la aplicación se genere
    app = QApplication(sys.argv)

    # Crar un objeto de tipo Ventana1 con el nombre ventana 1
    ventana4 = Ventana4()

    # Hacer que el objeto se muestre
    ventana4.show()

    sys.exit(app.exec_())
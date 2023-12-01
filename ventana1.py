import sys

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QApplication, QFormLayout, QLineEdit, \
    QPushButton, QDialog, QDialogButtonBox, QVBoxLayout
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from cliente import Cliente

class Ventana1(QMainWindow):

    # Hacer el metodo de construccion de la ventana:
    def __init__(self,parent=None):
        super(Ventana1,self).__init__(parent)

        # Poner el titulo:
        self.setWindowTitle("Formulario de registro")

        # Poner el icono:
        self.setWindowIcon(QtGui.QIcon('imagenes/4.png'))

        # Estableciendo las propiedades de ancho y alto:
        self.ancho = 1000
        self.alto = 850

        # Establecer el tamaño de la ventana:
        self.resize(self.ancho, self.alto)

        # Hacer que la ventana se vea en el centro:
        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        # Fijar el ancho y el alto de la ventana:
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        # Establecemos el fondo principal:
        self.fondo = QLabel(self)

        # Definimos la imagen de fondo
        self.imagenFondo = QPixmap('imagenes/2.png')

        # Definimos la imagen de fondo:
        self.fondo.setPixmap(self.imagenFondo)

        # Establecemos el modo para escalar la imagen:
        self.fondo.setScaledContents(True)

        # hacemos que se adapte el tamaño de la imagen:
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        # Establecemos la ventana de fondo como la ventana central
        self.setCentralWidget(self.fondo)

        # Establecemos la dsitribucion de los elementos en layout horizontal:
        self.horizontal = QHBoxLayout()
        # Le ponemos las margenes:
        self.horizontal.setContentsMargins(30,30,30,30)

        #----------------Layout Izquierdo--------------

        #creamos el layout del lado izquierdo:
        self.ladoIzquierdo = QFormLayout()

        # Hacemos el letrero:
        self.letrero1 = QLabel()

        # Le escribimos el texto:
        self.letrero1.setText("Informaciòn del cliente")

        # Le asignamos el tipo de letra:
        self.letrero1.setFont(QFont("Andale Mono", 20))

        # Le ponemos color de texto y margenes:
        self.letrero1.setStyleSheet("color: #000000;")

        # Agregamos el letrero en la primera fila:
        self.ladoIzquierdo.addRow(self.letrero1)

        # Hacemos el letrero:
        self.letrero2 = QLabel()

        # Establecemos el ancho del label:
        self.letrero2.setFixedWidth(340)

        # Le escribimos el texto:
        self.letrero2.setText("Por favor ingrese la informaciòn del "
                              "\ncliente en el formulario de abajo. "
                              "\nLos campos marcados con "
                              "\nasterisco son obligatorios.")

        # Le asignamos el tipo de letra:
        self.letrero2.setFont(QFont("Andale Mono", 10))

        # Le ponemos color de texto y margenes:
        self.letrero2.setStyleSheet("color: #000000; margin-bottom: 40px;"
                                    "margin-top: 20px;"
                                    "padding-bottom: 10px;"
                                    "border: 2px solid #000000;"
                                    "border-left: none;"
                                    "border_right: none;"
                                    "border-top: none;")

        # Agregamos el letrero en la fila siguiente:
        self.ladoIzquierdo.addRow(self.letrero2)

        # Hacemos el campo para ingresar el nombre:
        self.nombreCompleto = QLineEdit()
        self.nombreCompleto.setFixedWidth(250)

        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Nombre Completo*",self.nombreCompleto)

        # Hacemos el campo para ingresar el usuario:
        self.usuario = QLineEdit()
        self.usuario.setFixedWidth(250)

        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Usuario*", self.usuario)

        # Hacemos el campo para ingresar el password:
        self.password = QLineEdit()
        self.password.setFixedWidth(250)
        self.password.setEchoMode(QLineEdit.Password)

        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Password🔒*", self.password)

        # Hacemos el campo para ingresar el password:
        self.password2 = QLineEdit()
        self.password2.setFixedWidth(250)
        self.password2.setEchoMode(QLineEdit.Password)

        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Password🔒*", self.password2)

        # Hacemos el campo para ingresar el documento:
        self.documento = QLineEdit()
        self.documento.setFixedWidth(250)

        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Documento*", self.documento)

        # Hacemos el campo para ingresar el correo:
        self.correo = QLineEdit()
        self.correo.setFixedWidth(250)

        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Correo*", self.correo)

        # Hacemos el botòn para registrar los datos:
        self.botonRegistrar = QPushButton("Registrar")

        # Establecemos el ancho del botòn:
        self.botonRegistrar.setFixedWidth(90)

        # Le ponemos los estilos:
        self.botonRegistrar.setStyleSheet("background-color: #008B45;"
                                          "color: #FFFFFF;"
                                          "padding: 10px;"
                                          "margin-top: 40px;")

        self.botonRegistrar.clicked.connect(self.accion_botonRegistrar)

        # Hacemos el botòn para limpiar los datos:
        self.botonLimpiar = QPushButton("Limpiar")

        # Establecemos el ancho del botòn:
        self.botonLimpiar.setFixedWidth(90)

        # Le ponemos los estilos:
        self.botonLimpiar.setStyleSheet("background-color: #008B45;"
                                          "color: #FFFFFF;"
                                          "padding: 10px;"
                                          "margin-top: 40px;")
        self.botonLimpiar.clicked.connect(self.accion_botonLimpiar)

        # Agregamos los dos botones al layout ladoIzquierdo:
        self.ladoIzquierdo.addRow(self.botonRegistrar, self.botonLimpiar)


        # Agregamos el layout ladoIzquiero al layout horizontal:
        self.horizontal.addLayout(self.ladoIzquierdo)



        #-------------- LAYOUT DERECHO-----------------------

        # Creamos el layout del lado derecho:
        self.ladoDerecho = QFormLayout()

        # Se asigna la marge solo a la izquierda de 100px:
        self.ladoDerecho.setContentsMargins(100, 0, 0, 0)

        # Hacemos el letrero:
        self.letrero3 = QLabel()

        # Le escribimos el texto:
        self.letrero3.setText("Recuperar contraseña")

        # Le asignamos el tipo de letra:
        self. letrero3.setFont(QFont("Andale Mono", 20))

        # Le ponemos color de texto y margenes:
        self.letrero3.setStyleSheet("color: #000000;")

        # Agregamos el letrero en la primera fila:
        self.ladoDerecho.addRow(self.letrero3)

        # Hacemos el letrero:
        self.letrero4 = QLabel()

        # Establecemos el ancho del label:
        self.letrero4.setFixedWidth(400)

        # Le escribimos el texto:
        self.letrero4.setText("Por favor ingrese la información para recuperar"
                              "\nla contraseña. Los campos marcados"
                              "\ncon asterisco son obligatorios.")

        # Le asignamos el tipo de letra:
        self.letrero4.setFont(QFont("Andale Mono", 10))

        # Le ponemos color de texto y margenes:
        self.letrero4.setStyleSheet("color: #000000; margin-bottom: 40px;"
                                    "margin-top: 20px;"
                                    "padding-bottom: 10px;"
                                    "border: 2px solid #000000;"
                                    "border-left: none;"
                                    "border-right: none;"
                                    "border-top: none;")

        # Agregamos el letrero en la fila siguiente:
        self.ladoDerecho.addRow(self.letrero4)

        # --- 1

        # Hacemos el letrero de la pregunta 1:
        self.labelPregunta1 = QLabel("Pregunta de verificación 1*")

        # Agregamos el letrero en la fila siguiente:
        self.ladoDerecho.addRow(self.labelPregunta1)

        # Hacemos el campo para ingresar la pregunta 1:
        self.pregunta1 = QLineEdit()
        self.pregunta1.setFixedWidth(320)

        # Agregamos el campo en el formulario:
        self.ladoDerecho.addRow(self.pregunta1)

        # Hacemos el letrero de la respuesta 1:
        self.labelRespuesta1 = QLabel("Respuesta de verificación 1*")

        # Agregamos el letrero en la fila siguiente:
        self.ladoDerecho.addRow(self.labelRespuesta1)

        # Hacemos el campo para ingresar la respuesta 1:
        self.respuesta1 = QLineEdit()
        self.respuesta1.setFixedWidth(320)

        # Agregamos el campo en el formulario:
        self.ladoDerecho.addRow(self.respuesta1)

        # --- 2

        # Hacemos el letrero de la pregunta 2:
        self.labelPregunta2 = QLabel("Pregunta de verificación 2*")

        # Agregamos el letrero en la fila siguiente:
        self.ladoDerecho.addRow(self.labelPregunta2)

        # Hacemos el campo para ingresar la pregunta 2:
        self.pregunta2 = QLineEdit()
        self.pregunta2.setFixedWidth(320)

        # Agregamos el campo en el formulario:
        self.ladoDerecho.addRow(self.pregunta2)


        # Hacemos el letrero de la respuesta 2:
        self.labelRespuesta2 = QLabel("Respuesta de verificación 2*")

        # Agregamos el letrero en la fila siguiente:
        self.ladoDerecho.addRow(self.labelRespuesta2)

        # Hacemos el campo para ingresar la respuesta 2:
        self.respuesta2 = QLineEdit()
        self.respuesta2.setFixedWidth(320)

        # Agregamos el campo en el formulario:
        self.ladoDerecho.addRow(self.respuesta2)


        # --- 3

        # Hacemos el letrero de la pregunta 3:
        self.labelPregunta3 = QLabel("Pregunta de verificación 3*")

        # Agregamos el letrero en la fila siguiente:
        self.ladoDerecho.addRow(self.labelPregunta3)

        # Hacemos el campo para ingresar la pregunta 3:
        self.pregunta3 = QLineEdit()
        self.pregunta3.setFixedWidth(320)

        # Agregamos el campo en el formulario:
        self.ladoDerecho.addRow(self.pregunta3)

        # Hacemos el letrero de la respuesta 2:
        self.labelRespuesta3 = QLabel("Respuesta de verificación 3*")

        # Agregamos el letrero en la fila siguiente:
        self.ladoDerecho.addRow(self.labelRespuesta3)

        # Hacemos el campo para ingresar la respuesta 3:
        self.respuesta3 = QLineEdit()
        self.respuesta3.setFixedWidth(320)

        # Agregamos el campo en el formulario:
        self.ladoDerecho.addRow(self.respuesta3)

        # Hacemos el botón para buscar las preguntas:
        self.botonBuscar = QPushButton("Buscar")

        # Establecemos el ancho del boton:
        self.botonBuscar.setFixedWidth(90)

        # Le ponemos los estilos:
        self.botonBuscar.setStyleSheet("background-color: #008B45;"
                                       "color: #FFFFFF;"
                                       "padding: 9px;"
                                       "margin-top: 40px;")
        self.botonBuscar.clicked.connect(self.accion_botonBuscar)

        # Hacemos el botón para recuperar la contraseña:
        self.botonRecuperar = QPushButton("Recuperar")

        # Establecemos el ancho del boton:
        self.botonRecuperar.setFixedWidth(90)

        # Le ponemos los estilos:
        self.botonRecuperar.setStyleSheet("background-color: #008B45;"
                                       "color: #FFFFFF;"
                                       "padding: 9px;"
                                       "margin-top: 40px;")
        self.botonRecuperar.clicked.connect(self.accion_botonRecuperar)

        # Agregamos los dos botones al layout ladoDerecho:
        self.ladoDerecho.addRow(self.botonBuscar, self.botonRecuperar)


        # Agregamos el layout ladoDerecho al layout horizontal:
        self.horizontal.addLayout(self.ladoDerecho)


        #------------- OJO IMPORTANTE PONER AL FINAL---------

        #  Indicamos que el layout principal del fondo es horizontal
        self.fondo.setLayout(self.horizontal)



        # Creamos la ventana de dialogo:
        self.ventanaDialogo = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)

        # Definimos el tamaño de la ventana:
        self.ventanaDialogo.resize(300, 150)

        # Creamos el botón para aceptar:
        self.botonAceptar = QDialogButtonBox.Ok
        self.opciones = QDialogButtonBox(self.botonAceptar)
        self.opciones.accepted.connect(self.ventanaDialogo.accept)

        # Establecemos el titulo de la ventana:
        self.ventanaDialogo.setWindowTitle("Formulario de registro")

        # Configuramos la ventana para que sea modal:
        self.ventanaDialogo.setWindowModality(Qt.ApplicationModal)

        # Creamos un layout vertical
        self.vertical = QVBoxLayout()

        # Creamos un label para los mensajes:
        self.mensaje = QLabel("")

        # Le ponemos estilos al label mensaje:
        self.mensaje.setStyleSheet("background-color: #008B45; color: #FFFFFF; padding: 10px;")

        # Agregamos el label de mensajes:
        self.vertical.addWidget(self.mensaje)

        # Agregamos las opciones de los botones:
        self.vertical.addWidget(self.opciones)

        # Establecemos el layout para la ventana:
        self.ventanaDialogo.setLayout(self.vertical)

        # Variable para controlar que se han ingresado los datos correctos:
        self.datosCorrectos = True


    # Metodo del botonLimpiar:

    def accion_botonLimpiar(self):
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

    # Metodo del botonRegistrar
    def accion_botonRegistrar(self):

        # Validamos que los passwords sean iguales
        if (
            self.password.text() != self.password2.text()
        ):
            self.datosCorrectos = False

            # Escribimos el texto explicativo:
            self.mensaje.setText("Los passwords no son iguales")

            # Hacemos que la ventana de dialogo se vea:
            self.ventanaDialogo.exec_()

        # Validamos que se ingresen todos los campos
        if(
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

            # Escribimos el texto explicativo
            self.mensaje.setText("Debe ingresar todos los campos")

            # Hacemos que la ventana de dialogo se vea:
            self.ventanaDialogo.exec_()

        # Si los datos están correctos:
        if self.datosCorrectos:

            # Abrimos el archivo en modo agregar escribiendo datos binarios.
            self.file = open('datos/clientes.text', 'ab')

            # Traer el texto de los QLineEdit() y los agrega concatenandolos.
            # Para escribirlos en el archivo en formato binario utf-8
            self.file.write(bytes(
                self.nombreCompleto.text() + ";"
                + self.usuario.text() + ";"
                + self.password.text() + ";"
                + self.password2.text() + ";"
                + self.documento.text() + ";"
                + self.correo.text() + ";"
                + self.pregunta1.text() + ";"
                + self.respuesta1.text() + ";"
                + self.pregunta2.text() + ";"
                + self.respuesta2.text() + ";"
                + self.pregunta3.text() + ";"
                + self.respuesta3.text() + "\n"
                ,encoding='UTF-8'))

            # Cerramos el archivo.
            self.file.close()

            # Abrimos en modo lectura en formato bytes
            self.file = open('datos/clientes.text','rb')
            # Recorrer el archivo linea por linea.
            while self.file:
                linea = self.file.readline().decode('UTF-8')
                print(linea)
                if linea == '':
                    break
            self.file.close()


    # Metodo del botonBuscar
    def accion_botonBuscar(self):

        # Establecemos el titulo de la ventana:
        self.ventanaDialogo.setWindowTitle("Buscar preguntas de validación")

        # Validar que se haya ingresado el documento:
        if(
            self.documento.text() == ''
        ):
            self.datosCorrectos = False

            # Escribimos el texto explicativo:
            self.mensaje.setText("Si va a buscar las preguntas"
                                 "\npara recuperar la contraseña."
                                 "\nDebe primero, ingresar el documento.")

            # Hacemos que la ventana de dialogo se vea:
            self.ventanaDialogo.exec_()

        # validar si el documento es numerico:
        if (
            not self.documento.text().isnumeric()
        ):
            self.datosCorrectos = False

            # Escribimos el texto explicativo:
            self.mensaje.setText("El documento debe ser númerico."
                                 "\nNo ingrese letras"
                                 "\nni caracterés especiales.")

            # Hacemos que la ventana de dialogo se vea:
            self.ventanaDialogo.exec_()

            # Limpiamos el campo del documento:
            self.documento.setText('')


        # Si los datos estan correcto:
        if (
            self.datosCorrectos
        ):

            # Abrimos el archivo en modo de lectura:
            self.file = open('datos/clientes.text', 'rb')

            # Lista vacia para guardar los usuarios:
            usuarios = []

            while self.file:
                linea = self.file.readline().decode('UTF-8')
                # Obtenemos del string una lista con 11 datos separados por ;
                lista = linea.split(";")

                # Se para si ya no hay mas registros en el archivo
                if linea == '':
                    break

                # Creamos un onejto tipo cliente llamado u
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
                usuarios.append(u)

            # Cerramos el archivo:
            self.file.close()

            # En este punto tenemos la lista de usuarios con todos los usuarios:

            # Variable para controlar si existe el documento:
            existeDocumento = False

            # Buscamos en la lista usuario por usuario si existe la cedula:
            for u in usuarios:

                # comparamos el documento ingresado:
                # si corresponde con el documento, es el usuario correcto:
                if u.documento == self.documento.text():

                    #Mostramos las preguntas en el formulario
                    self.pregunta1.setText(u.pregunta1)
                    self.pregunta2.setText(u.pregunta2)
                    self.pregunta3.setText(u.pregunta3)
                    # Indicamos que encontramos el documento:
                    existeDocumento = True
                    # Paramos el for:
                    break

            # Si no existe un usuario con este documento:
            if(
                    not existeDocumento
            ):
                # Escribimos el texto explicativo:
                self.mensaje.setText("No existe un usuario con este documento:\n"
                                     + self.documento.text())

                # Hacemos que la ventana de dialogo se vea:
                self.ventanaDialogo.exec_()





    # Metodo del botonRecuperar
    def accion_botonRecuperar(self):
        pass







if __name__ == '__main__':

    app = QApplication(sys.argv)

    ventana1 = Ventana1()

    ventana1.show()

    sys.exit(app.exec_())
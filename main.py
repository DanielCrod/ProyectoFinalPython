import sys

from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import easygui as easygui



class Producto():
    def __init__(self, nombreProducto, descripcion, precio, marca):
        self.NombreProducto = nombreProducto
        self.descripcion = descripcion
        self.precio = precio
        self.marca = marca

ListaProductos=[]
listaFactura = []

class ejemplo_GUI(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("untitled.ui", self)
        self.anadir.clicked.connect(self.guardar)
        self.listView = QListWidget(self.listView)
        self.elimina.clicked.connect(self.eliminar)
        self.limpia.clicked.connect(self.limpiar)
        self.factura.clicked.connect(self.mostrarFactura)


    def cargarFactura(self):
        for Producto in ListaProductos:
            listaFactura.append(Producto.NombreProducto + "" + "{:2f}".format(Producto.precio))
            listaFactura.sort()
            return listaFactura.str()


    def mostrarFactura(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Factura")

        txtFactura = "Factura mostrada a continuación: \n \n"
        txtFactura += ("Total a pagar: "  + "€" + "\n")

        msgBox.setText(txtFactura)

        msgBox.addButton(QMessageBox.Ok)
        moreButton = QPushButton("Más")
        msgBox.addButton(moreButton, QMessageBox.ActionRole)

        msgBox.setDefaultButton(moreButton)

        def infoFactura():
            facturaInfo = "Más info: \n\n"
            facturaInfo += ("Productos contenidos: \n\n + \n\n")
            facturaInfo += ("Precio final:")

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Info completa")

            msg.setText(facturaInfo)

            moreButton.clicked.connect(infoFactura)
            returnValue = msgBox.exec_()



    def guardar(self):
        nombreProducto = self.nProducto.text()
        descripcion = self.descripcion.text()
        precio = self.precio.text()
        marca = self.marca.text()
        p = Producto(nombreProducto, descripcion, precio, marca)
        ListaProductos.append(p)
        self.actualizar()
        QMessageBox.information(self, "Producto Añadido", "Producto añadido: " + p.NombreProducto +"!")
        self.nProducto.setText("")
        self.descripcion.setText("")
        self.precio.setText("")
        self.marca.setText("")

        self.total.setText(self.sumar().__str__())


    def sumar(self):
        value = 0
        for i in ListaProductos:
            producto = i
            value = value + int(producto.precio)
        return value


    def eliminar(self):
        self.listView.takeItem(self.listView.currentRow())
        QMessageBox.information(self, "Producto Eliminado", "Producto eliminado!")
        self.total.setText("")

    def limpiar(self):
        self.nProducto.setText("")
        self.descripcion.setText("")
        self.precio.setText("")
        self.marca.setText("")

    def actualizar(self):
        self.listView.clear()
        for i in ListaProductos:
            producto = i
            item1 = QListWidgetItem(producto.NombreProducto)
            self.listView.addItem(item1)







if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = ejemplo_GUI()
    GUI.show()
    sys.exit(app.exec_())
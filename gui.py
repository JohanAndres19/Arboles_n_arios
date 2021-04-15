import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

class Ventana_principal(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ventana_principal.ui",self)
        #self.Boton_agregar.clicked.connect()

    def Agregar(self):
        self.texto




if __name__ =="__main__":
    app =QApplication(sys.argv)
    gui = Ventana_principal()
    gui.show()
    sys.exit(app.exec_())






        
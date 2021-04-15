import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsScene
from PyQt5.QtGui import QFont, QPen,QPainter,QBrush
from PyQt5.QtCore import Qt

class Ventana_principal(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ventana_principal.ui",self)
        self.escena= QGraphicsScene()
        self.green_brush =QBrush(Qt.green)
        self.blue_brush=QBrush(Qt.blue)
        self.canvas.backgroundBrush(self.green_brush)
        self.pen =QPen(Qt.red)
        self.texto.setClearButtonEnabled(True)
        self.texto_traducido.setClearButtonEnabled(True)
        self.Boton_agregar.clicked.connect(self.Agregar)

    def Agregar(self):
        a=self.texto.text()
        b=self.texto_traducido.text()
        self.texto.clear()
        self.texto_traducido.clear()
        print(a,b)

    def paintEvent(self, e):
        painter = QPainter(self.canvas)
        painter.setPen(self.pen)
        painter.drawLine(0,0,10,0)   


class modelo:

    def __init__(self) :
        pass



if __name__ =="__main__":
    app =QApplication(sys.argv)
    gui = Ventana_principal()
    gui.show()
    sys.exit(app.exec_())






        
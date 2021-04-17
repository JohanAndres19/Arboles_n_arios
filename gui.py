import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsScene, QWidget
from PyQt5.QtGui import QFont, QPalette, QPen,QPainter,QBrush
from PyQt5.QtCore import Qt

class Ventana_principal(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ventana_principal.ui",self)
        self.setAutoFillBackground(True)
        Paleta_color =self.palette()
        Paleta_color.setColor(self.backgroundRole(),Qt.cyan)
        self.setPalette(Paleta_color)
        self.canvas = canvas(self.contenedor_canvas)
        self.canvas.resize(self.contenedor_canvas.width(),self.contenedor_canvas.height())
        self.canvas.setAutoFillBackground(True)
        self.canvas.setBackgroundRole(QPalette.Base)
        self.texto.setClearButtonEnabled(True)
        self.texto_eliminar.setClearButtonEnabled(True)
        self.texto_buscar.setClearButtonEnabled(True)
        self.texto_traducido.setClearButtonEnabled(True)
        self.Boton_agregar.clicked.connect( lambda:self.canvas.dibujar(self.texto,self.texto_traducido))
        

    def Agregar(self):
        a=self.texto.text()
        b=self.texto_traducido.text()
        self.texto.clear()
        self.texto_traducido.clear()
        print(a,b)
       
    
class canvas (QWidget):

    def __init__(self, parent):
        super().__init__(parent=parent)
        self.a=None
        self.b =None


    def dibujar(self,valor1,valor2):
        self.a=valor1.text()
        self.b=valor2.text()
        valor1.clear()
        valor2.clear()
        self.update()


    def paintEvent(self,evento) :
        painter = QPainter()
        painter.begin(self)
        if self.a != None and self.b!=None:
            self.pen =QPen(Qt.red)
            painter.setPen(self.pen)
            """
            painter.drawText(30,30,16,15,Qt.AlignCenter,self.a[0])
            painter.drawLine(36,46,36,61)
            painter.drawText(30,62,16,15,Qt.AlignCenter,self.a[1])
            painter.drawLine(36,78,36,93)
            painter.drawText(30,94,16,15,Qt.AlignCenter,self.a[2])
            painter.drawLine(36,110,36,125)
            painter.drawText(30,126,16,15,Qt.AlignCenter,self.a[3])
            """
            for i in range(len(self.a)):
                if i == 0:
                    painter.drawText(30,30,16,15,Qt.AlignCenter,self.a[i])
                    painter.drawLine(36,46,36,61)
                elif i== (len(self.a)-1):
                    painter.drawText(30,30+(32*i),16,15,Qt.AlignCenter,self.a[i])
                else:    
                    painter.drawText(30,30+(32*i),16,15,Qt.AlignCenter,self.a[i])
                    painter.drawLine(36,46+(32*i),36,61+(32*i))



class modelo:

    def __init__(self) :
        pass



if __name__ =="__main__":
    app =QApplication(sys.argv)
    gui = Ventana_principal()
    gui.show()
    sys.exit(app.exec_())






        
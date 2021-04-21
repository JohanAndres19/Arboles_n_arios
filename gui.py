import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsScene, QMessageBox, QWidget
from PyQt5.QtGui import QFont, QPalette, QPen,QPainter,QBrush
from PyQt5.QtCore import Qt
from Palabras import Ingresar

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
        self.b_palabras=False
        self.diccionario={}
        self.palabras=[]
        self.matriz_dibujar=[]


    def dibujar(self,valor1,valor2):
        if valor1.text()!=''and valor2.text()!='':
            self.a=valor1.text().split(',')
            self.b=valor2.text().split(',')
            if len(self.a)==len(self.b):
                self.b_palabras=True
                self.a=[i.strip() for i in self.a]
                self.b=[i.strip() for i in self.b]
                self.a=[i.upper() for i in self.a]
                self.b=[i.upper() for i in self.b]
                for  i in range(len(self.a)):
                    self.diccionario[self.a[i]]=self.b[i]
                self.palabras=self.a
                self.matriz_dibujar=Ingresar(self.palabras,self.diccionario).verificar()   
                valor1.clear()
                valor2.clear()
            else:
                QMessageBox.warning(self,"   Advertencia   ", "  Verifique la cantidad de palabras  ")    
        else:
            QMessageBox.warning(self,"   Advertencia   ", "  Ingrese Valores    ")
        self.update()


    def paintEvent(self,evento) :
        painter = QPainter()
        painter.begin(self)
        if self.a != None and self.b!=None and self.b_palabras:
            self.pen =QPen(Qt.red)
            painter.setPen(self.pen)
            x=32
            y=32
            for i in range(len(self.matriz_dibujar)):
                if len(self.matriz_dibujar[i])!=0:
                    for j in range(len(self.matriz_dibujar[i])):
                      painter.drawText(30+(x*i),40+(j*y),16,15,Qt.AlignCenter,self.matriz_dibujar[i][j])  
            
                    

class modelo:

    def __init__(self) :
        pass





if __name__ =="__main__":
    app =QApplication(sys.argv)
    gui = Ventana_principal()
    gui.show()
    sys.exit(app.exec_())






        
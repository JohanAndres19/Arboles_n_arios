class Componente:
    
    def operacion(self):
        pass

class Arbol(Componente):
    
    def __init__(self,nombre,letras=None):
       self.partes=[]
       self.nombre=nombre
       self.letras=letras

    def operacion(self):
        if self.letras!=None:
            self.nombre=self.nombre.replace(self.letras,'',1)
        cad = self.nombre+"("
        for i in self.partes:
            cad+=i.operacion()+","
        cad= cad[0:len(cad)]+")"
        return cad   

    def funcion(self):
        if self.letras==None:
            pass

    def add_Componente(self,componente):
        self.partes.append(componente)   

    def Get__Partes(self):
        return self.partes

    def Get_componente(self,valor=0):
        return self.partes[valor] 

class construir_arbol:

    def __init__(self,lista_palabras,lista_letras):
        self.lista_palabras=lista_palabras
        self.lista_letras=lista_letras
        self.construir()

    def construir(self):
        self.arbol = Arbol("?")
        self.inicial=[]
        for i in self.lista_palabras:
            self.arbol.add_Componente(Arbol(i[0]))
            self.inicial.append(i[0])
        
        print("\n",self.lista_letras[2].Get_diccionario(),self.lista_palabras[2])
        for i in range(len(self.lista_palabras)):
           self.Agregar(self.lista_palabras[i],self.lista_letras[i].Get_diccionario(),i)
   
        print("\n",self.arbol.operacion())
        print("\n",self.lista_letras[2].Get_diccionario(),self.lista_palabras[2])
        
   
    def Agregar(self,lista_nodos,asociacones,pos_raiz):
        auxiliar=0
        if len(asociacones)>0:
            pos=0
            while pos in asociacones:
                max= self.maximo(asociacones[pos])
                if max[0] == 1:
                    pos+=1
                    self.arbol.Get__Partes()[pos_raiz].add_Componente(Arbol(lista_nodos[pos],(asociacones[pos-1])[max[1]]))
                else:
                    while max[0] > 1:
                        pos_max= max[1]
                        pos_max=pos_max+pos+1
                        if pos>0:
                            self.arbol.Get__Partes()[pos_raiz].Get_componente(pos-1).add_Componente(Arbol(lista_nodos[pos_max],(asociacones[pos])[max[1]]))
                        elif pos ==0:
                            self.arbol.Get__Partes()[pos_raiz].add_Componente(Arbol(lista_nodos[pos_max],(asociacones[pos])[max[1]]))
                        (asociacones[pos])[max[1]]=""
                        auxiliar=pos_max
                        max =self.maximo((asociacones[pos]))
                    pos=auxiliar    
    

    def maximo(self,lista):
        aux=lista[0]
        max=0
        posicion=0
        if len(lista)>1:
            for i in range(1,len(lista)):
                if len(lista[i])>len(aux):
                    posicion=i
                    aux=lista[i]
        max=(len(aux),posicion)         
        return max       


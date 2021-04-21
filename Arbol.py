class Componente:
    
    def operacion(self):
        pass

    def operacion3(self):
        pass
class Arbol(Componente):
    
    def __init__(self,nombre,letras=None,Traduccion=None):
       self.partes=[]
       self.nombre=nombre
       self.letras=letras
       self.traduccion =Traduccion

    def operacion(self):
        if self.letras!=None:
            for i  in self.letras:
             self.nombre=self.nombre.replace(i,'*',1)

        cad = self.nombre+"("
        for i in self.partes:
            cad+=i.operacion()+","
        cad= cad[0:len(cad)]+")"
        return cad   

    def operacion2(self):
        return self.nombre

    def operacion3(self):
        if self.traduccion==None:
            self.traduccion=""
        traduc=self.traduccion+','
        for i in self.partes:
            traduc+=i.operacion3()
        return traduc    

    def add_Componente(self,componente):
        self.partes.append(componente)   

    def Get__Partes(self):
        return self.partes

    def Get_componente(self,valor=0):
        return self.partes[valor] 

class construir_arbol:

    def __init__(self,lista_palabras,lista_letras,diccionario=None):
        self.lista_palabras=lista_palabras
        self.lista_letras=lista_letras
        self.diccionario =diccionario
        self.aux_arbol=None

    def construir(self):
        self.Matriz=[]
        pila=[]
        self.arbol = Arbol("?")
        self.inicial=[]
        for i in self.lista_palabras:
            self.arbol.add_Componente(Arbol(i[0],Traduccion=self.diccionario[i[0]]))
            self.inicial.append(i[0])
        for i in range(len(self.lista_palabras)):
           self.Agregar(self.lista_palabras[i],self.lista_letras[i].Get_diccionario(),i)
        arbol_l =self.arbol.operacion()
        i=0
        aux=arbol_l
        print(arbol_l)
        aux=aux.replace('(','}')
        aux=aux.replace(',','')
        aux=aux.replace(')','')
        print("\n",aux)
        while i < len(arbol_l):
            columna=[]
            if arbol_l[i]=='(':
                pila.append(arbol_l[i])
                if arbol_l[i+1]==')':
                    pila.pop()
                    if len(pila)==0:
                        break
                    elif len(pila)==1:
                        self.Matriz.append(columna)
                    i+=2
                else:
                    i+=1    
            elif arbol_l[i]==')':    
                pila.pop()
                if len(pila)==0:
                    break
                elif len(pila)==1:
                    self.Matriz.append(columna)
                i+=1
            elif arbol_l[i].isalpha() or arbol_l[i]=='*' :
                while arbol_l[i]!='(' and arbol_l[i]!=')' and arbol_l[i]!=',':
                    if arbol_l[i]=='*':
                        columna.append(' ')
                    else:
                        columna.append(arbol_l[i])
                    i+=1
                columna.append('}')
                self.Matriz.append(columna)    
            else:
                i+=1
        for i in range(len(self.Matriz)):
            for j in range(len(self.Matriz[i])):
                print(self.Matriz[i][j],end=" ")
            print()  
        print(self.arbol.operacion3())     
        return self.Matriz

   
    def Agregar(self,lista_nodos,asociacones,pos_raiz):
        auxiliar=0
        max_aux=0
        repetido=False
        if len(asociacones)>0:
            pos=0
            while pos in asociacones:
                max= self.maximo(asociacones[pos])
                if max[0] == 1:
                    pos+=1
                    self.arbol.Get__Partes()[pos_raiz].add_Componente(Arbol(lista_nodos[pos],(asociacones[pos-1])[max[1]],self.diccionario[lista_nodos[pos]]))
                else:
                    while max[0] > 1:
                        pos_max= max[1]
                        if (asociacones[pos]).count((asociacones[pos])[max[1]])==1:
                            pos_max=pos_max+pos+1
                            if pos>0:
                                self.arbol.Get__Partes()[pos_raiz].Get_componente(pos-1).add_Componente(Arbol(lista_nodos[pos_max],(asociacones[pos])[max[1]],self.diccionario[lista_nodos[pos_max]]))
                            elif pos ==0:
                                self.arbol.Get__Partes()[pos_raiz].add_Componente(Arbol(lista_nodos[pos_max],(asociacones[pos])[max[1]],self.diccionario[lista_nodos[pos_max]]))
                            (asociacones[pos])[max[1]]=""
                            auxiliar=pos_max
                            max =self.maximo((asociacones[pos]))
                        else:
                            if auxiliar>1 and pos!=0:
                                pos=pos+auxiliar-1
                            else:
                                pos=pos+auxiliar
                            repetido=True
                            break
                    else:
                        pos=auxiliar
                    if repetido:
                        max_aux=(asociacones[pos]).count((asociacones[pos])[max[1]])
                        pos_max= max[1]
                        pos_max=pos_max+pos+1
                        self.arbol.Get__Partes()[pos_raiz].add_Componente(Arbol(lista_nodos[pos_max],(asociacones[pos])[max[1]],self.diccionario[lista_nodos[pos_max]]))
                        contador=1
                        pos+=1
                        while contador< max_aux:
                            aux=max
                            max =self.maximo((asociacones[pos]))
                            pos_max= max[1]
                            pos_max=pos_max+pos+1
                            if max[0]>aux[0]:
                                if pos <=2:
                                    self.arbol.Get__Partes()[pos_raiz].Get_componente(pos-1).add_Componente(Arbol(lista_nodos[pos_max],(asociacones[pos])[max[1]],self.diccionario[lista_nodos[pos_max]]))
                                else:
                                    self.Ultimo_nivel(self.arbol.Get__Partes()[pos_raiz])
                                    print(self.aux_arbol.operacion2())
                                    self.aux_arbol.add_Componente(Arbol(lista_nodos[pos_max],(asociacones[pos])[max[1]],self.diccionario[lista_nodos[pos_max]]))
                                contador+=1
                                pos+=1
                            elif max[0]==1 :
                                break
                            else:
                                self.arbol.Get__Partes()[pos_raiz].add_Componente(Arbol(lista_nodos[pos_max],(asociacones[pos])[max[1]],self.diccionario[lista_nodos[pos_max]]))
                                contador+=1
                                pos+=1
                        else:
                            repetido=False
  
    
    def Ultimo_nivel(self,Arbol):
        if len(Arbol.Get__Partes())==0:
            self.aux_arbol=Arbol
        else:
           self.Ultimo_nivel(Arbol.Get__Partes()[len(Arbol.Get__Partes())-1])    

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


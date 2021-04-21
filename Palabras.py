from Arbol import *
import math

class Palabra:
    """
        Esta clase se encarga de compara las palabras
         para ver caracteres coinsiden entre ellas 
    """
    def __init__(self,palabra1,palabra2):
        self._palabra1=palabra1
        self._palabra2=palabra2
        self._letras_iguales=""


    def Comparar(self): 
        """
        este metodo es el encargado de comparar las dos palabras 
        que se añaden al crear el objeto de la clase de froam que se retorne la concatenacion 
        de  los caracteres similares en orden 
        """
        posiciones=[]
        if len(self._palabra1)<=len(self._palabra2):
            for indice,valor  in enumerate(self._palabra1):
                if valor == self._palabra2[indice]:
                    posiciones.append(indice)
                else:
                    break;    
        else:
            for indice,valor  in enumerate(self._palabra2):
                if valor == self._palabra1[indice]:
                    posiciones.append(indice)
                else:
                    break   
        if len(posiciones)!=0:         
            for i in posiciones:
                self._letras_iguales+=self._palabra1[i]
        return self._letras_iguales        
        
class Ingresar:
    """
        Esta clase es la encargada de ingresar los valore por consola
        (clase que hay que cambiar para el manejo de interface garfica)
    """

    def __init__(self,palabras=None,diccionario=None):  
        self.lista_palabras =palabras
        self.diccionario= diccionario
        self.lista_letras=[]
        #self.Iniciar()
        
    
    def  Iniciar(self):
        """
            metodo que inicia con la insercion de las palabras que van a componer el arbol 
        """
        archivo = open("prueba.txt",'r')
        mensaje = archivo.readlines()
        mensaje.pop(0)
        palabra=[s.strip('\n')for s in mensaje]
        palabras=palabra[4]
        archivo.close()
        self.lista_palabras = palabras.split(',')
        self.verificar()
        
    def verificar(self):
        posicion=[]
        sublistas=[]
        tamaño=[]
        self.lista_palabras.sort()
        """ Metodo que se enacarga de buscar las letras semejantes dentro de las 
            palabras ademas de agrupar las palabras semejantes  de tal forma que se mas facil  relacionar 
            que palabra es padre de otra 
        """
        for i in range(len(self.lista_palabras)):
           contador=i+1
           aux=self.lista_palabras[i]
           while contador<(len(self.lista_palabras)):
                aux1=Palabra(aux,self.lista_palabras[contador]).Comparar()
                if len(aux1) !=0:
                    self.lista_letras.append(aux1)
                else:
                    if posicion.count(contador)==0:
                        posicion.append(contador)
                    break;     
                contador+=1         
        posicion.append(len(self.lista_palabras))
        sublistas=self.Agrupar_Palabras(posicion)     
        for i in sublistas:
            contador=0
            contador=((len(i))*(len(i)-1))//2
            tamaño.append(contador)
        self.letras_agru= self.Agrupar_Letras(tamaño)
        a= construir_arbol(sublistas,self.letras_agru,self.diccionario).construir()  
        return a

    def  Agrupar_Palabras(self,posicion):
        """
            Este metodo agrupa las palabra usando una lista de refenrencia donde se 
            asignan las posiciones donde  la coinsidencia entre las palabras  es nula, lo que significa 
            que no son similares; permitiendo  asociar las que si son semejantes 
        """
        auxiliar=0
        sublistas=[]
        for valor in posicion:
            aux=[]
            for x in range(auxiliar,valor):
                aux.append(self.lista_palabras[x])
            sublistas.append(aux)
            auxiliar=valor       
        return sublistas 

    def Agrupar_Letras(self,tamaño):
        """
            Este metodo  se encarga de asociar cada conjuto de letras, respecto a la cantidad
            de comparaciones  realizadas 
        """
        auxiliar1=0
        auxiliar2=0
        lista_letras_asociadas=[]
        for i in tamaño:
            auxiliar2+=i
            lista=[]
            for x in range(auxiliar1,auxiliar2):
                lista.append(self.lista_letras[x])       
            discri= 1+8*(len(lista))
            a2= (1+ math.sqrt(discri))/2
            lista_letras_asociadas.append(asociacion(lista,int(a2)))
            auxiliar1=auxiliar2
        return lista_letras_asociadas    


class asociacion :
    def __init__(self,lista,base):
        self.base=base
        self.lista=lista
        self.dicicionario={}
        self.asociar()
       
    def asociar(self):
        self.aux_lista=[]
        aux1=0
        aux2=(self.base-1)
        for i in range((self.base-1),0,-1):
            lista=[]
            for j in range(aux1,aux2):
                lista.append(self.lista[j])
            aux1=aux2
            aux2=(i-1)+aux2
            self.aux_lista.append(lista)
        self.llenar_diccioanrio()   

    def llenar_diccioanrio(self):
        for i in range(len(self.aux_lista)):
            self.dicicionario[i]=self.aux_lista[i]   

    def Get_diccionario(self):
        return self.dicicionario    
        


if __name__ =="__main__":
    Ingresar()

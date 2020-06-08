from claseNodo import Nodo
from claseIColeccion import IColeccion
from zope.interface import implementer

@implementer(IColeccion)
class Coleccion:
    __comienzo=None
    __actual=None
    __indice=0
    __tope=0

    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            personal = self.__actual.getPersonal()
            self.__actual = self.__actual.getSiguiente()
            return personal

    def __len__ (self):
        return self.__tope

    def insertarElemento (self,elemento,pos):
        band = False
        if (pos < -self.__tope) or (pos > self.__tope):
            if (pos == -1):
                band = True
            else:
                raise IndexError('list index out of range')
        else:
            band = True
        if band:
            nodo = Nodo(elemento)
            if self.__comienzo == None:    #Coleccion vacía
                self.__comienzo = nodo
                self.__actual = nodo
                self.__tope += 1
            else:
                if pos >= 0:
                    if pos == 0:                                #Posicion positivo
                        nodo.setSiguiente(self.__comienzo)
                        self.__comienzo = nodo
                        self.__actual = nodo
                        self.__tope += 1
                    else:
                        ant = self.__comienzo
                        aux = ant.getSiguiente()
                        i = 0
                        while i < (pos - 1):
                            ant = aux
                            aux = aux.getSiguiente()
                            i += 1
                        nodo.setSiguiente(aux)
                        ant.setSiguiente(nodo)
                        self.__tope += 1
                else:                                           #Posicion negativa
                    if pos == -self.__tope:
                        nodo.setSiguiente(self.__comienzo)
                        self.__comienzo = nodo
                        self.__actual = nodo
                        self.__tope += 1
                    else:
                        ant = self.__comienzo
                        aux = ant.getSiguiente()
                        i = -self.__tope
                        while i < (pos - 1):
                            ant = aux
                            aux = aux.getSiguiente()
                            i += 1
                        nodo.setSiguiente(aux)
                        ant.setSiguiente(nodo)
                        self.__tope += 1


    def agregarElemento (self,elemento):
        nodo = Nodo(elemento)
        if self.__comienzo == None:
            self.__comienzo = nodo
            self.__actual = nodo
            self.__tope += 1
        else:
            ant = self.__comienzo
            aux = ant.getSiguiente()
            while aux != None:
                ant = aux
                aux = aux.getSiguiente()
            ant.setSiguiente(nodo)
            self.__tope += 1

    def mostrarElemento (self,pos):
        band = False
        if ((pos < -self.__tope) or (pos >= self.__tope)) & (pos != 0):
            if (pos == -1):
                band = True
            else:
                raise IndexError('list index out of range')
        else:
            band = True
        if band:
            if self.__comienzo != None:
                if pos >= 0:                          #Posicion positiva
                    ant = self.__comienzo
                    aux = ant.getSiguiente()
                    i = 0
                    while i < pos:
                        ant = aux
                        aux = aux.getSiguiente()
                        i += 1
                    print('El tipo del personal es: ' + ant.getPersonal().__class__.__name__)
                else:
                    ant = self.__comienzo             #Posicion negativa
                    aux = ant.getSiguiente()
                    i = -self.__tope
                    while i < pos:
                        ant = aux
                        aux = aux.getSiguiente()
                        i += 1
                    print('El tipo del personal es: ' + ant.getPersonal().__class__.__name__)
            else:
                print('Coleccion vacia.')

    def getElemento (self, pos):
        ant = self.__comienzo
        aux = ant.getSiguiente()
        i = 0
        while i < pos:
            ant = aux
            aux = aux.getSiguiente()
            i += 1
        return ant.getPersonal()

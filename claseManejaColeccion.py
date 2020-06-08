from claseColeccion import Coleccion
from claseApoyo import Apoyo
from claseDocente import Docente
from claseInvestigador import Investigador
from claseDocenteInvestigador import DocenteInvestigador

class ManejaColeccion:
    __agentes = None

    def __init__ (self):
        self.__agentes = Coleccion()

    def agregarPersonalDesdeArch(self,unPersonal):
        self.__agentes.agregarElemento(unPersonal)

    def crearPersonal (self):
        tipo = input('Ingrese la opcion de tipo de personal(1 = Apoyo ; 2 = Docente ; 3 = Investigador ; 4 = Docente Investigador): ')
        unPersonal = None
        if (tipo == '1') or (tipo == '2') or (tipo == '3') or (tipo == '4'):
            cuil = input('Ingrese el cuil del personal: ')
            if cuil.isdigit():
                apellido = input('Ingrese el apellido del personal: ')
                if apellido.isalpha():
                    nombre = input('Ingrese el nombre del personal: ')
                    if nombre.isalpha():
                        sueldoB = input('Ingrese el sueldo basico del personal: ')
                        try:
                            sueldoB = float(sueldoB)
                            antiguedad = input('Ingrese la antiguedad del personal: ')
                            if antiguedad.isdigit():
                                antiguedad = int(antiguedad)
                                if tipo == '1':
                                    categoria = input('Ingrese la categoria del personal Apoyo(1 a 22): ')
                                    if categoria.isdigit():
                                        categoria = int(categoria)
                                        if (categoria > 0) & (categoria <=22):
                                            unPersonal = Apoyo(cuil, apellido, nombre, sueldoB, antiguedad, categoria)
                                        else:
                                            print('La categoria debe ser de 1 a 22')
                                    else:
                                        print('La categoría debe ser un entero.')
                                elif tipo == '2':
                                    carrera = input('Ingrese la carrera del personal Docente: ')
                                    catedra = input('Ingrese la catedra del personal Docente: ')
                                    cargo = input('Ingrese el cargo del personal Docente(simple;semiexclusivo;exclusivo): ')
                                    if (cargo.lower() == 'simple') or (cargo.lower() == 'semiexclusivo') or (cargo.lower() == 'exclusivo'):
                                        cargo = cargo.lower()
                                        #unPersonal = Docente(cuil, apellido, nombre, sueldoB, antiguedad, carrera.lower(), catedra, cargo)
                                        unPersonal = Docente(cuil = cuil, apellido = apellido, nombre = nombre, sueldoB = sueldoB, antiguedad = antiguedad, carrera = carrera.lower(), catedra = catedra, cargo = cargo)
                                    else:
                                        print('Cargo inválido.')
                                elif tipo == '3':
                                    areainv = input('Ingrese el area de investigación del personal Investigador: ')
                                    tipoinv = input('Ingrese el tipo de investigación del personal Investigador: ')
                                    unPersonal = Investigador(cuil = cuil, apellido = apellido, nombre = nombre, sueldoB = sueldoB, antiguedad = antiguedad, areainv = areainv, tipoinv = tipoinv)
                                elif tipo == '4':
                                    areainv = input('Ingrese el area de investigación del personal Docente Investigador: ')
                                    tipoinv = input('Ingrese el tipo de investigación del personal Docente Investigador: ')
                                    carrera = input('Ingrese la carrera del personal Docente Investigador: ')
                                    catedra = input('Ingrese la catedra del personal Docente Investigador: ')
                                    cargo = input('Ingrese el cargo del personal Docente Investigador(simple;semiexclusivo;exclusivo): ')
                                    if (cargo.lower() == 'simple') or (cargo.lower() == 'semiexclusivo') or (cargo.lower() == 'exclusivo'):
                                        cargo = cargo.lower()
                                        categincent = input('Ingrese la categoria de investigacion del programa de incentivos del personal Docente Investigador(I,II,III,IV,V): ')
                                        if (categincent.upper() == 'I') or (categincent.upper() == 'II') or (categincent.upper() == 'II') or (categincent.upper() == 'IV') or (categincent.upper() == 'V'):
                                            categincent = categincent.upper()
                                            impextra = input('Ingrese el importe extra del personal Docente Investigador: ')
                                            try:
                                                impextra = float(impextra)
                                                unPersonal = DocenteInvestigador(cuil = cuil, apellido = apellido, nombre = nombre, sueldoB = sueldoB, antiguedad = antiguedad, carrera = carrera.lower(), catedra = catedra, cargo = cargo, areainv = areainv, tipoinv = tipoinv, categincent = categincent, impextra = impextra)
                                            except ValueError:
                                                print('Importe inválido.')
                                        else:
                                            print('Categoria inválida.')
                                    else:
                                        print('Cargo inválido.')
                            else:
                                print('Antiguedad inválida.')
                        except ValueError:
                            print('Sueldo inválido.')
                    else:
                        print('Nombre inválido.')
                else:
                    print('Apellido inválido.')
            else:
                print('Cuil inválido.')
        else:
            print('Opcion incorrecta.')
        return unPersonal

    def insertarPers (self,pos):
        unPersonal = self.crearPersonal()
        if unPersonal != None:
            try:
                self.__agentes.insertarElemento(unPersonal,pos)
                print('Personal agregado.')
            except IndexError:
                print('No es posible agregar (list index out of range).')
        else:
            print('No se pudo agregar el personal.')

    def agregarPersonalFinal(self):
        unPersonal = self.crearPersonal()
        if unPersonal != None:
            try:
                self.__agentes.agregarElemento(unPersonal)
                print('Personal agregado.')
            except IndexError:
                print('No es posible agregar (list index out of range).')
        else:
            print('No se pudo agregar el personal.')

    def tipoPers (self,pos):
        try:
            self.__agentes.mostrarElemento(pos)
        except IndexError:
            print('No es posible mostrar.')

    def buscCarrera_mostrarPers (self, carrera):
        lista = []
        for personal in self.__agentes:
            if isinstance(personal, DocenteInvestigador):
                if personal.getCarrera() == carrera:
                    lista.append(personal)
        if lista != []:
            print('Listado: ')
            ordenados = sorted([personal.getNombre() for personal in lista])
            for nombre in ordenados:
                band = False
                i = 0
                while (i < len(lista)) & (not band):
                    if lista[i].getNombre() == nombre:
                        band = True
                    else:
                        i += 1
                print(lista[i])
        else:
            print('No hay Docentes Investigador de esa carrera.')

    def contar_DocInvest_Invest(self, area):
        DocInv = 0
        Inv = 0
        for personal in self.__agentes:
            if (isinstance(personal, DocenteInvestigador)) or (isinstance(personal, Investigador)):
                if personal.getAreaInvestigacion().lower() == area:
                    if (isinstance(personal, DocenteInvestigador)):
                        DocInv += 1
                    else:
                        Inv += 1
        print('La cantidad de personal Docente Investigador de esa area es: {}'.format(DocInv))
        print('La cantidad de personal Investigador de esa area es: {}'.format(Inv))

    def mostrarPersonal(self):
        ordenados = sorted([personal.getApellido() for personal in self.__agentes])
        if ordenados != []:
            for apellido in ordenados:
                band = False
                i = 0
                while (i < len(self.__agentes)) & (not band):
                    if self.__agentes.getElemento(i).getApellido().lower() == apellido.lower():
                        band = True
                    else:
                        i += 1
                print('Nombre y Apellido: {}'.format(self.__agentes.getElemento(i).getNombre()+' '+self.__agentes.getElemento(i).getApellido()))
                print('Tipo de Personal: {}'.format(self.__agentes.getElemento(i).__class__.__name__))
                print('Sueldo: {:0.2f}'.format(self.__agentes.getElemento(i).calcularSueldo()))
                print('----------')
        else:
            print('No hay personal cargado.')

    def buscC_listarP(self, categoria):
        total = 0.0
        band = False
        for personal in self.__agentes:
            if isinstance(personal, DocenteInvestigador):
                if personal.getCategoriaIncentivo() == categoria:
                    print('Apellido: {}'.format(personal.getApellido()))
                    print('Nombre: {}'.format(personal.getNombre()))
                    print('Importe Extra: {:0.2f}'.format(personal.getImporteExtra()))
                    total += personal.getImporteExtra()
                    band = True
        if band:
            print('El total de dinero que la Secretaría de Investigación debe solicitar al Ministerio es: {}'.format(total))
        else:
            print('No hay informacion de Docentes Investigador con esa categoria.')

    def mostrarDatos(self):
        for personal in self.__agentes:
            print(personal)

    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            agentes = [personal.toJSON() for personal in self.__agentes]
            )
        return d

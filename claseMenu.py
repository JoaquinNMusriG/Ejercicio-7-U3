class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 0:self.salir,
                            1:self.insertarPersonalPos,
                            2:self.agregarPersonal,
                            3:self.tipoPersonalPos,
                            4:self.carreraDocInvest,
                            5:self.area_DocInvest_Invest,
                            6:self.listarPersonal,
                            7:self.categImporte,
                            8:self.almacenarPersonal,
                         }
    def getSwitcher(self):
        return self.__switcher
    def opcion(self, op, jsonF, agentes):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func(jsonF, agentes)
    def salir(self, jsonF, agentes):
        print('Salir')

    def insertarPersonalPos(self, jsonF, agentes):
        pos = input('Ingrese la posicion en la que quiere insertar el personal: ')
        try:
            pos = int(pos)
            agentes.insertarPers(pos)
        except ValueError:
            print('Posicion inválida.')

    def agregarPersonal(self, jsonF, agentes):
        agentes.agregarPersonalFinal()

    def tipoPersonalPos(self, jsonF, agentes):
        pos = input('Ingrese la posicion de la que quiere saber el tipo de personal almacenado en ella: ')
        try:
            pos = int(pos)
            agentes.tipoPers(pos)
        except ValueError:
            print('Posicion inválida.')

    def carreraDocInvest(self, jsonF, agentes):
        carrera = input('Ingrese la carrera a buscar agentes: ')
        agentes.buscCarrera_mostrarPers(carrera.lower())

    def area_DocInvest_Invest(self, jsonF, agentes):
        area = input('Ingrese el area de investigacion de la que quiere contar a los Docente Investigador e Investigadores: ')
        agentes.contar_DocInvest_Invest(area.lower())

    def listarPersonal(self, jsonF, agentes):
        agentes.mostrarPersonal()

    def categImporte(self, jsonF, agentes):
        categoria = input('Ingrese la categoria de investigacion para listar personal y mostrar total de importe extra(I,II,III,IV,V): ')
        if (categoria.upper() == 'I') or (categoria.upper() == 'II') or (categoria.upper() == 'II') or (categoria.upper() == 'IV') or (categoria.upper() == 'V'):
            agentes.buscC_listarP(categoria.upper())
        else:
            print('Categoria inválida.')

    def almacenarPersonal(self, jsonF, agentes):
        d = agentes.toJSON()
        jsonF.guardarJSONArchivo(d,'personal.json')
        print('Vehiculos almacenados.')

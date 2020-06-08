from claseManejaColeccion import ManejaColeccion
from claseObjectEncoder import ObjectEncoder
from claseMenu import Menu

if __name__ == '__main__':
    jsonF = ObjectEncoder()
    try:
        diccionario = jsonF.leerJSONArchivo('personal.json')
        agentes = jsonF.decodificarDiccionario(diccionario)
    except FileNotFoundError:
        agentes = ManejaColeccion()

    menu=Menu()
    salir = False
    while not salir:
        print("""
              0 Salir
              1 Insertar personal en una posicion.
              2 Agregar personal
              3 Por posicion mostrar tipo de personal
              4 Por nombre de carrera mostrar Docentes Investigador
              5 Por area de investigacion, cantidad de Docentes Investigador e Investigadores
              6 Listado de personal
              7 Por categoria de investigacion listar Docentes Investigadores y total de dinero en concepto de importe extra
              8 Almacenar personal en personal.json""")
        op = int(input('Ingrese una opcion: '))
        menu.opcion(op,jsonF,agentes)
        salir = op == 0

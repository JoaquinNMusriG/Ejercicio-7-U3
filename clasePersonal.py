class Personal:
    __Cuil = ''
    __Apellido = ''
    __Nombre = ''
    __SueldoBasico = 0.0
    __Antiguedad = 0

    def __init__ (self, cuil, apellido, nombre, sueldoB, antiguedad):
        self.__Cuil = cuil
        self.__Apellido = apellido
        self.__Nombre = nombre
        self.__SueldoBasico = sueldoB
        self.__Antiguedad = antiguedad

    def __str__ (self):
        return 'Cuil = {} Apellido = {} Nombre = {} Sueldo Basico = {} Antiguedad = {}'.format(self.__Cuil,self.__Apellido,self.__Nombre,self.__SueldoBasico,self.__Antiguedad)    

    def getNombre(self):
        return self.__Nombre

    def getApellido(self):
        return self.__Apellido

    def getCuil(self):
        return self.__Cuil

    def getSueldoBasico(self):
        return self.__SueldoBasico

    def getAntiguedad(self):
        return self.__Antiguedad

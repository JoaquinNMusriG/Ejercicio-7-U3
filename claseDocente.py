from clasePersonal import Personal

class Docente(Personal):
    __Carrera = ''
    __Cargo = ''
    __Catedra = ''

    def __init__(self, **kwargs):
        self.__Carrera = kwargs.pop("carrera")
        self.__Cargo = kwargs.pop("cargo")
        self.__Catedra = kwargs.pop("catedra")
        super().__init__(**kwargs)

    def __str__(self):
        print(super().__str__())
        return 'Carrera = {} Cargo = {} Catedra = {}'.format(self.__Carrera,self.__Cargo,self.__Catedra)

    def getCarrera(self):
        return self.__Carrera

    def getCargo(self):
        return self.__Cargo

    def getCatedra(self):
        return self.__Catedra

    def calcularSueldo(self):
        sueldo = self.getSueldoBasico()
        if self.__Cargo == "simple":
            sueldo += sueldo*0.1
        elif self.__Cargo == "semiexclusivo":
            sueldo += sueldo*0.2
        else:
            sueldo += sueldo*0.5
        sueldo += self.getSueldoBasico()*(self.getAntiguedad()*0.01)
        return sueldo

    def toJSON(self):
        d = dict(
                __class__ = self.__class__.__name__,
                __atributos__ = dict(
                            cuil = self.getCuil(),
                            apellido = self.getApellido(),
                            nombre = self.getNombre(),
                            sueldoB = self.getSueldoBasico(),
                            antiguedad = self.getAntiguedad(),
                            carrera = self.__Carrera,
                            cargo = self.__Cargo,
                            catedra = self.__Catedra
            )
        )
        return d

from clasePersonal import Personal

class Investigador(Personal):
    __AreaInvestigacion = ''
    __TipoInvestigacion = ''

    def __init__(self, **kwargs):
        self.__AreaInvestigacion = kwargs.pop("areainv")
        self.__TipoInvestigacion = kwargs.pop("tipoinv")
        super().__init__(**kwargs)

    def __str__(self):
        print(super().__str__())
        return 'Area de Investigación = {} Tipo de Investigación = {}'.format(self.__AreaInvestigacion,self.__TipoInvestigacion)     

    def getAreaInvestigacion(self):
        return self.__AreaInvestigacion

    def getTipoInvestigacion(self):
        return self.__TipoInvestigacion

    def calcularSueldo(self):
        return self.getSueldoBasico()+(self.getSueldoBasico()*(self.getAntiguedad()*0.01))

    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                            cuil = self.getCuil(),
                            apellido = self.getApellido(),
                            nombre = self.getNombre(),
                            sueldoB = self.getSueldoBasico(),
                            antiguedad = self.getAntiguedad(),
                            areainv = self.__AreaInvestigacion,
                            tipoinv = self.__TipoInvestigacion
            )
        )
        return d

from claseDocente import Docente
from claseInvestigador import Investigador

class DocenteInvestigador(Docente, Investigador):
    __CategoriaIncentivo = ''
    __ImporteExtra = 0.0

    def __init__(self,**kwargs):
        self.__CategoriaIncentivo = kwargs.pop("categincent")
        self.__ImporteExtra = kwargs.pop("impextra")
        super().__init__(**kwargs)

    def __str__(self):
        print(super().__str__())
        return 'Categoria del Incentivo = {} Importe Extra = {}'.format(self.__CategoriaIncentivo,self.__ImporteExtra)     

    def getCategoriaIncentivo(self):
        return self.__CategoriaIncentivo

    def getImporteExtra(self):
        return self.__ImporteExtra

    def calcularSueldo(self):
        return  Docente.calcularSueldo(self) + self.__ImporteExtra

    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                            cuil = self.getCuil(),
                            apellido = self.getApellido(),
                            nombre = self.getNombre(),
                            sueldoB = self.getSueldoBasico(),
                            antiguedad = self.getAntiguedad(),
                            areainv = self.getAreaInvestigacion(),
                            tipoinv = self.getTipoInvestigacion(),
                            carrera = self.getCarrera(),
                            cargo = self.getCargo(),
                            catedra = self.getCatedra(),
                            impextra = self.__ImporteExtra,
                            categincent = self.__CategoriaIncentivo,
            )
        )
        return d

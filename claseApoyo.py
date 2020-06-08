from clasePersonal import Personal

class Apoyo(Personal):
    __Categoria = 0

    def __init__(self, cuil, apellido, nombre, sueldoB, antiguedad, categoria):
        super().__init__(cuil, apellido, nombre, sueldoB, antiguedad)
        self.__Categoria = categoria

    def __str__(self):
        print(super().__str__())
        return 'Categoria = {}'.format(self.__Categoria)    

    def getCategoria(self):
        return self.__Categoria

    def calcularSueldo(self):
        sueldo = self.getSueldoBasico()
        if self.__Categoria <= 10:
            sueldo += sueldo * 0.1
        elif self.__Categoria <= 20:
            sueldo += sueldo * 0.2
        else:
            sueldo += sueldo * 0.3
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
                        categoria = self.__Categoria
                            )
            )
        return d

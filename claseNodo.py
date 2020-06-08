class Nodo:
    __personal=None
    __siguiente=None

    def __init__(self, personal):
        self.__personal = personal
        self.__siguiente = None

    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente

    def setPersonal(self, personal):
        self.__personal = personal

    def getSiguiente(self):
        return self.__siguiente

    def getPersonal(self):
        return self.__personal

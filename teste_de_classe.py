class Materia:
    def __init__(self):
        self.__name = None
        self.__sem = None
        self.__n1 = -1.0
        self.__n2 = -1.0
        self.__n3 = -1.0
        self.__n4 = -1.0
        self.__sim = -1.0
        self.__md1 = -1.0
        self.__md2 = -1.0
        self.__md3 = -1.0
        self.__md4 = -1.0
        self.__mdf = -1.0
        self.__pdam = -1.0
        self.__tipo = False
        self.__sitmat = 'À cursar'
        self.__sital = 'Indefinida'

    @staticmethod
    def linhas(msg: str, cima: int, baixo: int):
        msg1 = msg
        cm = cima
        bx = baixo
        tam = len(msg1)

    def setname(self, name: str):
        if name is str(name):
            if name != '':
                self.__name = name

    def setsem(self, semestre: str):
        if semestre is str(semestre):
            sem = semestre
            try:
                sem1 = int(sem)
            except (ValueError, TypeError):
                print('Informe um parâmetro válido para o semestre!')
            else:
                if 1 <= sem1 <= 6:
                    self.__sem = sem1
                else:
                    print('Informe um valor entre 1 e 6 como parâmetro para o semestre!')

    def getname(self):
        return self.__name

    def getsemestre(self):
        return self.__sem


x = Materia()
x.setname("klj")


x.setsem('5')
print(x.getname(), x.getsemestre())

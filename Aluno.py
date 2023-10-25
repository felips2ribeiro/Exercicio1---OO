from Pessoa import Pessoa
from Turma import Turma
from Curso import Curso

class Aluno(Pessoa):
    def __init__(self):
        super().__init__()
        self.__Turma = Turma()
        self.__Curso = Curso()

    def getTurma(self):
        return self.__Turma

    def setTurma(self, Turma):
        self.__Turma = Turma

    def getCurso(self):
        return self.__Curso

    def setCurso(self, Curso):
        self.__Curso = Curso



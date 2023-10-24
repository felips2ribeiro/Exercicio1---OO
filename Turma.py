from Professor import Professor
from Curso import Curso
from Disciplina import Disciplina

class Turma:
    def __init__(self):
        self.__nome = ""
        self.__alunos = []
        self.__Professor = Professor()
        self.__Curso = Curso()
        self.__Disciplina = Disciplina()

    def getNome(self):
            return self.__nome

    def setNome(self, nome):
            self.__nome = nome

    def addAlunos(self, alunos):
        self.__alunos.append(alunos)

    def removeAlunos(self, alunos):
        self.__alunos.remove(alunos)

    def getAlunos(self):
        return self.__alunos

    def setProfessor(self, Professor):
        self.__Professor = Professor

    def getProfesser(self):
        return self.__Professor

    def setCurso(self, Curso):
        self.__Curso = Curso

    def getCurso(self):
        return self.__Curso

    def getDisciplina(self):
        return self.__Disciplina

    def setDisciplina(self, Disciplina):
        self.__Disciplina = Disciplina

    def toString(self):
        string = "Alunos: "
        for i in self.__alunos:
            string += f"{i}"
        return print(f"Turma: {self.getNome()}\nProfessor: {self.getProfesser()}\n{string}\nCurso: {self.getCurso()}\nDisciplina: {self.getDisciplina()}")

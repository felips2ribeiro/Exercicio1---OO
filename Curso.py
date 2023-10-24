class Curso:
    def __init__(self):
        self.__alunos = []
        self.__turmas = []

    def addAlunos(self, alunos):
        self.__alunos.append(alunos)

    def removeAlunos(self, alunos):
        self.__alunos.remove(alunos)

    def addTurmas(self, turmas):
        self.__turmas.append(turmas)

    def removeTurmas(self, turmas):
        self.__turmas.remove(turmas)


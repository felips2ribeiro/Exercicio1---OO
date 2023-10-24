class Disciplina:
    def __init__(self):
        self.__turmas = []

    def addTurmas(self, turmas):
        self.__turmas.append(turmas)

    def removeTurmas(self, turmas):
        self.__turmas.remove(turmas)
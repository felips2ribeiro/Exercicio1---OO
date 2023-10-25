class Disciplina:
    def __init__(self):
        self.__nome = ""
        self.__turmas = []

    def getNome(self):
            return self.__nome

    def setNome(self, nome):
            self.__nome = nome

    def addTurmas(self, turmas):
        self.__turmas.append(turmas)

    def removeTurmas(self, turmas):
        self.__turmas.remove(turmas)

    def imprimirTurmas(self):
        return ", ".join(turma.getNome() for turma in self.__turmas)

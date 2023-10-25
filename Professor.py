from Pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self):
        super().__init__()
        self.__turmas = []

    def addTurmas(self, turmas):
        self.__turmas.append(turmas)

    def removeTurmas(self, turmas):
        self.__turmas.remove(turmas)

    def imprimirTurmas(self):
        return ", ".join(turma.getNome() for turma in self.__turmas)
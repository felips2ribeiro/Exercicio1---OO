from Pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self):
        super().__init__()
        self.__turmas = []

    def addTurmas(self, turmas):
        self.__turmas.append(turmas)

    def removeTurmas(self, turmas):
        self.__turmas.remove(turmas)

    def toString(self):
        string = "Turmas: "
        for i in self.__turmas:
            string += f"{i} |"
        return f"Professor: {self.getNome()}\n{string}"
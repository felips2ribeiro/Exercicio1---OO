class Curso:
    def __init__(self):
        self.__nome = ""
        self.__alunos = []
        self.__turmas = []

    def getNome(self):
            return self.__nome

    def setNome(self, nome):
            self.__nome = nome

    def addAlunos(self, alunos):
        self.__alunos.append(alunos)

    def removeAlunos(self, alunos):
        self.__alunos.remove(alunos)

    def addTurmas(self, turmas):
        self.__turmas.append(turmas)

    def imprimirAlunos(self):
        return ", ".join(aluno.getNome() for aluno in self.__alunos)

    def removeTurmas(self, turmas):
        self.__turmas.remove(turmas)
    def imprimirTurmas(self):
        string = ", ".join(turma.getNome() for turma in self.__turmas)
        return string

    def verificarAlunoNoCurso(self, nome_aluno):
        for aluno in self.__alunos:
            if aluno.getNome() == nome_aluno:
                return f"|{nome_aluno}| está matriculado no curso |{self.getNome()}|."
        return f"|{nome_aluno}| não está matriculado no curso |{self.getNome()}|."


    def verificarTurmaNoCurso(self, nome_da_turma):
        for turma in self.__turmas:
            if turma.getNome() == nome_da_turma:
                return f"|{nome_da_turma}| pertence ao curso |{self.getNome()}|."
        return f"|{nome_da_turma}| não pertence ao curso |{self.getNome()}|."

    def removeTurmaDoCurso(self, nome_da_turma):
        for turma in self.__turmas:
            if turma.getNome() == nome_da_turma:
                self.__turmas.remove(turma)
                return f"|{nome_da_turma}| foi removido do curso |{self.getNome()}|."
            return f"|{nome_da_turma}| não pertence ao curso |{self.getNome()}|."

    def removeAlunoDoCurso(self, nome_aluno):
        for aluno in self.__alunos:
            if aluno.getNome() == nome_aluno:
                self.__alunos.remove(aluno)
                return f"|{nome_aluno}| foi removido do curso |{self.getNome()}|."
            return f"|{nome_aluno}| não está matriculado ao curso |{self.getNome()}|."
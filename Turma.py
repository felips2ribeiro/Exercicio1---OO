from Professor import Professor
from Curso import Curso
from Disciplina import Disciplina

class Turma:
    def __init__(self):
        self.__nome = ""
        self.__alunos = []
        self.__Professor = Professor()
        self.__Curso = Curso()
        self.__disciplinas = []

    def getNome(self):
            return self.__nome

    def setNome(self, nome):
            self.__nome = nome

    def addAlunos(self, nome_aluno):
        self.__alunos.append(nome_aluno)

    def removeAlunoDaTurma(self, nome_aluno):
        for aluno in self.__alunos:
            if aluno.getNome() == nome_aluno:
                self.__alunos.remove(aluno)
                return f"|{nome_aluno}| foi removido da turma |{self.getNome()}|."
            return f"|{nome_aluno}| não está matriculado na turma |{self.getNome()}|."



    def imprimirAlunos(self):
        return ", ".join(aluno.getNome() for aluno in self.__alunos)

    def setProfessor(self, Professor):
        self.__Professor = Professor

    def getProfessor(self):
        return self.__Professor

    def setCurso(self, Curso):
        self.__Curso = Curso

    def getCurso(self):
        return self.__Curso

    def addDisciplina(self, disciplinas):
        self.__disciplinas.append(disciplinas)

    def removeDisciplina(self, disciplinas):
        self.__disciplinas.remove(disciplinas)

    def imprimirDisciplinas(self):
        return ", ".join(disciplinas.getNome() for disciplinas in self.__disciplinas)

    def verificarAlunoNaTurma(self, nome_aluno):
        for aluno in self.__alunos:
            if aluno.getNome() == nome_aluno:
                return f"|{nome_aluno}| está matriculado na turma |{self.getNome()}|."
        return f"|{nome_aluno}| não está matriculado na turma |{self.getNome()}|."

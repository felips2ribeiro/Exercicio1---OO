from Aluno import Aluno
from Curso import Curso
from Disciplina import Disciplina
from Pessoa import Pessoa
from Professor import Professor
from Turma import Turma

def main():
    curso1 = Curso()
    curso2 = Curso()
    aluno1 = Aluno()
    aluno2 = Aluno()
    aluno3 = Aluno()
    aluno4 = Aluno()
    aluno5 = Aluno()
    aluno6 = Aluno()
    aluno7 = Aluno()
    aluno8 = Aluno()
    disciplina1 = Disciplina()
    disciplina2 = Disciplina()
    disciplina3 = Disciplina()
    disciplina4 = Disciplina()
    professor1 = Professor()
    professor2 = Professor()
    turma1 = Turma()
    turma2 = Turma()


    curso1.setNome('Engenharia de Software')
    curso1.addTurmas(turma1)
    curso1.addTurmas(turma2)
    curso1.addAlunos(aluno1)
    curso1.addAlunos(aluno2)
    curso1.addAlunos(aluno6)
    curso1.addAlunos(aluno8)


    curso2.setNome('Sistemas de Informação')
    curso2.addTurmas(turma1)
    curso2.addTurmas(turma2)
    curso2.addAlunos(aluno3)
    curso2.addAlunos(aluno4)
    curso2.addAlunos(aluno5)
    curso2.addAlunos(aluno7)

    aluno1.setNome('Felipe')
    aluno2.setNome('Gabriel')
    aluno3.setNome('Pedro')
    aluno4.setNome('Vitor')
    aluno5.setNome('Matheus')
    aluno6.setNome('Arthur')
    aluno7.setNome('João')
    aluno8.setNome('Augusto')


    disciplina1.setNome('Orientação a Objetos')
    disciplina2.setNome('Algoritmo')
    disciplina3.setNome('Desenvolvimento Web')
    disciplina4.setNome('Matemática')

    professor1.setNome('Marcos Miguel')
    professor1.addTurmas(turma1)
    professor2.addTurmas(turma2)

    professor2.setNome('Marco Antonio')
    professor2.addTurmas(turma1)
    professor2.addTurmas(turma2)


    turma1.setNome('2 Período')
    turma1.setCurso(curso1)
    turma1.setProfessor(professor1)
    turma1.addAlunos(aluno1)
    turma1.addAlunos(aluno2)
    turma1.addAlunos(aluno3)
    turma1.addAlunos(aluno4)

    turma2.setNome('1 Período')
    turma2.addDisciplina(disciplina1)
    turma2.addDisciplina(disciplina2)
    turma2.addDisciplina(disciplina3)
    turma2.addDisciplina(disciplina4)
    turma2.setCurso(curso2)
    turma2.setProfessor(professor2)
    turma2.setProfessor((professor1))




    print(f'1)Nome do professor da turma |{turma1.getNome()}|: {turma1.getProfessor().getNome()}.')
    print(f'2)Nome de todos os alunos da turma |{turma1.getNome()}|: {turma1.imprimirAlunos()}.')
    print(f'3)Nome dos professores que lecionam no curso |{curso2.getNome()}|: {professor1.getNome()}, {professor2.getNome()}.')
    print(f'4)Nome dos alunos que estão na turma |{turma1.getNome()}| do curso |{turma1.getCurso().getNome()}|: {turma1.imprimirAlunos()}.')
    print(f'5)Nome dos alunos registrados no curso |{curso2.getNome()}|: {curso2.imprimirAlunos()}.')
    print(f'6)As disciplinas que estão na turma |{turma2.getNome()}| do curso |{turma2.getCurso().getNome()}| são: {turma2.imprimirDisciplinas()}.')
    print(f'7)O aluno {turma1.verificarAlunoNaTurma("Gustavo")}')
    print(f'8)O aluno {curso2.verificarAlunoNoCurso("Vitor")}')
    print(f'9)A turma {curso2.verificarTurmaNoCurso("2 Período")}')
    print(f'10)O aluno {turma1.removeAlunoDaTurma("Felipe")}')
    print(f'11)A turma {curso2.removeTurmaDoCurso("2 Período")}')
    print(f'12)O aluno {curso2.removeAlunoDoCurso("Pedro")}')

if __name__ == "__main__":
    main()
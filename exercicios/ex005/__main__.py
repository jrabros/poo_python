from rich import print, inspect
from classesex005 import Aluno, Professor, Funcionario

a1 = Aluno('João', 17, 'Informatica', 'T01')
inspect(a1, methods=True)

p1 = Professor('José', 31, 'Biologia', 'Mestre')

p1.fazer_aniversario()
inspect(p1, methods=True)
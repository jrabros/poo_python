from rich import print, inspect
from aluno import Aluno
from professor import Professor
from funcionario import Funcionario

def main():
    a1 = Aluno('João', 17, 'Informatica', 'T01')
    inspect(a1, methods=True)

    p1 = Professor('José', 31, 'Biologia', 'Mestre')

    p1.fazer_aniversario()
    inspect(p1, methods=True)

if __name__ == '__main__':
    main()
from ex033 import *

def main():
    a = Aluno('Joao', 1999, 'ADM')

    a.add_curso('JOTA')
    print(a.cursos_oficiais)

if __name__ == '__main__':
    main()
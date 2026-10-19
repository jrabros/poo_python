from ex010 import Avaliacao
from rich import print, inspect

def main():
    av1 = Avaliacao('João', 'Matemática')
    av1.nota = 3.5
    print(av1.nota)
    inspect(av1, private=True)

if __name__ == '__main__':
    main()
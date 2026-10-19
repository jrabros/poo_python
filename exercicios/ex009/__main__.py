from ex009 import Avaliacao
from rich import print, inspect

def main():
    av1 = Avaliacao('João', 'Matemática')
    av1.set_nota(4.8)
    inspect(av1, private=True)

if __name__ == '__main__':
    main()
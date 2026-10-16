
from cafeteira import *
from rich import print
from rich import inspect

def main():
    bebida = Leite()
    # inspect(bebida, methods=True)
    bebida.preparar()

if __name__ == '__main__':
    main()

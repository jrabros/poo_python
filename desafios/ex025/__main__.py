from transporte import *
from rich import print

def main():
    dist = 10

    entrega = Moto(dist)
    print(f'O frete de {type(entrega).__name__} em {entrega.calc_frete()}km = {entrega.calc_frete()}')

if __name__ == '__main__':
    main()

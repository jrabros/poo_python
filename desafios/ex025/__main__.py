from transporte import *
from rich import print

def main():
    dist = 51

    entrega = Caminhao(dist)
    print(f'O frete de {type(entrega).__name__} em {dist}km = {entrega.calc_frete()}')

if __name__ == '__main__':
    main()

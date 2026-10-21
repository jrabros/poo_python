from classes import *

def main():
    p1 = Produto('Caminhão', 17)
    p2 = Produto('Vans', 11)

    c1 = Carrinho()

    c1 = c1 + p1 + p2

    print(c1)

if __name__ == '__main__':
    main()
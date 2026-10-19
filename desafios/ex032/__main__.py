from classes032 import *


def main():
    cc = ContaBancaria(000, 'Jão', 10_000, 'Senha123')

    cc.sacar(1400)
    print(cc)
    
if __name__ == '__main__':
    main()
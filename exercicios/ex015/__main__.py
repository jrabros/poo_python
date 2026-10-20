from classes import *

def main():
    c1 = Carteira(100)
    c2 = Carteira(300)

    c1 += 200

    print(c1 == c2)



if __name__ == '__main__':
    main()
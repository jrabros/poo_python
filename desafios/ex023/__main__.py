from poligono import *
from rich import print

def main():
    v1 = Circulo(13)

    print(f'O valor da area é {v1.area():.1f}m²')
    print(f'O valor do perimetro é {v1.perimetro():.1f}m')

if __name__ == '__main__':
    main()
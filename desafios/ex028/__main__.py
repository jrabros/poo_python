from termostato import Termostato
from rich import inspect, print

def main():
    t = Termostato()
    try:
        t.temperatura = 18.5
    except Exception as e:
        print(f'Houve um problema: {e}')

    print(t.temperatura) 
    inspect(t, private=True, methods=True)


if __name__ == '__main__':
    main()
from classes030 import Credencial

def main():
    c = Credencial()
    c.senha = str(input('Qual sua senha? '))
    print(c.senha)

    c.validar('Senha')

if __name__ == '__main__':
    main()
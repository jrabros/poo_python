from rich import print

class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentar(self):
        print(f'Olá, sou [blue]{self.nome}[/] do setor {self.setor} e sou {self.cargo} na empresa Mallon')

c1 = Funcionario('João', 'TI', 'Programador')
c1.apresentar()
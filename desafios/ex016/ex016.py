from rich import print
from rich import inspect

class Funcionario:
    # Atributos de Classe
    empresa = 'Mallon'

    def __init__(self, nome, setor, cargo):
        # Atributos de Instância
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentar(self) -> str:
        return f":handshake: Olá, sou [blue]{self.nome}[/] do setor {self.setor} e sou {self.cargo} na empresa {self.__class__.empresa}"

c1 = Funcionario('João', 'TI', 'Programador')
print(c1.apresentar())
# inspect(c1, methods=True)
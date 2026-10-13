from rich import print
from rich.panel import Panel

class Produto:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f'{self.nome} custa R${self.preco:,.2f}'

    def etiqueta(self):
        content = f'{self.nome.center(30, ' ')}'
        content += f'{'-' * 30}'
        precof = f'R${self.preco:,.2f}'
        content += f'{precof.center(30,'.')}'
        etiqueta = Panel(content, title='Produto', width=34)
        print(etiqueta)

p1 = Produto('Iphone 17 Pro Max', 25_000.85)
p1.etiqueta()

p2 = Produto('Notebook Games', 8000)
p2.etiqueta()
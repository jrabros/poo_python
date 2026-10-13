from rich.panel import Panel
from rich import print

class Churrasco:
    consumo_padrao:float = 0.4
    preco_padrao:float = 82.40


    def __init__(self, titulo = '', quantidade = 0):
        self.titulo = titulo
        self.qntd = quantidade


    def calcular_qtd_carne(self):
        return self.qntd * __class__.consumo_padrao


    def calcular_custo_total(self):
        return self.calcular_qtd_carne() * __class__.preco_padrao


    def calcular_preco_individual(self):
        return self.calcular_custo_total() / self.qntd

    def analisar(self):
        content = f'Analisando [green]{self.titulo}[/] com [blue]{self.qntd} convidados[/]'
        content += f'\nCada membro comerá {__class__.consumo_padrao}kg e cada Kg custa R${__class__.preco_padrao:.2f}'
        content += f'\nRecomendo comprar {self.calcular_qtd_carne():.3f}Kg de carne'
        content += f'\nO custo total será de R${self.calcular_custo_total():,.2f}'
        content += f'\nCada membro pagará R${self.calcular_preco_individual():,.2f} para partipar.'
        analise = Panel(content, title= self.titulo, width=70)
        print(analise)

a1 = Churrasco('Churras Badass', 5)
a1.analisar()

a2 = Churrasco('Churrasco Badass', 11)
a2.analisar()
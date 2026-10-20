class Mãe:
    def __init__(self, nome:str = 'Mamãe'):
        self.nome = nome
        
    def fazer_pudim(self):
        print(f'{self.nome} faz PDUIM com leite condensado e calda')

    def fritar_coxinha(self):
        print(f'{self.nome} frita COXINHA no óleo de soja')


class Filha(Mãe):
    def fazer_pudim(self): #OVERRIDE
        print(f'{self.nome} faz PUDIM com leite ninho com Nutela')


class Filho(Mãe):
    def fritar_coxinha(self): #OVERRIDE
        print(f'{self.nome} frita COXINHA na Air Fryer')
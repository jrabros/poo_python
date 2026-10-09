#Declaração de CLasse
class Jão():
    def __init__(self, nome = '', idade = 0): #Método construtor
        #Atributos de Instância
        self.nome = nome
        self.idade = idade

    #Métodos de Instância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f'{self.nome} é Parceiro(a) e tem {self.idade} anos de idade'

    def __str__(self): # Dunder Method
        return f'{self.nome} é Parceiro(a) e tem {self.idade} anos de idade'

    def __getstate__(self):
        return f'Estado: nome = {self.nome} : idade = {self.idade}'
# Declaração de Objetos

g1 = Jão('João', 26)
g1.aniversario()
g2 = Jão('Luiz', 51)

# print(g1.__doc__) # Dunder A
# print(g1)
print(g1.__dict__) # Attribute
print(g1.__getstate__()) # Method
print(g1.__class__)
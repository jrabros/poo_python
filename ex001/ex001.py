#Declaração de CLasse
class Jão():
    def __init__(self): #Método construtor
        #Atributos de Instância
        self.nome = ""
        self.idade = 0

    #Métodos de Instância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f'{self.nome} é Parceiro(a) e tem {self.idade} anos de idade'
# Declaração de Objetos

g1 = Jão()
g1.nome = 'João'
g1.idade = 26
print(g1.mensagem())
g1.aniversario()
print(g1.mensagem())

g2 = Jão()
g2.nome = 'Luiz'
g2.idade = 51
print(g2.mensagem())
from abc import ABC, abstractmethod

class Cafeteira(ABC):
    def preparar(self):
        step = 'INICIANDO PROCESSO'
        step += f'\n1. {self.ferver_agua()}'
        step += f'\n2. {self.misturar()}'
        step += f'\n3. {self.servir()}'
        step += '\nBEBIDA PRONTA!!'
        print (step)
    
    def ferver_agua(self):
        return f'Fervendo água a 100 graus'

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass


class Cafe(Cafeteira):
    def misturar(self):
        return f'Passando água pressurizada pelo pó de café moído.'

    def servir(self):
        return f'Servindo em xícara pequena.'


class Cha(Cafeteira):
    def misturar(self):
        return f'Mergulhando o sachê de ervas na água.'

    def servir(self):
        return f'Servindo na canela de porelana com limão.'


class Leite(Cafeteira):
    def misturar(self):
        return f'Passando vapor pressurizado pelo bico do leite.'

    def servir(self):
        return f'Servindo na canela grande, já com café.'    
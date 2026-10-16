from abc import ABC, abstractmethod

class Transporte(ABC):

    def __init__(self, distance):
        self.distance = distance
        self.frete = 0

    @abstractmethod
    def calc_frete(self):
        pass


class Moto(Transporte):
    fator = 0.5

    def __init__(self, distance):
        super().__init__(distance)

    def calc_frete(self):
        self.frete = self.distance * __class__.fator
        return f'R${self.frete:,.2f}'


class Caminhao(Transporte):
    fator = 1.2

    def __init__(self, distance):
        super().__init__(distance)

    def calc_frete(self):
        if self.distance < 50:
            return 'Não será possível, distancia mínima de 50km'
        else:
            self.frete = self.distance * __class__.fator
            return f'R${self.frete:,.2f}'


class Drone(Transporte):    
    fator = 9.5

    def __init__(self, distance):
        super().__init__(distance)

    def calc_frete(self):
        if self.distance > 10:
            return 'Não será possível, distancia máxima de 10km'
        else:
            self.frete = self.distance * __class__.fator
            return f'R${self.frete:,.2f}'
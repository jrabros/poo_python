from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, distance):
        self.distance = distance

    @abstractmethod
    def calc_frete(self):
        pass


class Moto(Transporte):
    fator = 0.5
    def __init__(self, distance):
        super().__init__(distance)

    def calc_frete(self):
        frete = self.distance * __class__.fator
        return f'R${frete:,.2f}'
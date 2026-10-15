from abc import ABC, abstractmethod

class Poligono(ABC):
    def __init__(self, qtd_lados):
        self.qtd_lados = qtd_lados

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Quadrado(Poligono):
    def __init__(self,qtd_lados, lado):
        super().__init__(qtd_lados, lado)
        self.lado = lado

    def area(self):
        area = self.lado * (1/2)
        return area

    def perimetro(self):
        perimetro = self.lado * 4
        return perimetro
from abc import ABC, abstractmethod
from math import pi

class FormaGeometrica(ABC):
    def __init__(self, qtd_lados):
        self.qtd_lados = qtd_lados

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Quadrado(FormaGeometrica):
    def __init__(self, lado):
        super().__init__(qtd_lados = 4)
        self.lado = lado

    def area(self):
        area = self.lado ** 2
        return area

    def perimetro(self):
        perimetro = self.lado * 4
        return perimetro
    

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        super().__init__(qtd_lados= 1)
        self.raio = raio

    def area(self):
        area = pi * (self.raio ** 2)
        return area

    def perimetro(self):
        perimetro = 2 * pi * self.raio
        return perimetro

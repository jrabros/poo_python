class Termostato:

    def __init__(self):
        self.__temperatura = 24

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, value):
        if value % 0.5 != 0:
            raise ValueError(f'Temperatura inválida {value}. Use apenas valores com o passo 0.5')
        if value < 16:
            self.__temperatura = 16
        elif value > 30:
            self.__temperatura = 30
        else:
            self.__temperatura = value

    @property
    def ftemperatura(self):
        return f'{self.__temperatura}{chr(176)}C'
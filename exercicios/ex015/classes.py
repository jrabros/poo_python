from functools import singledispatchmethod

class Carteira:

    def __init__(self, saldo:int|float = 0):
        self.__saldo = saldo

    def __str__(self):
        return f'Você tem {self.__saldo:,.2f} na carteira'

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        raise PermissionError('Você não tem permissão para alterar o saldo deste jeito')

    def __eq__(self, outro):
        if self.__saldo == outro.__saldo:
            return True
        else:
            return False

    def __iadd__(self, valor: int|float):
        self.__saldo += valor
        return self
from abc import ABC, abstractmethod
import locale

class Pagamento(ABC):
    
    def __init__(self):
        self._valor = None

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor: float):
        if valor > 0:
            self._valor = valor
        else:
            raise ValueError(f'O pagamento só pode ser positivo')        

    @property
    def fvalor(self):
        # return f'R${self._valor:,.2f}'
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        return locale.currency(self._valor, grouping=True)

    @abstractmethod
    def pagar(self):
        pass


class Boleto(Pagamento):
    
    def pagar(self, valor):
        try:
            self.valor = valor
            # código para efetuar o pagamento
            return f'Pagamento de {self.fvalor} via {__class__.__name__} foi CONFIRMADO'
        except Exception as e:
            return f'Falha no pagamento de {self.fvalor} via {__class__.__name__}'


class Pix(Pagamento):
   
    def pagar(self, valor):
        try:
            self.valor = valor
            # código para efetuar o pagamento
            return f'Pagamento de {self.fvalor} via {__class__.__name__} foi CONFIRMADO'
        except Exception as e:
            return f'Falha no pagamento de {self.fvalor} via Pix'


class Credito(Pagamento):
    
    def pagar(self, valor):
        try:
            self.valor = valor
            # código para efetuar o pagamento
            return f'Pagamento de {self.fvalor} via {__class__.__name__} foi CONFIRMADO'
        except Exception as e:
            return f'Falha no pagamento de {self.fvalor} via {__class__.__name__}'


def finalizar_compra(tipo_pag: Pagamento, valor:float):
    print(tipo_pag.pagar(valor))
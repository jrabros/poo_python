from rich.panel import Panel
from rich import print


class Mensagem:
    def __init__(self, msg: str = '', tipo: str = 'aviso', icone: str =':speech_balloon:'):
        self._mensagem = msg
        self._tipo = tipo
        self._icon = icone

    def mostrar(self):
        msg = Panel(self._mensagem, title=f'{self._icon} {self._tipo.upper()} {self._icon}', style='#ffffff on #000000', width=50)
        print(msg)


class Alerta(Mensagem):
    def __init__(self, msg = ''):
        super().__init__(msg, 'alerta', ':warning:')

    def mostrar(self):
        msg = Panel(self._mensagem, title=f'{self._icon} {self._tipo.upper()} {self._icon}', style='#000000 on #fffc1b', width=50)
        print(msg)


class Erro(Mensagem):

    def __init__(self, msg = ''):
        super().__init__(msg, 'erro', ':prohibited:')

    def mostrar(self):
        msg = Panel(self._mensagem, title=f'{self._icon} {self._tipo.upper()} {self._icon}', style='#ffff00 on #880000', width=50)
        print(msg)
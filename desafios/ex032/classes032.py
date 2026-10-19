from hashlib import sha256

class ContaBancaria:
    """
Cria uma conta bancária e permite fazer saques e depósitos    
    """
    def __init__(self, id:int, nome:str, saldo = 0, chave:str = None):
        self._id = id # (#protegido)
        self._titular = nome # (# Protegido)
        self.__saldo = saldo # (- Privado)
        if chave is None:
            chave = self.pede_senha()
        self.__hash = sha256(chave.encode()).hexdigest()
        print(f"Conta {self._id} criada com sucesso. Saldo atual de R${self.__saldo:,.2f}")

    def pede_senha(self) -> str:
        from pwinput import pwinput

        while True:
            senha = str(pwinput('Senha: ')).strip()
            if len(senha) >= 6:
                break

        return senha

    def validar_senha(self, chave:str) -> bool:
        usuario = sha256(chave.encode()).hexdigest()
        if usuario == self.__hash:
            return True
        else:
            return False

    def __str__(self):
        return f'A conta {self._id} de {self._titular} tem R${self.__saldo:,.2f} de saldo'
        # return f'Estado atual da conta: {self.__dict__}'

    def depositar(self, valor):
        valor = abs(valor)
        self.__saldo += valor
        print(f"Depósito de R${valor:,.2f} autorizado na conta {self._id}")

    def sacar(self, valor:float, chave:str = None):
        valor = abs(valor)
        if chave is None:
            chave = self.pede_senha()

        if self.validar_senha(chave):
            if valor >= self.__saldo:
                print('Saque Negado')
            else:
                self.__saldo -= valor
                print(f"Saque de R${valor:,.2f} autorizado na conta {self._id}")
        else:
            print('Senha não confere, NÃO AUTORIZADO')
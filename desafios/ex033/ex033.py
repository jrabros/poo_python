from abc import ABC, abstractmethod
from datetime import date

class Pessoa(ABC):

    def __init__(self, nome:str, ano_nasc:int):
        self._nome = nome
        self._nascimento = None
        self.nascimento = ano_nasc

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, ano):
        if 1900 <= ano <= date.today().year:
            self._nascimento = ano
        else:
            raise ValueError(f'Ano {ano} é inválido')

    @property
    def idade(self):
        return date.today().year - self.nascimento

    @idade.setter
    def idade(self):
        raise PermissionError('Você não pode mudar a idade. Mude o ano de nascimento')


class Aluno(Pessoa):

    cursos_oficiais = ['ADM', 'ENG']

    def __init__(self, nome:str, ano_nasc:int, curso:str):
        super().__init__(nome, ano_nasc)
        self._curso = None
        self.curso = curso

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, curso):
        if curso in Aluno.cursos_oficiais:
            self._curso = curso
        else:
            self._curso = None
            raise ValueError(f'O curso {curso} não está na lista de curso oficiais')

    def add_curso(self, curso):
        curso = curso.strip().upper()

        if 3 <= len(curso) <=5:
            Aluno.cursos_oficiais.append(curso)
        else:
            raise ValueError(f'Nome {curso} está fora do padrão para Cursos')

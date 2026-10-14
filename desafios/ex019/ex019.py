from rich import print
from time import sleep
class Livro:

    def __init__(self, titulo, pages):
        self.titulo = titulo
        self.pages = pages
        self.page_atual = 1

        print(f':open_book: Você acabaou de abrir o livro [red]{self.titulo}[/] que tem {self.pages} págnias no total. Você agora está na página {self.page_atual}' )


    def __str__(self):
        return f'{self.titulo} com {self.pages} páginas'


    def avancar_paginas(self, num_pages = 1):
        for pg in range(0, num_pages, 1):
            if not self.fim_do_livro():
                self.page_atual += 1
                print(f'Pág{self.page_atual} :arrow_forward: ', end='')
                sleep(0.3)
        print(f'Você está agora está na página {self.page_atual}')
        if self.fim_do_livro():
            print(f':closed_book: Você chegou no final do livro!!')

    def fim_do_livro(self) -> bool:
        return True if self.page_atual == self.pages else False


l1 = Livro('Os Carecas', 25)
l1.avancar_paginas(5)
l1.avancar_paginas(21)
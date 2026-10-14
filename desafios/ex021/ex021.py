from rich.panel import Panel
from rich import print

class ControleRemoto:
    canal_max:int = 5
    canal_min:int = 1
    volume_max:int = 5
    volume_min:int = 1

    def __init__(self, canal = 1, volume = 1):
        self.canal = canal
        self.volume = volume
        self.ligada = False


    def liga_desliga(self):
        self.ligada = not self.ligada


    def aumentar_volume(self):
        if self.ligada:
            if __class__.volume_max > self.volume:
                self.volume += 1


    def diminuir_volume(self):
        if self.ligada:
            if __class__.volume_min < self.volume:
                self.volume -= 1


    def aumentar_canal(self):
        if self.ligada:
            if __class__.canal_max == self.canal:
                self.canal = __class__.canal_min
            else:
                self.canal += 1

    def diminuir_canal(self):
        if self.ligada:
            if __class__.canal_min == self.canal:
                self.canal = __class__.canal_max
            else:
                self.canal -= 1

    def mostrar_tv(self):
        content = ''
        if not self.ligada:
            content = f'TV DESLIGADA'
        else:
            content = f'\nCANAL = '
            for canal in range (__class__.canal_min, __class__.canal_max + 1):
                if canal == self.canal:
                    content += f'[on green] {canal} [/]'
                else:
                    content += f' {canal} '

            content += f'\nVOLUME = '
            for volume in range (__class__.volume_min, __class__.volume_max + 1):
                if volume <= self.volume:
                    content += f'[on red] [/]'
                else:
                    content += f'[on yellow] [/]'            
        tv = Panel(content, title='[ TV ]', width=30)
        print(tv)


c1 = ControleRemoto(1, 5)

while True:
    c1.mostrar_tv()
    comando = str(input(f'< CH >  - VOL + '))
    match comando:
        case '0':
            break
        case '@':
            c1.liga_desliga()
        case '<':
            c1.diminuir_canal()
        case '>':
            c1.aumentar_canal()
        case '+':
            c1.aumentar_volume()
        case '-':
            c1.diminuir_volume()
    print('\n' * 10)
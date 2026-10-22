import sqlite3
from datetime import date

busca = input('Quem você está procurando? ').strip()
hoje = date.today()

try:
    with sqlite3.connect('meubanco.db') as banco:
    # banco = sqlite3.connect('meubanco.db')
        banco.row_factory = sqlite3.Row # 
        cur = banco.cursor()
        cur.execute('select * from amigos WHERE nome LIKE ?', (f'%{busca}%',))
        # lista = cur.fetchall()
        # print(lista)

        total = 0
    for total, amigo in enumerate(cur, start=1):
        txtnasc = amigo['nascimento']
        if not txtnasc:
            info_nasc = 'sem data de nascimento'
        else:
            try:
                data = date.fromisoformat(str(txtnasc))

                japassou = (hoje.month, hoje.day) >= (data.month, data.day)

                if japassou:
                    idade = hoje.year - data.year
                else:
                    idade = hoje.year - data.year - 1

                info_nasc = f'nasceu em {data:%d/%m/%Y} e tem {idade} anos'
            except ValueError:
                info_nasc = f'data inválida'

        print(f"{amigo['nome']} {info_nasc}")

    if total == 0:
        print(f'Não econtrei ninguém com "{busca}" no nome')
    elif total == 1:
        print(f'Encontrei um amigo com "{busca}"')
    else:
        print(f'Ao todo encotrei {total} amigos com "{busca}"')

except sqlite3.Error as erro:
    print(f'Algo deu errado no banco {erro}')

except Exception as erro:
    print(f'Algo deu errado {erro}')
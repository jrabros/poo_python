import sqlite3

NOME_BANCO = "cadastro.db"

def criar_banco():
    try:
        with sqlite3.connect(NOME_BANCO) as db:
            cur = db.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS pessoas (cod INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, altura REAL NOT NULL);")
            db.commit()
            return True
    except sqlite3.Error as erro:
        print(f"Falha na criação no banco: {erro}")
        return False

def cadastro_em_massa():
    cad_pessoas = [
        ("1", "João", "1.81"),
        ("2", "Lucas", "1.87"),
        ("3", "Joana", "1.57"),
        ("4", "Luiz", "1.74"),
    ]

    try:
        with sqlite3.connect(NOME_BANCO) as db:
            cur = db.cursor()
            cur.executemany("INSERT INTO pessoas (cod, nome, altura) VALUES (?, ?, ?)", cad_pessoas)

    except sqlite3.Error as erro:
        print("Falha as fazer cadastro em massa")

def cadastrar_pessoas() -> bool:
    print("\nNOVO CADASTRO DE PESSOAS")

    #Leitura e validação do dados
    val_nome = input('Nome: ').strip()
    if not val_nome:
        print("[ERRO] O nome é um campo obrigatório")
        return False

    val_altura = input("Altura (metros): ").strip().replace(",",".")
    if not val_altura:
        print("[ERRO] A altura é um campo obrigatório!")
        return False

    try:
        altura = float(val_altura)
        if altura <= 0.30 or altura > 3.0:
            print("[ERRO] Valor incoerente para altura")
            return False
    except ValueError:
        print("[ERRO] A altura precisa ser um número.")
        return False
    
    try:
        with sqlite3.connect(NOME_BANCO) as db:
            cur = db.cursor()
            cur.execute("INSERT INTO pessoas (nome, altura) VALUES (?, ?)", (val_nome, val_altura))
            print(f"Cadastro de {val_nome} realizado com SUCESSO!")
            return True
    except sqlite3.Error as erro:
        print(f"[ERRO] Falha no cadastro no banco {erro}")
        return False

    
def listar_pessoas() -> bool:
    try:
        with sqlite3.connect(NOME_BANCO) as db:
            cur = db.cursor()
            cur.execute("SELECT cod, nome, altura FROM pessoas ORDER BY nome;")
            primeiro = cur.fetchone()
            if not primeiro:
                print("AVISO: NENHUM CADASTRO")
                return True
            print(f"\n" + '=' * 45)
            print(f"{'CÓD':<6} {'NOME':<28} {'ALTURA':>8}")
            print(f"-" * 45)

            vcod, vnome, valtura = primeiro
            print(f"{vcod:<6} {vnome:<28} {valtura:>8}m")

            for vcod, vnome, valtura in cur:
                print(f"{vcod:<6} {vnome:<28} {valtura:>8}m")

            print(f"\n" + '=' * 45)

            return True
    except sqlite3.Error as erro:
        print(f'[ERRO] falha ao acessar o banco: {erro}')
        return False


def atualizar_pessoa() -> bool:
    pass


def excluir_pessoa() -> bool:
    #Listar todos
    listar_pessoas()
    #Perguntar o id da exclusão
    entrada_cod = input(f"Informe o cód da pessoa a excluir: ").strip()
    if not entrada_cod.isdigit():
        print("ERRO - Cód inválido")
        return False
    #Buscar se pessoa existe
    #Mostrar os dados da pessoa
    #Pedir confirmação
    vcod = int(entrada_cod)
    try:
        with sqlite3.connect(NOME_BANCO) as db:
            cur = db.cursor()
            cur.execute("SELECT nome, altura FROM pessoas WHERE cod = ?", (vcod,))
            pessoa = cur.fetchone()

            if not pessoa:
                print(f"[ERRO] Pessoa com cód {vcod} não encontrada")
                return False

            vnome, valtura = pessoa
            print(f"\nEncontrei o registro {vnome} com {valtura:.2f}m de altura.")

            conf = input("Tem certeza que desja excluir? [S/N] ").strip().upper()

            if conf != "S":
                print("[AVISO] Exclusão foi cancelada")
                return True

            cur.execute("DELETE FROM pessoas WHERE cod = ?", (vcod,))

            print(f"[AVISO] Acabei de excluir os dados de {vnome}")
            return True
        
    except sqlite3.Error as erro:
        print(f"[ERRO] Falha ao excluir: {erro}")
    

def buscar_pessoa_por_nome() -> bool:
    termo = input('Digite o nome (ou parte dele) para buscar: ')

    if not termo:
        print("[AVISO] Nenhum termo foi informado")
        return False

    try:
        with sqlite3.connect(NOME_BANCO) as db:
            cur = db.cursor()
            cur.execute("SELECT cod, nome, altura FROM pessoas WHERE nome LIKE ? ORDER BY nome;", (f"%{termo}%",))
            primeiro = cur.fetchone()
            if not primeiro:
                print(f"AVISO: NENHUM CADASTRO COM {termo}.")
                return True
            print(f"\n" + '=' * 45)
            print(f"{'CÓD':<6} {'NOME':<28} {'ALTURA':>8}")
            print(f"-" * 45)

            vcod, vnome, valtura = primeiro
            print(f"{vcod:<6} {vnome:<28} {valtura:>8}m")

            for vcod, vnome, valtura in cur:
                print(f"{vcod:<6} {vnome:<28} {valtura:>8}m")

            print(f"\n" + '=' * 45)

            return True
    except sqlite3.Error as erro:
        print(f'[ERRO] falha ao acessar o banco: {erro}')
        return False
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
    pass


def atualizar_pessoa() -> bool:
    pass


def excluir_pessoa() -> bool:
    pass


def buscar_pessoa_por_nome() -> bool:
    pass
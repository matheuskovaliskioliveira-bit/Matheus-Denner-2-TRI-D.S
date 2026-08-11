import sqlite3


conexao = sqlite3.connect("loja.db")
cursor = conexao.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    preco REAL NOT NULL
)
""")


cursor.execute("INSERT INTO produtos (nome, preco) VALUES (?, ?)", ("Notebook", 3500))
cursor.execute("INSERT INTO produtos (nome, preco) VALUES (?, ?)", ("Mouse", 80))
cursor.execute("INSERT INTO produtos (nome, preco) VALUES (?, ?)", ("Teclado", 150))


conexao.commit()


conexao.close()

print("Banco criado com sucesso!")
import sqlite3
from flask import Flask, jsonify

app = Flask(__name__)


def conectar():
    conexao = sqlite3.connect("banco.db")
    conexao.row_factory = sqlite3.Row
    return conexao


def criar_tabelas():
    conexao = conectar()

    conexao.execute("""
        CREATE TABLE IF NOT EXISTS autores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
        )
    """)

    conexao.execute("""
        CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor_id INTEGER,
            FOREIGN KEY (autor_id) REFERENCES autores(id)
        )
    """)

    conexao.commit()
    conexao.close()


criar_tabelas()


@app.route("/autores", methods=["POST"])
def criar_autor():
    pass


@app.route("/livros", methods=["POST"])
def criar_livro():
    pass


if __name__ == "__main__":
    app.run(debug=True)
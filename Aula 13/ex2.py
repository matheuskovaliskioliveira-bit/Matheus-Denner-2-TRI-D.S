import sqlite3
from flask import Flask, jsonify

app = Flask(__name__)


def conectar():
    conexao = sqlite3.connect("banco.db")
    conexao.row_factory = sqlite3.Row
    return conexao


@app.route("/livros-completo", methods=["GET"])
def livros_completo():
    conexao = conectar()

    cursor = conexao.execute("""
        SELECT livros.id,
               livros.titulo,
               autores.nome AS autor
        FROM livros
        JOIN autores ON livros.autor_id = autores.id
    """)

    resultado = [dict(livro) for livro in cursor.fetchall()]

    conexao.close()

    return jsonify(resultado)


if __name__ == "__main__":
    app.run(debug=True)
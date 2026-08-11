from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)


def banco():
    db = sqlite3.connect("biblioteca.db")
    db.row_factory = sqlite3.Row
    db.execute("PRAGMA foreign_keys = ON")
    return db


db = banco()

db.execute("""
CREATE TABLE IF NOT EXISTS autores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
)
""")

db.execute("""
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    ano INTEGER,
    autor_id INTEGER NOT NULL,
    FOREIGN KEY (autor_id) REFERENCES autores(id) ON DELETE CASCADE
)
""")

db.commit()
db.close()


@app.route("/autores", methods=["GET"])
def ver_autores():

    db = banco()

    resultado = db.execute(
        "SELECT * FROM autores"
    ).fetchall()

    db.close()

    lista = []

    for autor in resultado:
        lista.append(dict(autor))

    return jsonify(lista)


@app.route("/autores", methods=["POST"])
def adicionar_autor():

    dados = request.get_json()

    if dados is None or "nome" not in dados:
        return jsonify({
            "erro": "Nome obrigatorio"
        }), 400

    db = banco()

    comando = db.execute(
        "INSERT INTO autores (nome) VALUES (?)",
        (dados["nome"],)
    )

    db.commit()

    novo_id = comando.lastrowid

    db.close()

    return jsonify({
        "id": novo_id,
        "nome": dados["nome"]
    }), 201


@app.route("/autores/<int:id>", methods=["PUT"])
def mudar_autor(id):

    dados = request.get_json()

    if dados is None or "nome" not in dados:
        return jsonify({
            "erro": "Nome obrigatorio"
        }), 400

    db = banco()

    comando = db.execute(
        "UPDATE autores SET nome = ? WHERE id = ?",
        (dados["nome"], id)
    )

    db.commit()

    if comando.rowcount == 0:
        db.close()

        return jsonify({
            "erro": "Autor nao encontrado"
        }), 404

    db.close()

    return jsonify({
        "id": id,
        "nome": dados["nome"]
    })


@app.route("/autores/<int:id>", methods=["DELETE"])
def excluir_autor(id):

    db = banco()

    comando = db.execute(
        "DELETE FROM autores WHERE id = ?",
        (id,)
    )

    db.commit()

    if comando.rowcount == 0:
        db.close()

        return jsonify({
            "erro": "Autor nao encontrado"
        }), 404

    db.close()

    return jsonify({
        "mensagem": "Autor excluido"
    })



@app.route("/livros", methods=["GET"])
def ver_livros():

    db = banco()

    resultado = db.execute(
        "SELECT * FROM livros"
    ).fetchall()

    db.close()

    lista = []

    for livro in resultado:
        lista.append(dict(livro))

    return jsonify(lista)


@app.route("/livros", methods=["POST"])
def adicionar_livro():

    dados = request.get_json()

    if dados is None:
        return jsonify({
            "erro": "Dados obrigatorios"
        }), 400

    if "titulo" not in dados:
        return jsonify({
            "erro": "Titulo obrigatorio"
        }), 400

    if "autor_id" not in dados:
        return jsonify({
            "erro": "Autor obrigatorio"
        }), 400

    db = banco()

    autor = db.execute(
        "SELECT id FROM autores WHERE id = ?",
        (dados["autor_id"],)
    ).fetchone()

    if autor is None:
        db.close()

        return jsonify({
            "erro": "Autor nao existe"
        }), 400

    comando = db.execute(
        """
        INSERT INTO livros (titulo, ano, autor_id)
        VALUES (?, ?, ?)
        """,
        (
            dados["titulo"],
            dados.get("ano"),
            dados["autor_id"]
        )
    )

    db.commit()

    novo_id = comando.lastrowid

    db.close()

    return jsonify({
        "id": novo_id,
        "titulo": dados["titulo"],
        "ano": dados.get("ano"),
        "autor_id": dados["autor_id"]
    }), 201


@app.route("/livros/<int:id>", methods=["PUT"])
def mudar_livro(id):

    dados = request.get_json()

    if dados is None:
        return jsonify({
            "erro": "Dados obrigatorios"
        }), 400

    if "titulo" not in dados:
        return jsonify({
            "erro": "Titulo obrigatorio"
        }), 400

    if "autor_id" not in dados:
        return jsonify({
            "erro": "Autor obrigatorio"
        }), 400

    db = banco()

    autor = db.execute(
        "SELECT id FROM autores WHERE id = ?",
        (dados["autor_id"],)
    ).fetchone()

    if autor is None:
        db.close()

        return jsonify({
            "erro": "Autor nao existe"
        }), 400

    comando = db.execute(
        """
        UPDATE livros
        SET titulo = ?, ano = ?, autor_id = ?
        WHERE id = ?
        """,
        (
            dados["titulo"],
            dados.get("ano"),
            dados["autor_id"],
            id
        )
    )

    db.commit()

    if comando.rowcount == 0:
        db.close()

        return jsonify({
            "erro": "Livro nao encontrado"
        }), 404

    db.close()

    return jsonify({
        "id": id,
        "titulo": dados["titulo"],
        "ano": dados.get("ano"),
        "autor_id": dados["autor_id"]
    })


@app.route("/livros/<int:id>", methods=["DELETE"])
def excluir_livro(id):

    db = banco()

    comando = db.execute(
        "DELETE FROM livros WHERE id = ?",
        (id,)
    )

    db.commit()

    if comando.rowcount == 0:
        db.close()

        return jsonify({
            "erro": "Livro nao encontrado"
        }), 404

    db.close()

    return jsonify({
        "mensagem": "Livro excluido"
    })




@app.route("/livros/detalhes", methods=["GET"])
def detalhes():

    db = banco()

    resultado = db.execute("""
        SELECT
            livros.id,
            livros.titulo,
            livros.ano,
            autores.nome AS autor
        FROM livros
        INNER JOIN autores
        ON livros.autor_id = autores.id
    """).fetchall()

    db.close()

    lista = []

    for livro in resultado:
        lista.append(dict(livro))

    return jsonify(lista)



@app.route("/autores/<int:id>/livros", methods=["GET"])
def livros_do_autor(id):

    db = banco()

    autor = db.execute(
        "SELECT * FROM autores WHERE id = ?",
        (id,)
    ).fetchone()

    if autor is None:
        db.close()

        return jsonify({
            "erro": "Autor nao encontrado"
        }), 404

    resultado = db.execute(
        "SELECT * FROM livros WHERE autor_id = ?",
        (id,)
    ).fetchall()

    db.close()

    lista = []

    for livro in resultado:
        lista.append(dict(livro))

    return jsonify(lista)



@app.route("/livros/buscar", methods=["GET"])
def procurar():

    palavra = request.args.get("titulo")

    if palavra is None or palavra == "":
        return jsonify({
            "erro": "Digite um titulo"
        }), 400

    db = banco()

    resultado = db.execute(
        "SELECT * FROM livros WHERE titulo LIKE ?",
        ("%" + palavra + "%",)
    ).fetchall()

    db.close()

    lista = []

    for livro in resultado:
        lista.append(dict(livro))

    return jsonify(lista)


if __name__ == "__main__":
    app.run(debug=True)
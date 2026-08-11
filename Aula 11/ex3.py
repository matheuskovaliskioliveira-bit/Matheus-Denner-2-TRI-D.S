from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def conectar():
    return sqlite3.connect("loja.db")

conexao = conectar()
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL
)
""")

conexao.commit()
conexao.close()


@app.route("/produtos", methods=["GET"])
def listar_produtos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()

    lista = []

    for produto in produtos:
        lista.append({
            "id": produto[0],
            "nome": produto[1],
            "preco": produto[2]
        })

    conexao.close()

    return jsonify(lista)


@app.route("/produtos", methods=["POST"])
def criar_produto():
    dados = request.get_json()

    if "preco" not in dados:
        return jsonify({
            "erro": "O campo preco e obrigatorio"
        }), 400

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO produtos (nome, preco) VALUES (?, ?)",
        (dados["nome"], dados["preco"])
    )

    conexao.commit()

    conexao.close()

    return jsonify({
        "mensagem": "Produto cadastrado com sucesso"
    }), 201

app.run(debug=True)
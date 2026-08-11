from flask import Flask, jsonify, request

app = Flask(__name__)

produtos = [
    {"id": 1, "nome": "Notebook", "preco": 3500},
    {"id": 2, "nome": "Mouse", "preco": 80}
]

@app.route("/produtos", methods=["GET"])
def listar_produtos():
    return jsonify(produtos)

@app.route("/produtos", methods=["POST"])
def criar_produto():
    novo_produto = request.get_json()

    produtos.append(novo_produto)

    return jsonify({
        "mensagem": "Produto criado com sucesso",
        "produto": novo_produto
    }), 201

app.run(debug=True)
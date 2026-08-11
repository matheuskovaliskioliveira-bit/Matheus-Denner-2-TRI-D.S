from flask import Flask, jsonify

app = Flask(__name__)

produtos = [
    {"id": 1, "nome": "Notebook", "preco": 3500.00, "disponivel": True},
    {"id": 2, "nome": "Mouse", "preco": 80.00, "disponivel": True},
    {"id": 3, "nome": "Teclado", "preco": 150.00, "disponivel": False},
    {"id": 4, "nome": "Monitor", "preco": 1200.00, "disponivel": True}
]

@app.route("/produtos/<int:id>")
def buscar_produto(id):
    for produto in produtos:
        if produto["id"] == id:
            return jsonify(produto)

    return jsonify({"erro": "Produto nao encontrado"}), 404

app.run(debug=True)
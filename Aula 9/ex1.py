from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/produto")
def produto():
    return jsonify({
        "id": 1,
        "nome": "Notebook",
        "preco": 3500.00,
        "disponivel": True
    })

app.run(debug=True)
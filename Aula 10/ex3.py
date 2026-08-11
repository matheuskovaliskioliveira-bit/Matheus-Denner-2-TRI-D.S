from flask import Flask, jsonify, request

app = Flask(__name__)

tarefas = []

@app.route("/tarefas", methods=["GET"])
def listar_tarefas():
    return jsonify(tarefas)

@app.route("/tarefas", methods=["POST"])
def criar_tarefa():
    nova_tarefa = request.get_json()

    if "titulo" not in nova_tarefa or nova_tarefa["titulo"].strip() == "":
        return jsonify({
            "erro": "O titulo nao pode ser vazio"
        }), 400

    tarefas.append(nova_tarefa)

    return jsonify({
        "mensagem": "Tarefa criada com sucesso",
        "tarefa": nova_tarefa
    }), 201

app.run(debug=True)
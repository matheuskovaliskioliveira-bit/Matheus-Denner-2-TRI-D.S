from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Bem-vindo"

@app.route("/curso")
def curso():
    return "Análise e Desenvolvimento de Sistemas"  

@app.route("/escola")
def escola():
    return "Nome da sua escola" 

app.run()
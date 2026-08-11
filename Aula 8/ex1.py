from Flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Matheus Denner"  

app.run()
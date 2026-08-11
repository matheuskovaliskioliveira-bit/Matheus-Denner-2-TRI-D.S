from flask import Flask
from datetime import date

app = Flask(__name__)

@app.route("/saudacao")
def saudacao():
    return "Seja bem-vindo à nossa API!"

@app.route("/data")
def data():
    return f"Data de hoje: {date.today()}"

app.run()
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    title = "Home | Ufes"
    return render_template("home.html", title = title)

@app.route("/quem_somos")
def quem_somos():
    title = "Quem somos | Ufes"
    return render_template("quem_somos.html", title = title)

@app.route("/contato")
def contato():
    title = "Contato | Ufes"
    return render_template("contato.html", title = title)
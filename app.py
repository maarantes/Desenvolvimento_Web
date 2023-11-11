from flask import Flask, render_template, request, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy
import mysql

app = Flask("__name__")

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://admin:unes@localhost:3306/db_unes'
app.config['SECRET_KEY'] = "faculdade_unes"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class formulario(db.Model):
    __tablename__ = "formulario"
    id = db.Column('mensagem_id', db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(50), unique = True)  
    assunto = db.Column(db.String(200))
    mensagem = db.Column(db.String(2000))

def __init__(nome, email, assunto, mensagem):
    self.nome = nome
    self.email = email
    self.assunto = assunto
    self.mensagem = mensagem




@app.route("/")
def home():
    return render_template("home.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/formulario_post", methods = ['GET', 'POST'])
def formulario_post():
    if request.method == 'POST':

        nome = request.form['nome']
        email = request.form['email']
        assunto = request.form['assunto']
        mensagem = request.form['mensagem']

        if not nome or not email or not assunto or not mensagem:
            flash('Por favor, preencha todos os campos!')

        else:
            mensagem_form = formulario(nome=nome, email=email, assunto=assunto, mensagem=mensagem)
         
            db.session.add(mensagem_form)
            db.session.commit()
            flash('Mensagem enviada com sucesso!')

    return redirect(url_for("contato")) #Pra rota "formulario_post" não aparecer no link do site e sim o "contato"




if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)
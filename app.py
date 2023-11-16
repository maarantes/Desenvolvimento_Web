from flask import Flask, render_template, request, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
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
    assunto = db.Column(db.String(100))
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
            try:
                db.session.commit()
                flash('Mensagem enviada com sucesso!')
            except IntegrityError: # Se o e-mail já foi enviado antes,
                db.session.rollback() # cancelará o envio das informações
                flash('Este e-mail já está em uso!') # e avisará que o e-mail já está em uso

    return redirect(url_for("contato")) # Pra rota "formulario_post" não aparecer no link do site e sim o "contato"

@app.route("/admin")
def admin():
    mensagens = formulario.query.all()
    return render_template("admin.html", mensagens=mensagens, total_pendente=len(mensagens))

@app.route("/deletar_msg/<int:id>", methods=['POST'])
def deletar_msg(id):
    mensagem = formulario.query.get_or_404(id)
    db.session.delete(mensagem)
    db.session.commit()
    return redirect(url_for('admin'))



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)
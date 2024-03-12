from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/usuario/<nome>')
def usuario(nome):
    return render_template('usuario.html', nome=nome)

@app.route('/gastos', defaults={"mes": "Janeiro", "valor": "0"})
@app.route('/gastos/<mes>/<valor>')
def gastos(mes, valor):
    return render_template('gastos.html', a = mes, b = valor)

@app.route('/perfil/<nome>')
def perfil(nome):
    return render_template('perfil.html', nome=nome)

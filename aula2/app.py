# Aula 02 - Criando Rotas e configurações

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Index"


def teste():
    return "<p>testando 1</p>"


def teste2():
    return "<h1>testando 2</h1>"


app.add_url_rule("/teste", "teste", teste)
app.add_url_rule("/teste-2", "teste2", teste2)

if __name__ == '__main__':
    app.run(debug=True, port="3000")

# Aula 10 - Enviando dados para o template
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')


@app.route('/')
def notas():
    return render_template('notas.html')


@app.route('/calculo', methods=['POST'])
def calculo():
    total = sum([int(v) for v in request.form.to_dict().values()])
    return render_template('calculo.html', total=total)


if __name__ == '__main__':
    app.run(debug=True)

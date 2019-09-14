# Aula 05 - WEB Arquivos Estaticos

from flask import Flask

app = Flask(__name__, static_folder='public')

# code

if __name__ == '__main__':
    app.run(debug=True)

# Aula 16 - REST API parte 2
from flask import Flask
from aula16.models.models import db
from aula16.controllers.estudante import app as estudante_controller
from aula16.controllers.discplina import app as disciplina_controller

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///estudantes.sqlite3'

app.register_blueprint(estudante_controller, url_prefix="/estudante/")
app.register_blueprint(disciplina_controller, url_prefix="/disciplina/")

if __name__ == '__main__':
    db.init_app(app=app)
    with app.test_request_context():
        db.create_all()
    app.run(debug=True)

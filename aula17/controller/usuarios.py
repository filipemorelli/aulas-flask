from flask import Blueprint, Response, request
from ..model.model import db, Usuarios
import json

app = Blueprint("usuarios", __name__)


@app.route('/')
def index():
    usuarios = Usuarios.query.all()
    result = [e.to_dict() for e in usuarios]
    return Response(response=json.dumps(result), status=200, content_type="application/json")


@app.route('/add', methods=['POST'])
def add():
    usuario = Usuarios(request.form['nome'])
    db.session.add(usuario)
    db.session.commit()
    return Response(response=json.dumps({'status': 'success', 'msg': "Usuario cadastrado com sucesso"}), status=200,
                    content_type="application/json")


@app.route('/edit/<int:id>', methods=['PUT', 'POST'])
def edit(id):
    usuario = Usuarios.query.get(id)
    if request.form['nome']:
        usuario.nome = request.form['nome'];
    if request.form['email']:
        usuario.email = request.form['email']
    if request.form['ativo']:
        usuario.ativo = request.form['ativo']
    db.session.commit()
    return Response(response=json.dumps({'status': 'success', 'msg': 'Usuario Editado com sucesso'}), status=200, content_type="application/json")


@app.route('/delete/<int:id>', methods=['GET', 'DELETE'])
def delete(id):
    disciplina = Usuarios.query.get(id)
    db.session.delete(disciplina)
    db.session.commit()
    return Response(response=json.dumps({'status': 'success', 'msg': 'Usuario Excluido com sucesso'}), status=200, content_type="application/json")

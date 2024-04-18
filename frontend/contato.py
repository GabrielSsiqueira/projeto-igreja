
from flask import Flask, render_template, request, redirect, Blueprint, url_for
import flask_cors
import requests

contato_blueprint = Blueprint('contato',__name__)


@contato_blueprint.route("/listar_contato")
def contato():

    backend_url = 'http://127.0.0.1:5000/contato'
    response = requests.get(backend_url)

    if response.status_code == 200:
        contato = response.json()
        return render_template ('listar_contato.html', dados=contato, contato=(0,0))
    else:
        return render_template('listar_contato.html',dados=[], contato=[])
    

@contato_blueprint.route("/contato/delete/<id>")
def liderancaDelete(id):
  bd = db.SQLiteConnection('dados.db')
  bd.connect()
  bd.execute_query(f"DELETE FROM lideranca WHERE id = {id}")
  return redirect(url_for('listar_contato'))
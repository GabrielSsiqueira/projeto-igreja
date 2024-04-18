
from flask import Flask, render_template, request, redirect, Blueprint, url_for
import flask_cors
import requests

membro_blueprint = Blueprint('membros', __name__)


@membro_blueprint.route("/membros")
def membros():

  backend_url = 'http://127.0.0.1:5000/membros'
  response = requests.get(backend_url)

  if response.status_code == 200:
      membros = response.json()
      return render_template('membros.html', dados=membros, membros=(0,0))
  else:
    return render_template("membros.html", dados=[], membros=(0,0))
  
@membro_blueprint.route("/membros/delete/<id>")
def membrosDelete(id):
  bd = db.SQLiteConnection('dados.db')
  bd.connect()
  bd.execute_query(f"DELETE FROM membros WHERE id = {id}")
  return redirect(url_for('membros'))

@membro_blueprint.route("/membros/edit/<id>")
def membrosEdit(id):
  bd = db.SQLiteConnection('dados.db')
  bd.connect()
  query = f"select id, nome from membros where id = {id};"
  nome = bd.execute_query(query)
  return render_template("membros.html", membros=nome)

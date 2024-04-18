
from flask import Flask, render_template, request, redirect, Blueprint, url_for
import flask_cors
import requests

lideranca_blueprint = Blueprint('lideranca', __name__)


@lideranca_blueprint.route("/lideranca")
def lideranca():

  backend_url = 'http://127.0.0.1:5000/lideranca'
  response = requests.get(backend_url)

  if response.status_code == 200:
      lideranca = response.json()
      return render_template('lideranca.html', dados=lideranca, lideranca=(0,0))
  else:
    return render_template("lideranca.html", dados=[], lideranca=(0,0))
  
@lideranca_blueprint.route("/lideranca/delete/<id>")
def liderancaDelete(id):
  bd = db.SQLiteConnection('dados.db')
  bd.connect()
  bd.execute_query(f"DELETE FROM lideranca WHERE id = {id}")
  return redirect(url_for('lideranca'))

@lideranca_blueprint.route("/atas/edit/<id>")
def atasEdit(id):
  bd = db.SQLiteConnection('dados.db')
  bd.connect()
  query = f"select id, nome from lideranca where id = {id};"
  nome = bd.execute_query(query)
  return render_template("lideranca.html", lideranca=nome)

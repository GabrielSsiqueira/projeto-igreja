
from flask import Flask, render_template, request, redirect, Blueprint, url_for
import flask_cors
import requests

ata_blueprint = Blueprint('ata', __name__)


@ata_blueprint.route("/atas")
def atas():

  backend_url = 'http://127.0.0.1:5000/atas'
  response = requests.get(backend_url)

  if response.status_code == 200:
      atas = response.json()
      return render_template('atas.html', dados=atas, atas=(0,0))
  else:
    return render_template("atas.html", dados=[], membros=(0,0))
  
@ata_blueprint.route("/atas/delete/<id>")
def atasDelete(id):
  bd = db.SQLiteConnection('dados.db')
  bd.connect()
  bd.execute_query(f"DELETE FROM atas WHERE id = {id}")
  return redirect(url_for('atas'))

@ata_blueprint.route("/atas/edit/<id>")
def atasEdit(id):
  bd = db.SQLiteConnection('dados.db')
  bd.connect()
  query = f"select id, nome from atas where id = {id};"
  nome = bd.execute_query(query)
  return render_template("atas.html", atas=nome)

from flask import Flask, request, render_template
import json
from flask_cors import CORS

app = Flask(__name__)

from membro import membro_blueprint
from ata import ata_blueprint
from lideranca import lideranca_blueprint
from contato import contato_blueprint


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/painel")
def admin_panel():
    return render_template('painel.html')

@app.route("/logout")
def logout():
    return('index.html')

app.register_blueprint(membro_blueprint)
app.register_blueprint(ata_blueprint)
app.register_blueprint(lideranca_blueprint)
app.register_blueprint(contato_blueprint)


if __name__ == "__main__":
  app.run(debug=True, port=5001)


from flask import Flask, render_template, request, send_from_directory
from utils.gerador_certificado import gerar_certificado, listar_certificados
import os
import re

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nome = request.form["nome"]
        cpf_raw = request.form["cpf"]
        nivel = request.form["nivel"]
        cpf = re.sub(r'\D', '', cpf_raw)
        link = gerar_certificado(nome, cpf, nivel)
        return render_template("gerar.html", link=link)
    return render_template("index.html")

@app.route("/buscar", methods=["GET", "POST"])
def buscar():
    certificados = []
    if request.method == "POST":
        cpf_raw = request.form["cpf"]
        cpf = re.sub(r'\D', '', cpf_raw)
        certificados = listar_certificados(cpf)
    return render_template("buscar.html", certificados=certificados)

@app.route("/certificado/<nome_arquivo>")
def certificado(nome_arquivo):
    pasta = os.path.join("static", "certificados")
    return send_from_directory(pasta, nome_arquivo, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
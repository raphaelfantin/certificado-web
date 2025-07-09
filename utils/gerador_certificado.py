from fpdf import FPDF
from datetime import datetime
import os
import re

TEMPLATE_PATHS = {
    "Básico": {
        "frente": "utils/templates_png/basico_frente.png",
        "verso": "utils/templates_png/basico_verso.png"
    },
    "Intermediário": {
        "frente": "utils/templates_png/intermediario_frente.png",
        "verso": "utils/templates_png/intermediario_verso.png"
    },
    "Avançado": {
        "frente": "utils/templates_png/avancado_frente.png",
        "verso": "utils/templates_png/avancado_verso.png"
    }
}

def data_em_portugues():
    meses = {
        '01': 'janeiro', '02': 'fevereiro', '03': 'março',
        '04': 'abril', '05': 'maio', '06': 'junho',
        '07': 'julho', '08': 'agosto', '09': 'setembro',
        '10': 'outubro', '11': 'novembro', '12': 'dezembro'
    }
    hoje = datetime.today()
    dia = hoje.strftime('%d')
    mes = meses[hoje.strftime('%m')]
    ano = hoje.strftime('%Y')
    return f"{dia} de {mes} de {ano}"

def gerar_certificado(nome, cpf, nivel):
    curso = "Excel com Método PLAD"
    instrutor = "Raphael Fantin"
    data_formatada = data_em_portugues()
    templates = TEMPLATE_PATHS[nivel]

    hoje_iso = datetime.today().strftime("%Y%m%d")
    nome_arquivo = f"{cpf}_{nivel}_{hoje_iso}.pdf"
    output_path = os.path.join("static", "certificados", nome_arquivo)

    pdf = FPDF(orientation='L', unit='mm', format='A4')

    for lado in ["frente", "verso"]:
        pdf.add_page()
        img_path = templates[lado]
        pdf.image(img_path, x=0, y=0, w=297, h=210)

        if lado == "frente":
            pdf.set_font("Helvetica", "B", 26)
            pdf.set_text_color(0, 0, 0)
            pdf.set_xy(0, 70)
            pdf.cell(297, 10, nome, ln=True, align="C")

            pdf.set_font("Helvetica", "", 14)
            pdf.set_xy(0, 135)
            pdf.cell(297, 10, f"Data de emissão: {data_formatada}", ln=True, align="C")

            pdf.set_font("Helvetica", "", 12)
            pdf.set_xy(30, 174)
            pdf.cell(0, 10, f"Nome: {nome}", ln=True)

            pdf.set_xy(30, 179)
            pdf.cell(0, 10, f"CPF: {cpf}", ln=True)

    pdf.output(output_path)
    return "/" + output_path.replace("\\", "/")

def listar_certificados(cpf):
    pasta = "static/certificados"
    arquivos = os.listdir(pasta)
    cpf_puro = re.sub(r'\D', '', cpf)
    return [arq for arq in arquivos if cpf_puro in arq and arq.endswith(".pdf")]
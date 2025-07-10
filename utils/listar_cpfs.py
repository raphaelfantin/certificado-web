import os
import re

def listar_cpfs_emitidos():
    pasta = "static/certificados"
    arquivos = os.listdir(pasta)
    cpfs = set()

    for nome_arquivo in arquivos:
        if nome_arquivo.endswith(".pdf"):
            match = re.match(r"(\d{11})_", nome_arquivo)
            if match:
                cpfs.add(match.group(1))
    
    return sorted(cpfs)

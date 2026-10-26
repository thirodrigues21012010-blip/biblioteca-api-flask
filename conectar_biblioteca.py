import sqlite3
from pathlib import Path


CAMINHO_BANCO = Path(__file__).with_name("biblioteca.db")


def conectar(caminho=CAMINHO_BANCO):
    conexao = sqlite3.connect(caminho)
    conexao.row_factory = sqlite3.Row
    return conexao

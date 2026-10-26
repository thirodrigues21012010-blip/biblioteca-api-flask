from flask import Flask, jsonify, request

from conectar_biblioteca import conectar
from livro import Livro
from livro_dao import LivroDAO


app = Flask(__name__)


@app.route("/livros")
def listar_livros():
    # Cada requisição usa sua própria conexão SQLite.
    conexao = conectar()
    try:
        dao = LivroDAO(conexao)
        resultado = dao.buscar_todos()
        return jsonify(resultado)
    finally:
        conexao.close()


@app.route("/livros", methods=["POST"])
def cadastrar_livro():
    dados = request.json
    if not isinstance(dados, dict):
        return jsonify({"erro": "Envie um objeto JSON com os dados do livro."}), 400

    titulo = dados.get("titulo")
    autor = dados.get("autor")
    ano = dados.get("ano_publicacao")
    disponivel = dados.get("disponivel", True)
    if (not isinstance(titulo, str) or not titulo.strip()
            or not isinstance(autor, str) or not autor.strip()
            or type(ano) is not int or type(disponivel) is not bool):
        return jsonify({
            "erro": "Informe titulo e autor não vazios, ano_publicacao inteiro "
                    "e disponivel booleano (true ou false)."
        }), 400

    livro = Livro(titulo.strip(), autor.strip(), ano, disponivel)
    conexao = conectar()
    try:
        dao = LivroDAO(conexao)
        dao.inserir(livro)
        return jsonify({"status": "criado"}), 201
    finally:
        conexao.close()


if __name__ == "__main__":
    app.run(debug=True)

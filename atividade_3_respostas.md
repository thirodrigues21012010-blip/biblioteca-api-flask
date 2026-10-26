# Atividade 3 — API Flask para o Sistema de Biblioteca

Aluno: Thiago Rodrigues | Turma: 2 TI B

## Parte 1 — Planejamento

| Rota | Método | O que faz |
|---|---|---|
| /livros | GET | Consulta todos os livros pelo LivroDAO e os devolve em JSON. |
| /livros | POST | Recebe um livro em JSON, cadastra pelo LivroDAO e confirma a criação. |

## Partes 2 e 3 — Código Python (`app.py`)

```python
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
```

## Parte 4 — Fetch no navegador (`teste_fetch.js`)

```javascript
// Abra http://127.0.0.1:5000/livros antes de executar no console (F12).
// Execute primeiro a consulta:
fetch("/livros")
  .then(r => r.json())
  .then(dados => console.log(dados));

// Depois execute o cadastro. Cada execução insere um novo registro.
fetch("/livros", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    titulo: "Dom Casmurro",
    autor: "Machado de Assis",
    ano_publicacao: 1899,
    disponivel: true
  })
})
  .then(async r => {
    console.log("Código HTTP:", r.status);
    return r.json();
  })
  .then(dados => console.log(dados));

// Quando o cadastro terminar, execute novamente a consulta GET acima.
```

Teste realizado pelo aluno no navegador: consulta inicial vazia, cadastro com HTTP 201 e status criado, seguido de consulta com um registro.

## Parte 5 — Revisão rápida

1. **B.** Para manter a responsabilidade única: a rota cuida de HTTP e o DAO cuida do banco.
2. **B.** GET busca ou lê dados; POST envia dados para criar um novo registro.
3. **B.** Os dados chegam do navegador pela rede. `input()` aguardaria uma pessoa digitando no terminal do servidor.

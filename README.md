# Biblioteca — API Flask

Aluno: Thiago Rodrigues | Turma: 2 TI B

[Respostas completas da atividade 3](atividade_3_respostas.md)

Testes GET e POST realizados no console do navegador pelo aluno, com cadastro
HTTP 201 e consulta posterior retornando um livro.

Base mínima da atividade 2 e implementação da atividade 3, conforme os dois
enunciados fornecidos. Os exemplos ProdutoDAO/API de Produto e o diagrama
anterior não foram disponibilizados; não foi possível conferir a organização
exata usada pelo professor em aula.

## Como executar

1. Baixe o projeto em Code > Download ZIP, extraia e abra um terminal na pasta que contém `app.py`.
2. Instale a dependência:

   ```bash
   python -m pip install -r requirements.txt
   ```

3. Inicie o servidor:

   ```bash
   python app.py
   ```

4. Abra `http://127.0.0.1:5000/livros` no navegador.
5. Abra o console com F12 e execute os trechos de `teste_fetch.js`, um de cada vez.
6. Para encerrar o servidor, pressione Ctrl+C no terminal.

Se o seu sistema utiliza `python3`, substitua `python` por `python3` nos comandos.
O modo `debug=True` atende ao exercício e deve ser usado apenas no ambiente local.

## Organização

- `livro.py`: representa o livro e seus atributos.
- `conectar_biblioteca.py`: abre a conexão com SQLite.
- `livro_dao.py`: cria a tabela, insere e consulta os livros.
- `app.py`: recebe as requisições HTTP e devolve JSON.
- `teste_fetch.js`: comandos pedidos para o console do navegador.
- `atividade_3_respostas.md`: planejamento e revisão da atividade 3.
- `requirements.txt`: dependência necessária.

O arquivo `biblioteca.db` é criado automaticamente junto aos arquivos Python
no primeiro acesso válido às rotas. O banco começa vazio e mantém os registros
quando o servidor é reiniciado. Não há cadastro automático de livros.

## Escopo da atividade 2

Foram implementados a conexão, a tabela, a classe Livro e os métodos
`inserir(livro)` e `buscar_todos()`. O construtor do DAO recebe a conexão.
Os campos seguem o enunciado: id, titulo, autor, ano_publicacao e disponivel.
A disponibilidade é armazenada como 0 ou 1 e devolvida em JSON como false ou true.
As inserções usam parâmetros `?` e `commit()`.

Os métodos atualizar/excluir e a demonstração de CRUD completo ficaram de fora,
conforme o escopo combinado. Portanto, este projeto não representa a entrega
completa da atividade 2.

## Resultados esperados

- GET inicial: HTTP 200 e `[]`.
- POST com o exemplo: HTTP 201 e `{"status": "criado"}`.
- GET após o cadastro: lista com o livro e seu id.
- POST com campos ausentes ou tipos incorretos: HTTP 400.

Os testes executados durante a elaboração estão descritos em `verificacao.md`.

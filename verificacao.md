# Verificação do projeto

Testes executados com Flask 3.1.3, usando o cliente de testes do Flask e um
banco SQLite temporário, separado do projeto entregue:

- GET em banco vazio: HTTP 200 e lista vazia.
- POST de livro válido: HTTP 201 e resposta `{"status": "criado"}`.
- GET após POST: livro devolvido com id e todos os atributos.
- Novas conexões e outro cliente: dados persistidos e consultáveis.
- Cadastro com disponibilidade false: valor preservado na consulta.
- Título com apóstrofo e acento: cadastro e consulta corretos.
- Campos ausentes, JSON com lista e tipos incorretos: HTTP 400.
- Corpo sem Content-Type JSON: HTTP 415.
- JSON malformado: HTTP 400.
- PUT em /livros: HTTP 405, pois a atividade só prevê GET e POST.
- Requisições inválidas não inserem novos registros.

Todos esses testes passaram. A sintaxe de `teste_fetch.js` também foi
verificada com `node --check`.

Posteriormente, o aluno executou os comandos fetch no console do navegador.
As capturas compartilhadas na conversa mostraram GET inicial vazio, POST com
HTTP 201 e status criado, e GET final com um registro, autor Machado de Assis,
ano 1899 e disponibilidade true. As imagens não integram o repositório,
conforme a preferência do aluno.

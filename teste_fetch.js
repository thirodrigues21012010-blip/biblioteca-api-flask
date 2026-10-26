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

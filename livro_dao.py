class LivroDAO:
    def __init__(self, conexao):
        self.conexao = conexao
        self.criar_tabela()

    def criar_tabela(self):
        cursor = self.conexao.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS livros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                autor TEXT NOT NULL,
                ano_publicacao INTEGER NOT NULL,
                disponivel INTEGER NOT NULL DEFAULT 1
                    CHECK (disponivel IN (0, 1))
            )
        """)
        self.conexao.commit()

    def inserir(self, livro):
        cursor = self.conexao.cursor()
        cursor.execute("""
            INSERT INTO livros (titulo, autor, ano_publicacao, disponivel)
            VALUES (?, ?, ?, ?)
        """, (livro.titulo, livro.autor, livro.ano_publicacao,
              int(livro.disponivel)))
        self.conexao.commit()
        livro.id = cursor.lastrowid

    def buscar_todos(self):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM livros ORDER BY id")
        # Dicionários podem ser convertidos em JSON pelo Flask.
        livros = []
        for linha in cursor.fetchall():
            livro = dict(linha)
            livro["disponivel"] = bool(livro["disponivel"])
            livros.append(livro)
        return livros

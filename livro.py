class Livro:
    def __init__(self, titulo, autor, ano_publicacao, disponivel=True, id=None):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = disponivel

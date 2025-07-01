class Livro:
    def __init__(self, titulo, autor, ISBN):
        self.titulo = titulo
        self.autor = autor
        self.isbn = ISBN
        self.disponivel = True
    


class Usuario:
    def __init__(self, nome, id):
        self.nome = nome
        self.id = id
        self.emprestimos = []
        


class Biblioteca:
    def __init__(self):
        self.info = None

import library_system as ls

library = ls.Library()

books_data = [
    {"ISBN": "978-0743273565", "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"ISBN": "978-0061120084", "title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"ISBN": "978-0451524935", "title": "1984", "author": "George Orwell"},
    {"ISBN": "978-0547928227", "title": "The Hobbit", "author": "J.R.R. Tolkien"},
    {"ISBN": "978-0385732559", "title": "The Catcher in the Rye", "author": "J.D. Salinger"},
    {"ISBN": "978-0345391803", "title": "The Hitchhiker's Guide to the Galaxy", "author": "Douglas Adams"},
    {"ISBN": "978-0743273565", "title": "Pride and Prejudice", "author": "Jane Austen"}, # Teste de duplicidade
    {"ISBN": "978-0307277747", "title": "The Da Vinci Code", "author": "Dan Brown"},
    {"ISBN": "978-0439023528", "title": "The Hunger Games", "author": "Suzanne Collins"},
    {"ISBN": "978-0062315811", "title": "The Alchemist", "author": "Paulo Coelho"}
]

users_data = [
    {"id": "U001", "name": "Alice Smith"},
    {"id": "U002", "name": "Bob Johnson"},
    {"id": "U003", "name": "Carol White"},
    {"id": "U004", "name": "David Green"},
    {"id": "U001", "name": "Alice Smith Duplicada"} # Para testar a duplicidade
]


print("\n--- Testando add_book ---")

for book in books_data:
    library.add_book(book["ISBN"], book["title"], book["author"])
     
     
print("\n--- Testando add_user ---")

for user in users_data:
    library.add_user(user["id"], user["name"])


print("\n--- Testando find_book ---")

# Caso 1: Livro que existe (The Great Gatsby - ISBN 978-0743273565)
print(f"Buscando ISBN: 978-0743273565")
library.find_book("978-0743273565")

# Caso 2: Livro que existe (The Hobbit - ISBN 978-0547928227)
print(f"Buscando ISBN: 978-0547928227")
library.find_book("978-0547928227")

# Caso 3: Livro que existe (The Alchemist - ISBN 978-0062315811)
print(f"Buscando ISBN: 978-0062315811")
library.find_book("978-0062315811")

# Caso 4: Livro que NÃO existe (ISBN 978-9999999999)
print(f"Buscando ISBN: 978-9999999999")
library.find_book("978-9999999999")

# Caso 5: Buscar ISBN duplicado (ISBN 978-0743273565) - deve encontrar The Great Gatsby
print(f"Buscando ISBN (duplicado): 978-0743273565")
library.find_book("978-0743273565")
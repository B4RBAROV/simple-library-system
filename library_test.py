import library_system as ls

library = ls.Library()

books_data = [
    {"ISBN": "978-0743273565", "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"ISBN": "978-0061120084", "title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"ISBN": "978-0451524935", "title": "1984", "author": "George Orwell"},
    {"ISBN": "978-0547928227", "title": "The Hobbit", "author": "J.R.R. Tolkien"},
    {"ISBN": "978-0385732559", "title": "The Catcher in the Rye", "author": "J.D. Salinger"},
    {"ISBN": "978-0345391803", "title": "The Hitchhiker's Guide to the Galaxy", "author": "Douglas Adams"},
    {"ISBN": "978-0307277747", "title": "The Da Vinci Code", "author": "Dan Brown"},
    {"ISBN": "978-0439023528", "title": "The Hunger Games", "author": "Suzanne Collins"},
    {"ISBN": "978-0062315811", "title": "The Alchemist", "author": "Paulo Coelho"}
]

users_data = [
    {"id": "U001", "name": "Alice Smith"},
    {"id": "U002", "name": "Bob Johnson"},
    {"id": "U003", "name": "Carol White"},
    {"id": "U004", "name": "David Green"},
    {"id": "U005", "name": "Ana Lívia Noleto"}
]

for book in books_data:
    library.add_book(book["ISBN"], book["title"], book["author"])

for user in users_data:
    library.add_user(user["id"], user["name"])

library.main_menu()
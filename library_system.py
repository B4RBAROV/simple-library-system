class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.isbn = ISBN
        self.available = True
        self.left = self.right = None
    


class Users:
    def __init__(self):
        self.user = {}
        
    def new_user(self, name, id):
        self.user[id] = {
            "name": name,
            "loans": []
        }
        


class Library:
    def __init__(self):
        self.root = None

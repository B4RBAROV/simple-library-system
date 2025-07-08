class Book:
    def __init__(self, ISBN, title, author):
        self.title = title
        self.author = author
        self.isbn = ISBN
        self.available = True
        self.left = self.right = None
        
        
    def add_book(self, ISBN, title, author):
        if ISBN < self.isbn:
            if self.left == None:
                self.left = Book(ISBN, title, author)
                return
            self.left.add_book(ISBN, title, author)
            return
        
        if self.right == None:
            self.right = Book(ISBN, title, author)
            return
        self.right.add_book(ISBN, title, author)

    


class Users:
    def __init__(self):
        self.user = {}
        
    def new_user(self, id, name):
        self.user[id] = {
            "name": name,
            "loans": []
        }
        


class Library:
    def __init__(self):
        self.root = None
        
    
    def add_book(self, ISBN, title, author):
        if self.root != None:
            self.root.add_book(ISBN, title, author)
            return print('New book cataloged!')
        
        self.root = Book(ISBN, title, author)
        return print('New book cataloged!')
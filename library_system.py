class Book:
    def __init__(self, isbn, title, author):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True
        self.left = self.right = None
        
        
    def __str__(self):
        return 'Livro: {} ({});\nBy: {}.\n'.format(self.title, self.isbn, self.author)
        
        
    def add_book(self, isbn, title, author):
        if isbn == self.isbn:
            print('ISBN already exists!\n')
            return
        
        if isbn < self.isbn:
            if self.left == None:
                self.left = Book(isbn, title, author)
                print('New book cataloged!\n')
                return
            
            return self.left.add_book(isbn, title, author)
        
        if self.right == None:
            self.right = Book(isbn, title, author)
            print('New book cataloged!\n')
            return
            
        return self.right.add_book(isbn, title, author)
    
    
    def find_book(self, isbn):
        if isbn == self.isbn:
            return print(str(self))
        
        if isbn < self.isbn:
            if self.left == None:
                print("Didn't find any book with ISBN = {}\n".format(isbn))
                return
            
            self.left.find_book(isbn)
            return
        
        if self.right == None:
            print("Didn't find any book with ISBN = {}\n".format(isbn))
            return
        
        self.right.find_book(isbn)
    


class User:
    def __init__(self):
        self.user = {}
        
        
    def new_user(self, id, name):
        if id in self.user:
            print('User id already exists!\n')
            return
        
        self.user[id] = {
            "name": name,
            "loans": []
        }
        print('User registered!\n')
        


class Library:
    def __init__(self):
        self.root = None
        self.user_manager = User()
        
    
    def add_book(self, isbn, title, author):
        if self.root != None:
            self.root.add_book(isbn, title, author)
            return
        
        self.root = Book(isbn, title, author)
    
    
    def add_user(self, id, name):
        self.user_manager.new_user(id, name)
        
        
    def find_book(self, isbn):
        if self.root != None:
            self.root.find_book(isbn)
            return 
        
        print("No books have been cataloged in this library yet!")
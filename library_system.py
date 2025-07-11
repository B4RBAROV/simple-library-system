class Book:
    def __init__(self, ISBN, title, author):
        self.title = title
        self.author = author
        self.isbn = ISBN
        self.available = True
        self.left = self.right = None
        
        
    def add_book(self, ISBN, title, author):
        if ISBN == self.isbn:
            print('ISBN already exists!\n')
            return
        
        if ISBN < self.isbn:
            if self.left == None:
                self.left = Book(ISBN, title, author)
                print('New book cataloged!\n')
                return
            
            return self.left.add_book(ISBN, title, author)
        
        if self.right == None:
            self.right = Book(ISBN, title, author)
            print('New book cataloged!\n')
            return
            
        return self.right.add_book(ISBN, title, author)

    


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
        
    
    def add_book(self, ISBN, title, author):
        if self.root != None:
            self.root.add_book(ISBN, title, author)
            return
        
        self.root = Book(ISBN, title, author)
    
    
    def add_user(self, id, name):
        self.user_manager.new_user(id, name)
        
        
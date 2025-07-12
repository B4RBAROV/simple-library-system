class Book:
    def __init__(self, isbn, title, author):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True
        self.left = self.right = None
        
        
    def __str__(self):
        return 'ISBN: {};\nLivro: {};\nBy: {}.\n'.format(self.isbn, self.title, self.author)
        
        
    def add_book(self, isbn, title, author):
        if isbn == self.isbn:
            return False
        
        if isbn < self.isbn:
            if self.left == None:
                self.left = Book(isbn, title, author)
                return True
            
            return self.left.add_book(isbn, title, author)
        
        if self.right == None:
            self.right = Book(isbn, title, author)
            return True
            
        return self.right.add_book(isbn, title, author)
    
    
    def find_book(self, isbn):
        if isbn == self.isbn:
            return self
        
        if isbn < self.isbn:
            if self.left == None:
                return
            
            return self.left.find_book(isbn)
        
        if self.right == None:
            return
        
        return self.right.find_book(isbn)
    


class User:
    def __init__(self):
        self.user = {}
        
        
    def new_user(self, id, name):
        if id in self.user:
            return False
        
        self.user[id] = {
            "name": name,
            "loans": []
        }
        return True
        


class Library:
    def __init__(self):
        self.root = None
        self.user_manager = User()
        
    
    def add_book(self, isbn, title, author):
        if self.root != None:
            sys_return = self.root.add_book(isbn, title, author)
            
            if sys_return:
             return print('New book cataloged!\n')
         
            return print('ISBN already exists!\n')
        
        self.root = Book(isbn, title, author)
        print('New book cataloged!\n')
    
    
    def add_user(self, id, name):
        sys_return = self.user_manager.new_user(id, name)
        
        if sys_return:
            return print('User registered!\n')
        
        print('User id already exists!\n')
        
        
    def find_book(self, isbn):
        if self.root != None:
            sys_return = self.root.find_book(isbn)
            
            if sys_return != None:
                return print(sys_return.__str__())
            
            return print("Didn't find any book with ISBN = {}\n".format(isbn))
             
        
        print("No books have been cataloged in this library yet!")
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
            if self.left is None:
                self.left = Book(isbn, title, author)
                return True
            
            return self.left.add_book(isbn, title, author)
        
        if self.right is None:
            self.right = Book(isbn, title, author)
            return True
            
        return self.right.add_book(isbn, title, author)
    
    # ----------------FUNCT FUTURA-------------------
    def borrow(self, isbn):
        pass
    # -----------------------------------------------
    
    
    
    def find_book(self, isbn):
        if isbn == self.isbn:
            return self
        
        if isbn < self.isbn:
            if self.left is None:
                return
            
            return self.left.find_book(isbn)
        
        if self.right is None:
            return
        
        return self.right.find_book(isbn)
    
    
    def list_available_books(self):
        if self.left is not None:
            self.left.list_available_books()
            
        if self.available:
            print(self.__str__())
        
        if self.right is not None:
            self.right.list_available_books()
    


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
    
    # --------------------EM CRIAÇÃO-----------------------
    def borrow_book(self, id, isbn):
        if id in self.user:
            book = Library.find_book(isbn)
            
            if book is None:
                return 1 # isbn not founded
            
            if book.available:
                self.user[id]["loans"].append(isbn)
                return 2 # borrow succed
            
            return 3 # isbn not available
                    
        
        return 0 # user id not founded
    # -----------------------------------------------------   


class Library:
    def __init__(self):
        self.root = None
        self.user_manager = User()
        
    
    def add_book(self, isbn, title, author):
        if self.root is not None:
            sys_return = self.root.add_book(isbn, title, author)
            
            if sys_return:
             print('New book cataloged!\n')
             return sys_return
         
            print('ISBN already exists!\n')
            return sys_return
        
        self.root = Book(isbn, title, author)
        print('New book cataloged!\n')
        return True
    
    
    def add_user(self, id, name):
        sys_return = self.user_manager.new_user(id, name)
        
        if sys_return:
            print('User registered!\n')
            return sys_return
        
        print('User id already exists!\n')
        return sys_return
        
        
    def find_book(self, isbn):
        if self.root is not None:
            sys_return = self.root.find_book(isbn)
            
            if sys_return is not None:
                print(sys_return.__str__())
                return sys_return
            
            print("Didn't find any book with ISBN = {}\n".format(isbn))
            return sys_return
             
        
        print("No books have been cataloged in this library yet!")
        return None
    
    # -------------------------EM CRIAÇÃO---------------------------
    def borrow_book(self, id, isbn):
        if self.root is not None:
            sys_return = self.user_manager.borrow_book(id, isbn)
            
        if sys_return == 0:
            print('User not founded!')
            
        if sys_return == 1:
            print('ISBN not founded!')
            
        if sys_return == 2:
            print('User: {}, boorow book: {}'.format(id, isbn))
            
        if sys_return == 3:
            print("Book: {} is not available!".format(isbn))
    # --------------------------------------------------------------
        
    
    def list_available_books(self):
        if self.root is not None:
            print("-------Available Books-------")
            self.root.list_available_books()
            return True
        
        print("No books have been cataloged in this library yet!")
        return False
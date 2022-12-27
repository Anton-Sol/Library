
class Library:
    __instance = None
    
    def __new__(cls, *args,**kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            return cls.__instance
        else:
            raise Exception("Library have only instance")
        
    def __init__(self, lib_name = "Open Source LIbrary"):
        self.lib_name = lib_name
        self.books = 459
        self.books = {}

    def __str__(self):
        return self.lib_name


class Librarian:
    __instance = None
    __instance_amount = 0

    def __new__(cls, *args,**kwargs):
        if cls.__instance is None or cls.__instance_amount < 3:
            cls.__instance = super().__new__(cls)
            cls.__instance_amount += 1
            return cls.__instance
        else:
            raise Exception("Librarian have only 3 instance")

    
    def __init__(self, name):
        self.name = name 

    def __str__(self):
        return self.name

library  = Library()
print(library)

librarian1 = Librarian("Mary")
librarian2 = Librarian("Janette")
librarian3 = Librarian("Groze")


for i in (librarian1,librarian2,librarian3):
    print(i)
'''abstract fabric'''

from abc import ABC, abstractmethod
class Books(ABC):
    def __init__(self):
        self.books_dict = dict()

    def add_book(self):
        new_book = input("Whats books you want to add\n>>>>").strip().title()
        book_amount = input('How much examples\n').strip()

        assert book_amount.isdigit(), "Must be digit"#assert - утверждать->short if/else

        book_amount = int(book_amount)

        if new_book not in self.books_dict:
            self.books_dict[new_book] = book_amount
        else:
            self.books_dict[new_book] += book_amount

    @abstractmethod
    def type_book(self):
        pass
        
    def __getitem__(self,item):
        return self.books_dict[item]

    def __str__(self):
        return ''.join(f'Title: {key}, amount books: {value}\n' for key,value in self.books_dict.items())

class Fantasy(Books):
    def type_book(self):
        return 'Fantasy'

class Non_fiction(Books):
    def type_book(self):
        return 'Non_fiction'

class Roman(Books):
    def type_book(self):
        return 'Roman'

class Science(Books):
    def type_book(self):
        return 'Science'



book = Roman()
book.add_book()
print(book)

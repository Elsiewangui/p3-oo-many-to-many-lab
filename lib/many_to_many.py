class Author:
    all_authors =[]
    def __init__(self,name):
        if not isinstance(name,str) or not name:
            raise Exception("Invalid")
        self.name=name
        Author.all_authors.append(self)
    

    def contracts(self):
        return[contract for contract in Contract.all if contract.author==self]
    
    def books(self):
        return[contract.book for contract in self.contracts()]
    
    def sign_contract(self,book,date,royalties):
        contract = Contract(self, book, date, royalties)
        return contract
    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())

class Book:
    all_books=[]
    def __init__(self,title):
        if not isinstance (title,str) or not title:
            raise Exception("Invalid")
        self.title=title
        Book.all_books.append(self)
        
    def authors(self):
        return[contract.author  for contract in self.contracts()]
    def contracts(self):
        return[contract for contract in Contract.all if contract.book==self]

class Contract:
    all= []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise ValueError("Invalid Author")
        if not isinstance(book, Book):
            raise ValueError("Invalid Book")
        if not isinstance(date, str):
            raise ValueError("Date must be a string.")
        if not isinstance(royalties, int) or royalties < 0:
            raise ValueError("Royalties must be a non-negative integer.")
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        if not isinstance(date, str):
            raise ValueError("Invalid date")
        return [contract for contract in cls.all if contract.date == date]
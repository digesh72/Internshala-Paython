class Book:

    def __init__(self,title,author,publisher,price,copies_sold):
        self.set_title(title)
        self.set_author(author)
        self.set_publisher(publisher)
        self.set_price(price)
        self.set_copies_sold(copies_sold)
        
    def get_title(self):
        return self._title
    
    def set_title(self,title):
        if not title :
            print("Title cannot be empty.")
        else:
            self._title = title
            return
        
    def get_author(self):
        return self._author
    
    def set_author(self,author):
        if not author:
            print("Author cannot be empty.")
        else:
            self._author = author
            return
        
    def get_publisher(self):
        return self._publisher
    
    def set_publisher(self,publisher):
        if not publisher:
            print("Publisher cannot be empty.")
        else:
            self._publisher = publisher
            return
        
    def get_price(self):
        return self._price
    
    def set_price(self,price):
        if not isinstance(price, (int, float)) or price <= 0:
            print("Price must be a positive number.")
        else:
            self._price = price
            return
        
    def get_copies_sold(self):
        return self._copies_sold
    
    def set_copies_sold(self,copies_sold):
        if not isinstance(copies_sold, int) or copies_sold < 0:
            print("Copies sold must be a non-negative integer.")
        else:
            self._copies_sold = copies_sold
            return
           
        
    def royalty(self):
        copies = self.get_copies_sold()
        price = self.get_price()
        royalty_amount = 0
        
        if copies <= 500:
            royalty_amount = copies * price * 0.10
        elif copies <= 1500:
            royalty_amount = (500 * price * 0.10) + ((copies - 500) * price * 0.125)
        else:
            royalty_amount = (500 * price * 0.10) + (1000 * price * 0.125) + ((copies - 1000) * price * 0.15)
        return royalty_amount

class EBook(Book): 
    def __init__(self,title,author,publisher,price,copies_sold,ebook_format):
        super().__init__(title,author,publisher,price,copies_sold)
        self.set_format = ebook_format

        def get_format(self):
            return self._ebook_format

        def set_format(self, ebook_format):
            if not ebook_format:
                print("Ebook format cannot be empty.")
                self._ebook_format = "Unknown"
            else:
                self._ebook_format = ebook_format
                return

        def royalty(self):
            base_royalty = super().royalty()
            return base_royalty * 0.88 
        

b = Book("OOP in Python", "John Doe", "TechPress", 500, 1800)
print("Book Royalty:", b.royalty())

e = EBook("OOP in Python - Digital", "John Doe", "TechPress", 500, 1800, "PDF")
print("EBook Royalty after GST:", e.royalty())


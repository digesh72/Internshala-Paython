import sqlite3

# Connect to the database
MyBook = sqlite3.connect('booktest.db')
curbook = MyBook.cursor()

# Create table (only first time)
try:
    curbook.execute('''
        CREATE TABLE book (
            BookID INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT(30) NOT NULL,
            author TEXT(20) NOT NULL,
            price REAL NOT NULL
        );
    ''')
    print("Table created successfully.")
except:
    print("Table already exists. Skipping creation.")

# Insert a book
title = input('Enter Book Title: ')
author = input('Enter Book Author: ')
price = float(input('Enter Book Price: '))

curbook.execute(
    "INSERT INTO book (title, author, price) VALUES (?, ?, ?);",
    (title, author, price)
)

MyBook.commit()
Total_amount = 0.0
while True:
# Search for the book
    print("=====================")
    book_name = input('Enter Book name to search: ')
    curbook.execute("SELECT * FROM book WHERE title = ?", (book_name,))

    result = curbook.fetchone()

    if result:
        print(result)
        print("=======================")
        book_copy = int(input('Enter the number of copies required: '))
        Total_amount += book_copy * result[3]
    else:
         print("Book not found.")
         continue
    
    print("========================")
    book_add = input('Do you want to add more books? Y/N: ')
    if book_add.strip().upper() == 'N':
        break

print("\nTotal Cost:", Total_amount)
MyBook.close()

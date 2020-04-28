# Implement a library management system which will handle the following tasks:
# 1. Customer should be able to display all books available in the library
# 2. Handle the process when customer requests to borrow a new books
# 3. Update the library collection when the customer returns the book

class Library:
    # display available books and availablity status, and next available date
    def __init__(self, dataBase):
        self.books = dataBase
        self.index = 0

    def displayBooks(self):
        for id, bookProps in enumerate(self.books):
            print(id,".The book \"", bookProps[0],"\" is wriiten by", bookProps[1])
            print('Availablity Status: ',bookProps[2])
            if bookProps[2] == 'no':
                print("Next Available in",bookProps[3],"days")
            print()

    def getBookPropArray(self):
        return self.books[self.index]

    def borrowBook(self):
        self.displayBooks()
        self.index = int(input("Select the index of the Title: "))
        bookProps = self.getBookPropArray()
        if bookProps[2] == 'yes':
            print("You may borrow the book for the next 14 days")
            bookProps[2] = 'no'
            bookProps[3] = 14
            return self.index, bookProps
        else:
            print("Try Again in", bookProps[3],"days")
            return self.index, bookProps


    def returnBook(self):
        self.books.append(self.bookReturned)
        displayBooks(self)

    def setAvailableDate(self):
        pass

    def findAvailableDate(self):
        pass

class Customer:
    # display the list of borrowed books by the customer, and allow him to borrow or return
    def __init__(self):
        pass

    def borrowedBooks(self):
        pass

    def borrowBook(self):
        pass

    def returnBook(self):
        pass
        
# properties : name, author, availablity status, nextAvailable
dataBase = [['The ending of time', 'JK', 'yes', None],['Void','Lalith','no',14]]
dataBaseAvailability = []

lib = Library(dataBase)
# lib.displayBooks()
index, borrowArray = lib.borrowBook()
dataBase[index] = borrowArray
lib.displayBooks()

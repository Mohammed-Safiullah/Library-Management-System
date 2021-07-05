
class Library:
    def __init__(self, listOfBooks):
        #Instance attribute that will store all the books of library
        self.books = listOfBooks
        pass

    def displayAvailableBooks(self):
        print("The books available in this library are:")
         #for-loop to display every book book available in the list of books
        for book in self.books:
            print("\t*" + book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(
                f"You have been issued {bookName}. Please Keep it safe and return it within 30 days.")
            # Issuing the book to the student(if it is available) and removing it from the available list of books
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, this book is either not available or has already been issued to someone else. Please wait until the book is available. ")

    def returnBook(self, bookName):
        # adding the returned book to available list of books in the library
        self.books.append(bookName)
        print(
            f"Thanks for adding/returning this book. Hope you enjoyed reading it.\nHave a great day ahead.")
        return False


class Student:

    def requestBook(self):  #function to take the input of the requested book, from the student
        self.book = input("Enter the book name you want to borrow: ")
        return self.book

    def returnBook(self):  #function to take the input of the book returned, from the student
        self.book = input("Enter the book name you want to Add/Return: ")
        return self.book



if __name__ == "__main__":

    centralLibrary = Library(["Algorithms", "Django", "Clrs", "Python Notes"])
    student = Student()
    
    while(True):
            welcomeMsg = '''\n=====Welcome to Central Library=====
            please choose an option:
            1. List of all the books
            2. Request a book
            3. Add/Return a book
            4. Exit the library
            '''
            print(welcomeMsg)
            try:
                a = int(input("Enter an option: "))

                if a == 1:
                    centralLibrary.displayAvailableBooks()
                elif a == 2:
                    centralLibrary.borrowBook(student.requestBook())
                elif a == 3:
                    centralLibrary.returnBook(student.returnBook())
                elif a == 4:
                    print("Thanks for choosing Central Library")
                    exit()
                else:
                    print("Invalid Choice")
            except Exception as e:
                print("Please enter a valid input")
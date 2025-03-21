print("Welcome to Ojha ji Library")
book_list = []


Menu = """"
1)Add
2)Remove Book
3)View All Books
4)Press x to exit 
"""

# Adding Book
def add_book(book_list, title,author,year,genre,read):
   book = {
       "Title":title,
       "Author":author,
       "Year":year,
       "Genre":genre,
       "Read Status":read,

   } 
   book_list.append(book)
   print("Book Added Successfully")


# Removing Book
def remove_book(book_list, title):
    for book in book_list:
        if book["Title"].lower() == title.lower():
          book_list.remove(book)
          print("Book Removed Successfully")
          return
        else:
          print("Book Not Found")


# Showing Off All Books
def show_list(book_list):
    if book_list:
        print("Current Books: ")
        for book in book_list:
            read_status = "Read" if book["Read Status"].lower() == 'yes'else "unread"
            print(f'{book["Title"]} by {book["Author"]} ({book["Year"]}) - {book["Genre"]} - {read_status}')

    else:
        print("No Book in List")

# Exit
def exit_program():
    print("Than You For Visiting Ojha Ji Digital Library..")
    quit()


# Main Program with loops
while True:
    print(Menu)
    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        book_name = input("Enter Book Name to add: ") 
        author = input("Enter Author Name: ")
        publi_year = int(input("Enter Publication Year: "))
        genre = input("Enter the genre: ")
        read = input("Have you read this book Yes/NO: ").strip()
        add_book(book_list,book_name,author,publi_year,genre,read)
    elif choice == 2:
        book_name = input("Enter a Book Name to remove: ")
        remove_book(book_list,book_name)
    elif choice ==3:
        show_list(book_list)
    elif choice == 4:
        exit_program()
    else:
        print("Invalid Choice")
        print("Press Enter to return to the Main Menu")

    









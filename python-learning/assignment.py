
books_collection = []  
users_list = []        


def add_book(book_id, title, author, genre, availability):
    book = {
        "ID": book_id,
        "Title": title,
        "Author": author,
        "Genre": genre,
        "Availability": availability
    }
    books_collection.append(book)


def add_user(user_id, name):
    user = {
        "ID": user_id,
        "Name": name,
        "Borrowed Books": []
    }
    users_list.append(user)


def search_books(query):
    results = [book for book in books_collection if 
               query.lower() in book["Title"].lower() or 
               query.lower() in book["Author"].lower() or 
               query.lower() in book["Genre"].lower()]
    
    if results:
        print("Search Results:")
        for book in results:
            print(f"{book['Title']} by {book['Author']} - Genre: {book['Genre']} - Status: {book['Availability']}")
    else:
        print("No books found matching your criteria.")


def view_all_books():
    print("All Books:")
    for book in books_collection:
        print(f"{book['ID']}. \"{book['Title']}\" by {book['Author']} ({book['Availability']})")


def view_available_books():
    available_books = [book for book in books_collection if book["Availability"] == "Available"]
    print("Available Books:")
    if available_books:
        for book in available_books:
            print(f"{book['ID']}. \"{book['Title']}\" by {book['Author']}")
    else:
        print("No books are currently available.")


def view_checked_out_books():
    checked_out_books = [book for book in books_collection if book["Availability"] == "Checked Out"]
    print("Checked-Out Books:")
    if checked_out_books:
        for book in checked_out_books:
            print(f"{book['ID']}. \"{book['Title']}\" by {book['Author']}")
    else:
        print("No books are currently checked out.")


def borrow_book(user_id, book_id):
    user = next((u for u in users_list if u["ID"] == user_id), None)
    book = next((b for b in books_collection if b["ID"] == book_id), None)
    
    if user and book:
        if book["Availability"] == "Available":
            user["Borrowed Books"].append(book)
            book["Availability"] = "Checked Out"
            print(f"{user['Name']} borrowed '{book['Title']}'.")
        else:
            print(f"Sorry, the book \"{book['Title']}\" is currently checked out.")
    else:
        if user is None:
            print("User not found.")
        if book is None:
            print("Book not found.")

def return_book(user_id, book_id):
    user = next((u for u in users_list if u["ID"] == user_id), None)
    book = next((b for b in books_collection if b["ID"] == book_id), None)

    if user and book and book in user["Borrowed Books"]:
        user["Borrowed Books"].remove(book)
        book["Availability"] = "Available"
        print(f"{user['Name']} returned '{book['Title']}'.")
    else:
        print("Returning failed: User or book not found, or book was not borrowed.")

def menu():
    while True:
        print("\nWelcome to the Community Library System!")
        print("----------------------------------------")
        print("Please choose an option:")
        print("1. View all books")
        print("2. Search for a book")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. View all users")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            view_all_books()
        elif choice == "2":
            search_query = input("Enter a title, author, or genre to search for books: ")
            search_books(search_query)
        elif choice == "3":
            user_id = int(input("Enter your User ID: "))
            book_id = int(input("Enter the Book ID you want to borrow: "))
            borrow_book(user_id, book_id)
        elif choice == "4":
            user_id = int(input("Enter your User ID: "))
            book_id = int(input("Enter the Book ID you want to return: "))
            return_book(user_id, book_id)
        elif choice == "5":
            print("All Users:")
            for user in users_list:
                print(f"User ID: {user['ID']}, Name: {user['Name']}, Borrowed Books: {[book['Title'] for book in user['Borrowed Books']]}")
        elif choice == "6":
            print("Exiting the library system. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

def initialize_data():
    add_book(1, "1-To Kill a Mockingbird", "Harper Lee", "Fiction", "Available")
    add_book(2, "2-1984", "George Orwell", "Dystopian", "Checked Out")
    add_book(3, "3-The Great Gatsby", "F. Scott Fitzgerald", "Classic", "Available")
    add_book(4, "4-Pride and Prejudice", "Jane Austen", "Romance", "Available")
    add_book(5, "5-Moby Dick", "Herman Melville", "Adventure", "Available")
    add_user(1, "Alice")
    add_user(2, "Bob")


initialize_data()
menu()

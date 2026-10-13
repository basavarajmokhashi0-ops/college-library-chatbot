# College Library Chatbot

books = [
    {
        "id": "B001",
        "name": "Java Programming",
        "author": "Herbert Schildt",
        "department": "CSE/ISE",
        "copies": 3
    },
    {
        "id": "B002",
        "name": "Database Management Systems",
        "author": "Korth",
        "department": "CSE/ISE",
        "copies": 2
    },
    {
        "id": "B003",
        "name": "Computer Networks",
        "author": "Andrew S. Tanenbaum",
        "department": "CSE/ISE",
        "copies": 4
    },
    {
        "id": "B004",
        "name": "Operating System Concepts",
        "author": "Silberschatz",
        "department": "CSE/ISE",
        "copies": 1
    },
    {
        "id": "B005",
        "name": "Data Structures",
        "author": "Seymour Lipschutz",
        "department": "CSE/ISE",
        "copies": 3
    },
    {
        "id": "B006",
        "name": "Software Engineering",
        "author": "Ian Sommerville",
        "department": "ISE",
        "copies": 2
    },
    {
        "id": "B007",
        "name": "Python Programming",
        "author": "Mark Lutz",
        "department": "CSE/ISE",
        "copies": 5
    },
    {
        "id": "B008",
        "name": "Machine Learning",
        "author": "Tom M. Mitchell",
        "department": "CSE/ISE",
        "copies": 2
    },
    {
        "id": "B009",
        "name": "Web Technology",
        "author": "Uttam K. Roy",
        "department": "ISE",
        "copies": 3
    },
    {
        "id": "B010",
        "name": "Computer Graphics",
        "author": "Donald D. Hearn",
        "department": "CSE/ISE",
        "copies": 1
    }
]


# Display all books first
def show_all_books():
    print("\n==============================================================")
    print("                 COLLEGE LIBRARY BOOKS")
    print("==============================================================")

    print(f"{'ID':<8}{'BOOK NAME':<32}{'AUTHOR':<25}{'COPIES'}")
    print("-" * 75)

    for book in books:
        print(
            f"{book['id']:<8}"
            f"{book['name']:<32}"
            f"{book['author']:<25}"
            f"{book['copies']}"
        )

    print("==============================================================")


# Search for a book
def search_book(search):

    found = False

    for book in books:

        if (search.lower() in book["name"].lower()
                or search.lower() in book["author"].lower()
                or search.upper() == book["id"]):

            print("\nBook Found!")
            print("----------------------------")
            print("Book ID:", book["id"])
            print("Book Name:", book["name"])
            print("Author:", book["author"])
            print("Department:", book["department"])
            print("Available Copies:", book["copies"])

            if book["copies"] > 0:
                print("Status: Available")
            else:
                print("Status: Not Available")

            print("----------------------------")

            found = True

    if not found:
        print("\nSorry, book not found.")


# Library chatbot
def library_chatbot():

    # Show books FIRST
    show_all_books()

    print("\n======================================")
    print("       COLLEGE LIBRARY CHATBOT")
    print("======================================")

    print("Hello! Welcome to the College Library.")

    print("\nYou can:")
    print("1. Search for a book")
    print("2. Check book availability")
    print("3. Show all books")
    print("4. Exit")

    while True:

        choice = input("\nYou: ")

        # Search
        if choice == "1":

            search = input("Enter book name, author or Book ID: ")
            search_book(search)

        # Availability
        elif choice == "2":

            search = input("Enter book name or Book ID: ")

            found = False

            for book in books:

                if (search.lower() in book["name"].lower()
                        or search.upper() == book["id"]):

                    print("\nBook:", book["name"])
                    print("Available Copies:", book["copies"])

                    if book["copies"] > 0:
                        print("Status: Available")
                    else:
                        print("Status: Not Available")

                    found = True

            if not found:
                print("Book not found.")

        # Show books
        elif choice == "3":

            show_all_books()

        # Exit
        elif choice == "4":

            print("\nThank you for using the College Library Chatbot!")
            break

        else:

            print("\nInvalid choice. Please enter 1, 2, 3 or 4.")


# Start program
library_chatbot()
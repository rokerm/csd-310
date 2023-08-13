#Malachi Roker
#08/06/2023
#CYBR410

import sys
import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

def show_menu():
    #shows main page
    print("\n Main Page")

    print("\n 1. Our Books\n 2. Our Locations\n 3. Account Settings\n 4. Close")

    try:
        select = int(input("\n Please enter a number from the choices above. \n"))
        return select
    
    except ValueError:
        print("\n Invalid number value. Session has ended.")


def show_books(_cursor):
    _cursor.execute("SELECT book_id, book_name, author, details from book")
# results for cursor
    books = _cursor.fetchall()

    print ("\n -- Displaying All Books -- ")

# iterate over book data
    for book in books:
        print("\n Book Name: {}\n Author: {}\n Details: {}\n ".format(book[0], book[1], book[2]))
    

def validate_user():
#user validation
    try:
        user_id = int (input('\n Please enter your customer id \n '))

# if the user's choice is less than 0 or greater than 3, display an error message
        if user_id < 0 or user_id > 3:
            print('\n Invalid customer id, session has ended ')
            sys.exit(0)
            
        print("Login Successful!")

        return user_id 
    except ValueError:
        print('\n Invalid user id, session has ended')
        sys.exit(0)

def show_account_settings():
    #displays account settings

    try:
        print("\n -- Account Settings --")
        print("\n 1. Wishlist\n 2. Add Book\n 3. Main Page\n ")
        account_settings = int(input('\n Please enter a number to navigate through the customer menu \n'))

        return account_settings
    except ValueError:
        print("\n Invalid entry, session has ended")
        sys.exit(0)

def show_wishlist(_cursor, _user_id):
    #users add books to wishlist

    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))
    
    wishlist = _cursor.fetchall()

    print("\n -- Displaying Wishlist --")

    for book in wishlist:
        print("\n Book Name: {}\n Author: {}\n".format(book[4], book[5]))

def show_books_to_add(_cursor, _user_id):
    #displays all other books not chosen by the user

    query = ("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id, _user_id))
    print(query)

    _cursor.execute(query)

    book_options = _cursor.fetchall()
    for book in book_options:
        print("\n Book id: {}\n Book Name: {}\n".format(book[0], book[1]))

    print("\n -- Displaying Book Inventory --")

def add_book_to_wishlist(_cursor, _user_id, _book_id):
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))

def show_locations(_cursor):
# displays store locations
    _cursor.execute("SELECT store_id, locale from store")

    locations = _cursor.fetchall()

    print("\n -- Displaying Locations --")

    for location in locations:
        print("Locale: {}\n".format(location[1]))

try:
    #connect to whatabook database
    db = mysql.connector.connect(**config)

    cursor = db.cursor()
    print("\n  Welcome to WhataBook Virtual Store! ")

    user_selection = show_menu()

    # while the user doesn't equal 4 
    while user_selection != 4:

        # if the user chooses option 1, display the books
        if user_selection == 1:
            show_books(cursor)

        # if the user chooses option 2, display location
        if user_selection == 2:
            show_locations(cursor)
        
        # if the user chooses option 3, validate user id and and show account settings
        if user_selection == 3:
            my_user_id = validate_user()
            account_settings = show_account_settings()

            while account_settings != 3:

             # if the user chooses option 1 it will display user and wishlist 
                if account_settings == 1:
                    show_wishlist(cursor, my_user_id)

                # if the user chooses option 2, show the wishlist items not chosen by the user
                if account_settings == 2:

                    # show the books not chosen by the user
                    show_books_to_add(cursor, my_user_id)

                    # fetch the desired book_id 
                    book_id = int(input("\n Enter the id of the book you want to add: "))
                    
                    # add the desired book to user's wishlist
                    add_book_to_wishlist(cursor, my_user_id, book_id)

                    db.commit() # commit changes

                    print("\n Book id: {} was added to your wishlist!".format(book_id))
                                
                    # if the user's choice is less than 0 or greater than 2, display an error message
                if account_settings < 0 or account_settings > 3:
                    print("\n Invalid option, please try again.")

                    # show the account menu 
                account_settings = show_account_settings()
        
        # if the user's choice is less than 0 or greater than 4, display an error message
        if user_selection < 0 or user_selection > 4:
            print("\n Invalid option, please try again.")
            
        # show the main menu
        user_selection = show_menu()

    print("\n Session Ended. Please visit us again!")

except mysql.connector.Error as err:
    
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")

    else:
        print(err)

finally:
        #disconnects from MYSQL
        db.close()
    







from getbooks import search_books

# storing variables outside of functions so input calls wont overwrite reading list
reading_list = []

# loop runs asking for input so long as the while loop isnt broken
while True:
    # welcome message and instructions
    print('\nWelcome to the Google Books CLI application!\n')
    query = input("Enter a Search Term to Begin\nTo Exit the Program enter 'quit program'\n\n")
    # checks input is not quit program command
    if query != "quit program":
        # calls search book fucntion
        print(search_books(query,reading_list))
    else:
        # goodbye message, breaks loop and exits program
        print('Thank you for using the Google Books CLI application')
        break


import requests
import os
from dotenv import load_dotenv

# loading Google Book API key from .env file
load_dotenv()

# Funtion built to parse out search results. It also adds books to the reading list and dsiplays the reading list
def print_book_results(results,reading_list):
    # establishes result list and stores newline string value for print formating and to account for zero based index
    result_list = ['\n']
    # loops through search results and increases book choices from 1 to length of the results list
    for i, book in enumerate(results, start=1):
        # check to see if book has author or not (every book found had at least a title and a publisher)
        if len(book) == 2:
            title = book[0][0]
            publisher = book[1][0]
            result_list.append(f"{i}: \"{title}\" published by {publisher}\n")
        # check to see if book had title, author, and publisher
        elif len(book) == 3:
            title = book[0][0]
            # check to see if book had multiple authors
            if len(book[1]) == 1:
                authors = book[1][0]
            else:
                authors = ' and '.join(book[1])
            publisher = book[2][0]
            result_list.append(f"{i}: \"{title}\" by {authors}, published by {publisher}\n")
    # result string stores a printable formatted string for the current results stored in result_list
    result_string = "".join(result_list)
    # check to make sure result list not empty
    if len(result_list) == 1:
        return "No search results found"
    # displays search results
    print('\nHere are your search results:')
    print(result_string)
    # enters secondary menu to add book to reading list and display that reading list. reading list remembers additions while program runs as they are stored outside of the functions
    while True:
        # menu instructions
        book_num = input("\nEnter the number of a book below to add it to your reading list\nTo display your reading list enter 'display'\nTo return to the main menu enter 'menu'\n\n")
        # check to see if book result number is a number in-between 1 and the total results
        if book_num.isnumeric() and (int(book_num) in range(1,len(result_list))):
            # formating to remove book choice number from string
            curr_book = result_list[int(book_num)]
            colon_index = curr_book.index(":") + 1
            formatted_curr_book = curr_book[colon_index:]
            striped_book = formatted_curr_book.strip()
            # checks that duplicate book will not be added to list
            if striped_book not in reading_list:
                # adds formatted book to reading list and adds formatting for display call
                reading_list.append(striped_book)
                reading_list.append('\n')
                print("\nBook added to list\n")
            else:
                print("This book has already been added to your reading list")
        # checks to see if display command was given
        elif book_num == 'display':
            # checks that reading list is not empty
            if len(reading_list) == 0:
                print('\nYour reading list is currently empty. Add books to display your list\n')
            else:
                # displays reading list in string format
                print('\nHere is your Reading List\n')
                reading_string = "".join(reading_list) + "\n"
                print(reading_string)  
        # checks to see if menu command was given
        elif book_num == 'menu':
            break
        # checks for any other not recognized command was entered
        else:
            print('Please reenter a valid command\n')
    # return statement informing user the system is returning to main menu
    return "\n...redirecting back to the main menu...\n"
    


# function built to perform initial api request utilizing user input 
def search_books(query,reading_list):
    # replaces white space in query
    formatted_query = query.replace(" ", "+")
    # retrieves api key and stores it in variable
    api_key = os.getenv('API_KEY')
    # variable that makes API call and stores results
    response = requests.get(
        f'https://www.googleapis.com/books/v1/volumes?q={formatted_query}&maxResults=5&key={api_key}')
    # checks to make sure API request was good
    if response.status_code == 200:
        # Parse the data into json
        data = response.json()
        # Create an empty list to store the Title, Author, & Publisher of each search result
        results = []
        # checks to ensure there are results in the data.
        if data['totalItems'] == 0:
            return "\nNo Results Found. Try Another Search.\n"
        # loops through 5 result 'items'
        for item in data['items']:
            # due to some results not having authors and some results returning Publisher vs Publishers, if/else statements used to append book in proper format
            if ('author' and 'authors') not in item['volumeInfo']:
                if 'publisher' in item['volumeInfo']:
                    results.append([[item['volumeInfo']['title']], [item['volumeInfo']['publisher']]])
                elif 'publishers' in item['volumeInfo']:
                    results.append([[item['volumeInfo']['title']], [item['volumeInfo']['publishers']]])
            elif 'publisher' in item['volumeInfo']:
                results.append([[item['volumeInfo']['title']], item['volumeInfo']['authors'], [item['volumeInfo']['publisher']]])
            elif 'publishers' in item['volumeInfo']:
                results.append([[item['volumeInfo']['title']], item['volumeInfo']['authors'], [item['volumeInfo']['publishers']]])
        # return statement calls print_boo_results function to format that book data to display
        return print_book_results(results,reading_list)
        #Alternative return statement used to check query tests conducting in the spec file
    else:
        # Print an error message
        return print(f'An error occurred: {response.status_code} \n Please try a new search.')
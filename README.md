To Run:
-generate a Google Books API key
-create a .env file and add the following variable to line 1: API_KEY = "Replace With Your API Key"
-Create and start a venv environment
-pip install requirements.txt
-run the runner.py file



My Process:
-To test my Google Books API key in a get request I used postman to ensure I was properly formatting my uri request
-Once I had a good result from Google Books, I hardcoded a search request function that printed the results in my console in JSON
-I then processed my results data to store only the three variables I wanted to display and save to the reading list (Author, Title, Publisher)
-I imported the function into a spec file where I ran various querying tests to find edge cases in the results I received
-Once I consistently received data for various edge cases in the form of nested lists, I created a function to formate the data in a way I felt was readable with the console interface. In this function I built a sub-menu to handle the addition of books from the search results to the reading list as well as a command to display that list.
-Next I imported the main function into the runner.py file where I created a main menu and ran queries to test the limitations and edge cases of the application.
-Once I was satisfied with the applications functionality, I cleaned up my code and added notes explaining the logic of my functions, created this READ.ME document and pushed the project to github.
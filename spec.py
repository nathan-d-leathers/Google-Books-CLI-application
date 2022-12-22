from getbooks import search_books

# Testing a single word book title
print(search_books("dune")) 

# Testing a two worded book title 
print(search_books("harry potter")) 
# problem with publisher term

# Testing a multiple worded book title
print(search_books("The Lord of The Rings")) 

# Testing a book title with multiple authors
print(search_books("The Dawn of Everything"))

# Testing an author name
print(search_books("Dr. Suess")) 

# testing a book title where results might have no author, test 1
print(search_books("Bible"))

# testing a book title where results might have no author test 2
print(search_books("The Bible"))

# testing a book title where results might have no author, test 3
print(search_books("The Holy Bible"))

# testing a book title with no author
print(search_books("Key of Solomon"))

# testing untitled book
print(search_books("untitled"))

# testing a search with no real words
print(search_books("208ydp12u3dg12u3dg82 21p93d8h2euodh"))



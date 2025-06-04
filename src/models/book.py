# This is a class that represents a book. Think of it as a template for creating book objects.
# Each book will have an ID, title, genre, and description.
class Book:
    # This is called when we create a new book. It sets up the initial values.
    # The parameters are what we need to create a book:
    # - bookId: a unique number for each book
    # - title: the name of the book
    # - genre: what type of book it is (fantasy, crime, etc.)
    # - description: a summary of what the book is about
    def __init__(self, bookId, title, genre, description):
        # We store these values in the book object using 'self'
        # 'self' refers to the current book we're working with
        self.bookId = bookId
        self.title = title
        self.genre = genre
        self.description = description
    
    # This method shows the book's information in a nice format
    def displayInfo(self):
        # First, print the title and genre
        print(f"\nTitle: {self.title}")
        print(f"Genre: {self.genre}")
        
        # Now we'll print the description, but we'll make it look nice
        # by breaking it into lines that aren't too long
        print("Description:", end=" ")
        
        # Split the description into individual words
        words = self.description.split()
        
        # Keep track of how many characters we've printed on the current line
        line_length = 0
        
        # Go through each word in the description
        for word in words:
            # If adding this word would make the line too long (more than 80 characters)
            # start a new line
            if line_length + len(word) + 1 > 80:  # (+1 for the space after the word)
                print("\n", end="")  # Start a new line
                line_length = 0      # Reset the line length
            
            # Print the word and a space
            print(word, end=" ")
            # Add the word length plus 1 (for the space) to our line length
            line_length += len(word) + 1
        
        # Print a blank line at the end for spacing
        print("\n") 
# We need these libraries:
# - sqlite3: for working with our database
# - Book: our Book class that we created
import sqlite3
from src.models.book import Book

# This class handles all our interactions with the database
class DatabaseManager:
    # When we create a new DatabaseManager, we tell it where our database file is
    def __init__(self, dbPath="database/books.db"):
        # Store the database path for later use
        self.dbPath = dbPath
    
    # This is a helper method that connects to our database
    def getConnection(self):
        # Create and return a connection to our SQLite database
        return sqlite3.connect(self.dbPath)
    
    # This method gets all the different genres we have in our database
    def getAllGenres(self):
        try:
            # Connect to the database
            conn = self.getConnection()
            # Create a cursor (think of it as a pointer to the database)
            cursor = conn.cursor()
            
            # Get all unique genres, sorted alphabetically
            cursor.execute('SELECT DISTINCT genre FROM books ORDER BY genre')
            
            # Get all results and extract just the genre names
            # The [genre[0] for genre in cursor.fetchall()] part:
            # - cursor.fetchall() gets all results
            # - for each result (genre), we take the first item [0]
            # - this creates a list of just the genre names
            genres = [genre[0] for genre in cursor.fetchall()]
            
            # Close the connection (always clean up!)
            conn.close()
            
            # Return the list of genres
            return genres
            
        except Exception as e:
            # If anything goes wrong, print the error and return an empty list
            print(f"Error getting genres: {str(e)}")
            return []
    
    # This method gets books of a specific genre
    # - genre: what type of books to get
    # - limit: how many books to return (default is 10)
    def getBooksByGenre(self, genre, limit=10):
        try:
            # Connect to the database
            conn = self.getConnection()
            cursor = conn.cursor()
            
            # Get random books of the specified genre
            # The ? marks are placeholders for our values (genre and limit)
            # This is a safe way to put values in our SQL query
            cursor.execute('''
                SELECT book_id, title, genre, description 
                FROM books 
                WHERE genre = ? 
                ORDER BY RANDOM() 
                LIMIT ?
            ''', (genre, limit))
            
            # Create a list to store our books
            books = []
            
            # For each row we got from the database:
            # - Create a new Book object with the data
            # - Add it to our list
            for row in cursor.fetchall():
                book = Book(row[0], row[1], row[2], row[3])
                books.append(book)
            
            # Close the connection
            conn.close()
            
            # Return our list of books
            return books
            
        except Exception as e:
            # If anything goes wrong, print the error and return an empty list
            print(f"Error getting books: {str(e)}")
            return [] 
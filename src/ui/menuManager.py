# This class handles all the user interaction - showing menus and getting user input
class MenuManager:
    # When we create a MenuManager, we need to give it a DatabaseManager
    # so it can get books and genres from the database
    def __init__(self, dbManager):
        # Store the database manager for later use
        self.dbManager = dbManager
    
    # This method shows all available genres with numbers
    # Example:
    # 1. fantasy
    # 2. crime
    # etc.
    def displayGenres(self, genres):
        print("\nAvailable genres:")
        # enumerate(genres, 1) gives us pairs of (number, genre) starting from 1
        for i, genre in enumerate(genres, 1):
            print(f"{i}. {genre}")
    
    # This method gets a valid number choice from the user
    # maxChoice is the highest number they're allowed to pick
    def getUserChoice(self, maxChoice):
        while True:  # Keep asking until we get a valid choice
            try:
                # Get input from user and convert to number
                choice = int(input("\nEnter your choice (number): "))
                
                # Check if the number is valid (between 1 and maxChoice)
                if 1 <= choice <= maxChoice:
                    return choice
                
                # If we get here, the number was too high or too low
                print(f"Please enter a number between 1 and {maxChoice}")
                
            except ValueError:
                # If the user didn't enter a valid number, tell them
                print("Please enter a valid number")
    
    # This method gets a yes/no answer from the user
    def getYesNoInput(self, prompt):
        while True:  # Keep asking until we get a valid answer
            # Get input and convert to lowercase (so 'Y' and 'y' both work)
            response = input(prompt + " (y/n): ").lower()
            
            # Check if the response is valid
            if response in ['y', 'n']:
                # Return True for 'y', False for 'n'
                return response == 'y'
            
            # If we get here, they didn't enter 'y' or 'n'
            print("Please enter 'y' for yes or 'n' for no")
    
    # This method shows a list of books
    def displayBooks(self, books):
        # If we didn't get any books, say so
        if not books:
            print("\nNo books found for this genre.")
            return
        
        # Show the recommendations
        print("\nHere are some recommended books:")
        for book in books:
            book.displayInfo()
    
    # This is the main method that runs our menu system
    def run(self):
        while True:  # Keep running until the user wants to quit
            # Get all genres from the database and show them
            genres = self.dbManager.getAllGenres()
            if not genres:
                print("Error: No genres available in the database")
                return
            
            self.displayGenres(genres)
            
            # Get the user's genre choice
            choice = self.getUserChoice(len(genres))
            selectedGenre = genres[choice - 1]  # -1 because list indices start at 0
            
            # Keep showing books in this genre until user wants to switch
            while True:
                # Get and show book recommendations
                books = self.dbManager.getBooksByGenre(selectedGenre)
                self.displayBooks(books)
                
                # Ask if they want more books in this genre
                if not self.getYesNoInput("\nWould you like more recommendations from this genre?"):
                    break
            
            # Ask if they want to pick another genre
            if not self.getYesNoInput("\nWould you like to choose another genre?"):
                print("\nThank you for using the Book Recommendation System!")
                break 
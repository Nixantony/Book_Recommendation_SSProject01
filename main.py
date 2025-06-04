# Import the classes we need from our other files
from src.database.databaseManager import DatabaseManager
from src.ui.menuManager import MenuManager

# This is our main function that starts the program
def main():
    # Show a welcome message
    print("Welcome to the Book Recommendation System!")
    print("----------------------------------------")
    
    # Create our database manager (to handle getting books from the database)
    dbManager = DatabaseManager()
    
    # Create our menu manager (to handle showing menus and getting user input)
    menuManager = MenuManager(dbManager)
    
    # Start the application by running the menu
    menuManager.run()

# This is a special Python line that only runs the main() function
# if we run this file directly (not when we import it from another file)
if __name__ == "__main__":
    main() 
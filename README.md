# Book Recommendation System

The home page displays the top 10 books based on genres. In recent years, recommender systems have been in great demand in every field, and so has it been in the world of readers. There have been a lot of recommendation techniques developed over the past years, such as Content-Based Filtering, Collaborative Filtering, and Hybrid Filtering. In this project, we have implemented a Content-Based Filtering approach, specifically using genre-based recommendation. Instead of relying on user behavior, this method suggests books by analyzing the content of the books themselves—particularly their genres. By matching genre similarities, users are presented with books that align closely with their interests. Books are the best resources for most of us to develop and gain perspectives. I myself love reading books. Once I like a book, I have a habit of going to good books or asking someone who has a similar taste to look for recommendations for the next series of books I might like. Artificial Intelligence has made our world so easy by recommending us books, movies, and products all based on past data, saving our time and energy on analyzing different options. In fact, sometimes machines can recommend us better than what we think, because they don’t suffer from emotional biases.

## Project Structure

```
bookRecommendation/
│
├── database/
│   └── books.db              # SQLite database with book info
│
├── src/
│   ├── models/
│   │   └── book.py           # Book class (what a book is)
│   ├── database/
│   │   └── databaseManager.py # Code to get books from the database
│   └── ui/
│       └── menuManager.py    # Code to show menus and take input
│
├── main.py                   # Starts the program
└── README.md                 # This file
```

## How to Run the Program

1. Make sure you have Python installed on your computer
2. Open a terminal/command prompt
3. Navigate to the project folder
4. Run the program with:
   ```
   python main.py
   ```

## How the Program Works

1. When you start the program, it will show you a list of available book genres
2. You can choose a genre by entering its number
3. The program will show you 10 random books from that genre
4. You can then:
   - Get more recommendations from the same genre
   - Choose a different genre
   - Exit the program

## Understanding the Code

The project uses Object-Oriented Programming (OOP) with three main classes:

1. **Book** (book.py)
   - Think of this as a template for books
   - Each book has:
     - An ID number
     - A title
     - A genre
     - A description

2. **DatabaseManager** (databaseManager.py)
   - Handles all database operations
   - Can:
     - Get a list of all genres
     - Get random books from a specific genre

3. **MenuManager** (menuManager.py)
   - Handles all user interaction
   - Shows menus and gets user input
   - Displays book information

## Learning from This Project

This project demonstrates several important programming concepts:

1. **Object-Oriented Programming (OOP)**
   - Using classes to organize code
   - Each class has a specific job

2. **Database Usage**
   - Using SQLite to store and retrieve data
   - Basic SQL queries

3. **User Interface**
   - Getting user input
   - Displaying formatted information
   - Input validation

4. **Code Organization**
   - Proper file structure
   - Separating different parts of the program

## Modifying the Program

Want to make changes? Here are some ideas:

1. Add more features:
   - Search for books by title
   - Add user ratings
   - Save favorite books

2. Improve the display:
   - Add colors to the text
   - Show more book information
   - Create a graphical interface

3. Enhance recommendations:
   - Recommend based on multiple genres
   - Add a rating system
   - Suggest similar books

## Need Help?

If you're new to programming and need help understanding any part of the code:
1. Look at the comments in the code - everything is explained!
2. Try running the program and see how it works
3. Experiment with making small changes to learn how things work 
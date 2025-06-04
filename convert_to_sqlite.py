import pandas as pd
import sqlite3
from pathlib import Path

def convert_csv_to_sqlite():
    print("Starting conversion process...")
    
    # Create database directory if it doesn't exist
    Path("database").mkdir(exist_ok=True)
    
    try:
        # Read the CSV file
        print("Reading CSV file...")
        df = pd.read_csv('dataset/data.csv')
        
        # Rename columns to match our desired schema
        column_mapping = {
            'index': 'book_id',
            'title': 'title',
            'genre': 'genre',
            'summary': 'description'
        }
        
        # Select and rename the columns
        df_selected = df.rename(columns=column_mapping)
        
        # Create SQLite database
        print("\nCreating SQLite database...")
        conn = sqlite3.connect('database/books.db')
        
        # Create table and insert data
        df_selected.to_sql('books', conn, if_exists='replace', index=False)
        
        # Create an index on book_id for faster queries
        cursor = conn.cursor()
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_book_id ON books(book_id);')
        
        # Get the number of rows inserted
        cursor.execute('SELECT COUNT(*) FROM books;')
        row_count = cursor.fetchone()[0]
        
        print(f"\nSuccess! Converted {row_count} books to SQLite database.")
        print("Database created at: database/books.db")
        
        conn.close()
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    convert_csv_to_sqlite() 
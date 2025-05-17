import requests
from bs4 import BeautifulSoup
import sqlite3

# Function to scrape quotes from a website
def scrape_quotes():
    url = "http://quotes.toscrape.com/page/1/"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        quotes = []
        for quote in soup.find_all("div", class_="quote"):
            text = quote.find("span", class_="text").text
            author = quote.find("span", class_="small").find("author").text
            quotes.append((text, author))
        return quotes
    else:
        print("Failed to retrieve quotes.")
        return []

# Function to create and initialize the database
def initialize_database():
    conn = sqlite3.connect("quotes.db")
    cursor = conn.cursor()
    
    # Create a table to store quotes
    cursor.execute('''CREATE TABLE IF NOT EXISTS quotes
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       text TEXT,
                       author TEXT)''')
    
    conn.commit()
    conn.close()

# Function to insert quotes into the database
def insert_quotes(quotes):
    conn = sqlite3.connect("quotes.db")
    cursor = conn.cursor()
    
    for quote in quotes:
        cursor.execute("INSERT INTO quotes (text, author) VALUES (?, ?)", quote)
    
    conn.commit()
    conn.close()

# Function to retrieve and print quotes from the database
def get_quotes_from_db():
    conn = sqlite3.connect("quotes.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM quotes")
    quotes = cursor.fetchall()
    
    for quote in quotes:
        print(f"{quote[1]} - {quote[2]}")

    conn.close()

# Main function
def main():
    initialize_database()
    quotes = scrape_quotes()
    if quotes:
        insert_quotes(quotes)
        print("Quotes inserted into the database.")
        print("\nQuotes from the database:")
        get_quotes_from_db()

if __name__ == "__main__":
    main()

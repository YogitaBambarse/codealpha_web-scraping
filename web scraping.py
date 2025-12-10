import requests
from bs4 import BeautifulSoup
import pandas as pd
url ="https://books.toscrape.com/catalogue/category/books/childrens_11/index.html"
response=requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")
# Lists for data
titles = []
prices = []
ratings = []

# Find all book sections
books = soup.find_all("article", class_="product_pod")

for book in books:
    # Title
    title = book.h3.a["title"]
    titles.append(title)
    
    # Price
    price = book.find("p", class_="price_color").text
    prices.append(price)
    
    # Rating (as text)
    rating = book.find("p")["class"][1]   # Example: "Three", "Five"
    ratings.append(rating)

# Make DataFrame
df = pd.DataFrame({x 
    "Book Title": titles,
    "Price": prices,
    "Rating": ratings
})

# Save as CSV
df.to_csv("books_scraped.csv", index=False)

print("Scraping completed! CSV file saved as books_scraped.csv")

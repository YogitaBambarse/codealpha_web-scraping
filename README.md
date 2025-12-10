# codealpha_web-scraping
Books to Scrape - Web Scraper

A Python script to scrape book data (title, price, rating) from the Books to Scrape website using BeautifulSoup and pandas.

## Features

Scrapes book titles, prices, and ratings.

Saves the data in CSV format for easy analysis.

Handles HTML parsing with BeautifulSoup.

## Code Example

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/catalogue/category/books/childrens_11/index.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract book titles, prices, and ratings
# Save to CSV using pandas

## Output

CSV file with columns:

Book Title

Price

Rating


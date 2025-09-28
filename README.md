Web Scraper for News Headlines
 The goal of this project is to automatically fetch the latest news headlines from the BBC News website and save them into a text file for easy reference or further analysis. This is useful for monitoring news,    creating datasets for NLP projects, or just staying updated.
 Overview:

 Libraries Used:
 requests → To send HTTP requests and fetch the HTML content of the webpage.
 BeautifulSoup (from bs4) → To parse the HTML and extract the news headlines.

 Key Functions:
 fetch_headlines(url: str) -> list:
 Fetches the HTML content of the given URL.
 Parses the HTML using BeautifulSoup.
 Searches for headline tags (<h1>, <h2>, <h3>).
 Filters out empty or very short text (less than 10 characters).
 Returns a list of headline strings.
 save_headlines(headlines: list, filename: str) -> None:
 Takes the list of headlines and writes them line by line into a text file.
 Provides feedback on successful saving.

 Execution Flow:
 The script starts by printing "Fetching headlines..."
 It calls fetch_headlines() to get headlines from the BBC News site.
 If headlines are found, it calls save_headlines() to store them in headlines.txt.
 Otherwise, it prints "No headlines found."
 
 Dataset:
 Type: Dynamic web dataset
 Source: BBC News (https://www.bbc.com/news)
 Content: Headlines of current news articles from the website.
 Format: Saved as a plain text file (headlines.txt), each headline on a new line.

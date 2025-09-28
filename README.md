import requests
URL = "https://www.bbc.com/news"
OUTPUT_FILE = "headlines.txt"
def fetch_headlines(url: str) -> list:
    """Fetch top news headlines from the given URL."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise error for bad status
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return []
 soup = BeautifulSoup(response.text, "html.parser")
    headlines = []
    for tag in soup.find_all(["h1", "h2", "h3"]):
        text = tag.get_text(strip=True)
        if text and len(text) > 10:
            headlines.append(text)
    return headlines
def save_headlines(headlines: list, filename: str) -> None:
    """Save headlines to a text file."""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            for line in headlines:
                f.write(line + "\n")
        printf("✅ {len(headlines)} headlines saved to {filename}")
    except Exception as e:
        print(f"Error saving headlines: {e}")
if __name__ == "__main__":
    print("Fetching headlines...")
    headlines = fetch_headlines(URL)
    if headlines:
        save_headlines(headlines, OUTPUT_FILE)
    else:
        print(" No headlines found.")


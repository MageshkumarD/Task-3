from urllib.request import urlopen
from html.parser import HTMLParser

URL = "https://www.bbc.com/news"
OUTPUT_FILE = "headlines.txt"


class HeadlineParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_heading = False
        self.headlines = []

    def handle_starttag(self, tag, attrs):
        if tag in ["h1", "h2", "h3"]:
            self.in_heading = True

    def handle_endtag(self, tag):
        if tag in ["h1", "h2", "h3"]:
            self.in_heading = False

    def handle_data(self, data):
        if self.in_heading and len(data.strip()) > 10:
            self.headlines.append(data.strip())


def fetch_headlines(url: str) -> list:
    with urlopen(url) as response:
        html = response.read().decode("utf-8")
    parser = HeadlineParser()
    parser.feed(html)
    return parser.headlines


def save_headlines(headlines: list, filename: str) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        for line in headlines:
            f.write(line + "\n")
    print(f"✅ {len(headlines)} headlines saved to {filename}")


if __name__ == "__main__":
    print("Fetching headlines...")
    headlines = fetch_headlines(URL)
    if headlines:
        for i, h in enumerate(headlines, start=1):
            print(f"{i}. {h}")   # 👈 print each headline to console
        save_headlines(headlines, OUTPUT_FILE)
    else:
        print("No headlines found.")

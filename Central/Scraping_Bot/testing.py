import requests
from bs4 import BeautifulSoup
import random
import time
from fake_useragent import UserAgent
from requests.exceptions import RequestException
import os
import re

## 

class ScraperBot:
    def __init__(self, base_url, endpoints=None):
        self.base_url = base_url
        self.headers = {'User-Agent': self.get_random_user_agent()}
        self.session = requests.Session()
        self.endpoints = endpoints if endpoints else ['']  # Default to base URL if no endpoints
        self.output_file = "scraped_data.txt"  # Output file

    def get_random_user_agent(self):
        ua = UserAgent()
        return ua.random

    def fetch_page(self, url):
        try:
            response = self.session.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            return response.text
        except RequestException as e:
            print(f"Request failed: {e}")
            return None

    def parse_html(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        return soup

    def scrape(self, endpoint):
        full_url = f"{self.base_url}/{endpoint}".rstrip('/')
        print(f"Scraping URL: {full_url}")
        
        html = self.fetch_page(full_url)
        if html:
            soup = self.parse_html(html)
            self.process_data(soup, full_url)
        else:
            print("Failed to retrieve the page.")

    def process_data(self, soup, page_url):
        with open(self.output_file, 'a', encoding='utf-8') as f:  # 'a' mode appends to the file
            f.write(f"Data scraped from: {page_url}\n")
            f.write("=" * 100 + "\n\n")

            # Extract Navigation Links
            nav_links = soup.find_all('a', href=True)
            if nav_links:
                f.write("Navigation Links:\n")
                for link in nav_links:
                    f.write(f"- {link['href']}\n")
                f.write("\n")
            f.write("=" * 100 + "\n\n")

            # Extract and label titles
            title = soup.title.string if soup.title else "No Title"
            f.write(f"Title: {title}\n\n")
            f.write("=" * 100 + "\n\n")

            # Extract and label paragraphs
            paragraphs = soup.find_all('p')
            if paragraphs:
                f.write("Paragraphs:\n")
                for p in paragraphs:
                    f.write(f"- {p.get_text(strip=True)}\n")
                f.write("\n")
            f.write("=" * 100 + "\n\n")

            # Extract and label headings (h1, h2, h3, etc.)
            for i in range(1, 4):  # Example for headings h1 to h3
                headings = soup.find_all(f"h{i}")
                if headings:
                    f.write(f"Headings (H{i}):\n")
                    for heading in headings:
                        f.write(f"- {heading.get_text(strip=True)}\n")
                    f.write("\n")
            f.write("=" * 100 + "\n\n")

            # Extract and label div class="country-info"
            country_info = soup.find_all('div', class_='country-info')
            if country_info:
                f.write("Country Info:\n")
                for info in country_info:
                    f.write(f"{info.get_text(strip=True)}\n")
                f.write("\n")

    def wait_random(self):
        delay = random.uniform(1, 3)
        print(f"Waiting for {delay:.2f} seconds to avoid detection.")
        time.sleep(delay)

    def run(self):
        # Clear previous file content
        if os.path.exists(self.output_file):
            os.remove(self.output_file)
        
        for endpoint in self.endpoints:
            self.scrape(endpoint)
            self.wait_random()

if __name__ == "__main__":
    # Base URL of the website you want to scrape
    base_url = "https://www.scrapethissite.com/pages/simple/"

    # Optionally provide a list of endpoints
    # Or leave empty to scrape just the base URL
    endpoints = [
        # "page1",
        # "page2",
        # "page3"
    ]

    # Initialize the scraper bot
    bot = ScraperBot(base_url, endpoints if endpoints else None)
    
    # Run the bot
    bot.run()
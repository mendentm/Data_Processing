import sys
import os
from Data_Analyzer.main import DataAnalyzer
from Scraping_Bot.main import ScraperBot

# Add the Scraping_Bot and Data_Analzer directories to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), 'Data_Analyzer'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'Scraping_Bot'))

def main():
    # You can now instantiate and use the ScraperBot class
    base_url = 'https://www.scrapethissite.com/pages/simple/'
    scraper = ScraperBot(base_url)
    scraper.run()

    analyzer = DataAnalyzer('scraped_data.txt')
    print(analyzer.run_operation('word_count'))

if __name__ == "__main__":
    main()



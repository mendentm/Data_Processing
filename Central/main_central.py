import sys
import os
from Data_Analyzer.main import DataAnalyzer
from Scraping_Bot.main import ScraperBot
from Central.Database.storing_scraped_data import store_file

# Add the Scraping_Bot and Data_Analzer directories to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), 'Data_Analyzer'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'Scraping_Bot'))

def main():

    # You can now instantiate and use the ScraperBot class
    base_url = 'https://www.scrapethissite.com/pages/simple/'
    scraper = ScraperBot(base_url)
    scraped_data = scraper.run()
    
    # Storing the scraped binary into "Data_Processing_Bots" local PosgreSQL server 
    store_file(scraped_data)

    # Analyzing the scraped file 
    analyzer = DataAnalyzer('scraped_data.txt')

    print(analyzer.run_operation('word_count'))

if __name__ == "__main__":
    main()



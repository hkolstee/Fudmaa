from scrapyProject.Scraper import Scraper 

def main():
    newScraper = Scraper("https://www.funda.nl/koop/groningen/", "groningen.json", "json")
    newScraper.run_scraper()

if __name__ == "__main__":
    main()
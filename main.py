from scrapyProject.Scraper import Scraper 

def main():
    # Scraper(*url*, *filename*.*format*, *format*)
    # format has to be one of = json, jsonlines, csv, xml, pickle, marshal
    newScraper = Scraper("https://www.funda.nl/koop/groningen/", "test.json", "json")
    newScraper.run_scraper()

if __name__ == "__main__":
    main()
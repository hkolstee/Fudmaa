from scrapyProject.Scraper import Scraper 
import sys

def main():
    # Scraper(*url*, *filename*, *format*)
    # format has to be one of = json, jsonlines, csv, xml, pickle, marshal
    try:
        newScraper = Scraper(sys.argv[1], sys.argv[2], sys.argv[3])
    except Exception as e:
        print(e)
        sys.exit("\033[91m" + "Usage: python3 main.py *URL* *output_filename* *output_format*" + "\033[0m")
    newScraper.run_scraper()

if __name__ == "__main__":
    main()
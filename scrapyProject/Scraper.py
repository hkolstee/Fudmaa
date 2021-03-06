from scrapyProject.scrapyProject.spiders.fudmaa_spider import FudmaaSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import os
import datetime

class Scraper:
    def __init__(self, url, output_filename, output_format):
        self.url = url
        self.output_filename = output_filename
        self.output_format = output_format

        # set setting.py file path to allow detection of scrapyProject settings 
        #   (can't run this code from outside project folder (Fudmaa) otherwise)
        # use path from Fudmaa folder to settings.py
        os.environ.setdefault('SCRAPY_SETTINGS_MODULE', 'scrapyProject.scrapyProject.settings')
        self.process = CrawlerProcess(get_project_settings())

        # Spider you want to run
        self.spider = FudmaaSpider

        # specify settings (output location and file name/format)
        date = datetime.datetime.now()
        output_filename = "output/" + output_filename + "_" + date.strftime("%d-%m-%Y")+ "." + output_format
        self.process.settings.attributes["FEEDS"].value = {output_filename: {"format": output_format, "overwrite": True}}
        

    def run_scraper(self):
        self.process.crawl(self.spider, domain=self.url)
        self.process.start() # the script will block here until the crawling is finished

import scrapy
import re
from itertools import dropwhile


class FudmaaSpider(scrapy.Spider):
    # Name per spider class has to be unique for a given project.
    name = "fudmaa"


    def __init__(self, **kw):
        super(FudmaaSpider, self).__init__(**kw)
        # get url specified in script
        url = kw.get('url') or kw.get('domain') or 'https://www.funda.nl/koop/groningen/'
        # add 'https://' to url if needed
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'http://%s/' % url
        # define starting url
        self.url = url

    # requests should return iterable
    def start_requests(self):
        return [scrapy.Request(self.url, callback=self.parse)]

    # Method that will be called to handle the response downloaded for each fo the requests made.
    # The response parameter is an instance of TextResponse that holds the page content
    #   and has further helpful methods to handle it.
    # This method usually parses the response, extracting the scraped data as dicts and also
    #   finding new URLs to follow and creating new requests (Request) from them.
    def parse(self, response):

        # Blikkenvanger listings (the bigger listings), normal smaller listings
        for listing in response.css('div.search-result-main, div.search-result-main-promo'):
            # title looks like this: "\r\n              Esserweg 6\r\n        "
            title = listing.css('h2.search-result__header-title.fd-m-none::text').get()
            price = listing.css('span.search-result-price::text').get()
            location = listing.css('h4.search-result__header-subtitle.fd-m-none::text').get()
            living_space = listing.css('span[title="Gebruiksoppervlakte wonen"]::text').get()
            # plot area sometimes not specified
            plot_area = listing.css('span[title="Perceeloppervlakte"]::text').get(default="")
            rooms = listing.css('ul.search-result-kenmerken ').get()
            broker = listing.css('span.search-result-makelaar-name::text').get()
            link = listing.css('a').attrib['href']
            
            yield {
                # clean up data of additional characters
                'title': re.sub('\r\n[ ]*','', title),
                'price': re.sub('\u20ac ','', price),
                'location': re.sub('\r\n[ ]*','', title) + ", " + re.sub('\r\n[ ]*','', location),
                'living_space': re.sub('\u00b2','^2', living_space),
                'plot_area': re.sub('\u00b2','^2',plot_area),
                # number of rooms need to be extracted out of string of couple lines with at multiple times numbers in it
                # subsitute every character but a number out of last 5 characters of string cut off at point " kamers"
                'rooms': re.sub('[^0-9]+','', (rooms.rpartition(' kamers')[0])[-5:]),
                # remove spaces in front and at end of string with .strip()
                'broker': broker.strip(),
                'link': "https://www.funda.nl" + link
            }
        

        next_page = response.css('a[rel="next"]').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
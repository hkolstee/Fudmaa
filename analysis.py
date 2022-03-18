import numpy as np
import json
import re
import sys

# Class with multiple analytic methods
class DataAnalyser:
    def __init__(self, filename):
        self.filename = filename

        # load json file to use in object
        with open('output/' + filename, 'r') as json_file:
            self.json_load = json.load(json_file)

    # Average of all prices in data.
    def averagePrice(self):
        total = 0
        skipped = 0

        for entry in self.json_load:
            price = entry['price']
            if (price == 'Prijs op aanvraag'):
                skipped += 1
            else:
                price = re.sub(' k.k.', '', price)
                price = re.sub(' v.o.n.', '', price)
                price = re.sub('\.', '', price)

                total += int(price)

        average = total/len(self.json_load)
        print("average price: €"  + "{:.2f}".format(average))

    def average
    

def main():
    try:
        analyser = DataAnalyser(sys.argv[1])
    except Exception as e: 
        print(e)
        sys.exit("\033[91m" + "Usage: python3 analyser.py *filename*" + "\033[0m")

    analyser.averagePrice()

if __name__ == '__main__':
    main()



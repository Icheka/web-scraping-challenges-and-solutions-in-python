from urllib.request import urlopen
from urllib.error import URLError
from urllib.error import HTTPError
from bs4 import BeautifulSoup

'''
03: Write a Python program to get the number of datasets currently listed on https://catalog.data.gov/dataset
'''
class Scraper:
    '''
    Loads any webpage and returns an exit code + a string that can either be an error message or the text of the requested webpage
    loadWebPage(url: string): dict
    @props url: string representation of the URL to request
    '''
    def loadWebPage(self, url):
        try:
            page = urlopen(url)
        except URLError:
            return {'code': 1, 'error': 'Remote server not found'}
        except HTTPError:
            return {'code': 2, 'error': 'The request returned an HTTP error'}
        else:
            bs = BeautifulSoup(page.read(), 'html.parser')
            return {'code': 0, 'soup': bs}
    
    def getDatasets(self, url):
        if (isinstance(url, str) != True):
            return {'code': 1, 'error': "URL must be a string."}
        page = self.loadWebPage(url)
        if (page['code'] == 0):
            bs = page['soup']
            datasets = bs.find('div', {'class': 'new-results'})                
            return {'code': 0, 'result': datasets.get_text()}
        else:
            return {'code': 2, 'error': page['error']}

def main():
    url = "https://catalog.data.gov/dataset"
    scraper = Scraper()
    result = scraper.getDatasets(url)
    if (result['code'] == 0):
        print("There are currently {} datasets at {}".format(result['result'], url))
    else:
        print("An error occurred!")
        print("Error: {}".format(result['error']))
        
main()

from urllib.request import urlopen
from urllib.error import URLError
from urllib.error import HTTPError
from bs4 import BeautifulSoup

'''
02: Write a Python program to download and display the contens of robots.txt for https://en.wikipedia.org
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
            return {'code': 0, 'text': bs.prettify()}

    def getRobotsFile(self, url):
        if (isinstance(url, str) != True):
            return {'code': 2, 'msg': "URL must be a string!"}
        page = self.loadWebPage(url)
        if (page['code'] != 0):
            # I use exit codes (0 for success, any other integer for failure)
            # so that the calling function can simply check the exit code
            # and determine if the request was successfu or not
            # without needing to parse the returned string
            return {'code': 1, 'msg': "An error occurred! :>> {}".format(page['error'])}
        return {'code': 0, 'msg': "{}".format(page['text'])}

def main():
    url = "https://en.wikipedia.org/robots.txt"
    scraper = Scraper()
    robots_file = scraper.getRobotsFile(url)
    print(robots_file['msg'])
                
main()

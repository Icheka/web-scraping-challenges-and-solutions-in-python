from urllib.request import urlopen
from urllib.error import URLError
from urllib.error import HTTPError

'''
01: Write a program to test if a given page is found or not on the server
'''

class Scraper:
    # @props url: URL for the resource to be tested
    def doesPageExist(self, url):
        try:
            urlopen(url)
            return 0
        except URLError:
            return 1
        except HTTPError:
            return 2

def main():
    url = "https://google.com"
    scraper = Scraper()
    doesPageExistCode = scraper.doesPageExist(url)

    if doesPageExistCode == 0:
        print("Page exists!")
    elif doesPageExistCode == 1:
        print("Remote server not found")
    elif doesPageExistCode == 2:
        print("The request returned an HTTP error")

main()

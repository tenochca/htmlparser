
from urllib.request import urlopen

def gethtml(fullurl):
    'issue http request, return the html code as a string'
    r = urlopen(fullurl)
    h = r.read().decode()
    return h

from html.parser import HTMLParser

class simpleparser(HTMLParser):
    'parser to get just the tags and data'

    def handle_starttag(self, tag, attrs):
        print('START TAG: ', tag)

    def handle_endtag(self, tag):
        print('END TAG: ', tag)

    def handle_data(self, data):
        d = data.strip()
        print('***'+ d + '***')


fullurl = input('URL: ')
code = gethtml(fullurl)
parser = simpleparser()
parser.feed(code)



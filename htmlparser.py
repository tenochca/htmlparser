
from urllib.request import urlopen

def gethtml(fullurl):
    'issue http request, return the html code as a string'
    r = urlopen(fullurl)
    h = r.read().decode()
    return h

from html.parser import HTMLParser

class ImageParser(HTMLParser):
    'parser to get all the image links in a website'
    def __init__(self):
        HTMLParser.__init__(self)
        self.images = []

    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            #print(tag, attrs)
            for i in attrs:
                if i[0] == 'src':
                    self.images.append(i[1])
                    

fullurl = input('URL: ')
code = gethtml(fullurl)
parser = ImageParser()
parser.feed(code)
imagelist = parser.images
print(imagelist)





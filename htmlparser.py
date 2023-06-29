
from urllib.request import urlopen

def gethtml(fullurl):
    'issue http request, return the html code as a string'
    r = urlopen(fullurl) #imported urlopen function issues http request
    h = r.read().decode() #read method gets the html and decode method decodes the html into legible code
    return h #returning the html code

from html.parser import HTMLParser

class ImageParser(HTMLParser): #created subclass of imported class HTMLParser
    'parser to get all the image links in a website'
    def __init__(self):
        HTMLParser.__init__(self)
        self.images = [] #init counter list for the image links

    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            for i in attrs: #if the start tag is img then the code will iterate through the attributes in that tag
                if i[0] == 'src': #if the first item in the list of attributes is src
                    self.images.append(i[1]) #then add the following link to the list
                     

def getimages(fullurl):
    'function to get the list of image links from a website'
    code = gethtml(fullurl) #getting html code
    parser = ImageParser() #variable 'parser' becomes a imageparser object
    parser.feed(code) #Inherited HTMLParser feed method used on the new parser
    imagelist = parser.images 
    return imagelist #returning the final list

fullurl = input('URL: ')
print(getimages(fullurl))




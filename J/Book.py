class bookScraping:

    def __inti__(self,baseUrl,uri,nbPage):
        self.setBaseUrl(baseUrl)
        self.setUri(uri)
        self.setNbPage = nbPage
        self.urls = []

    def setBaseUrl(self,url):
        response = requests.get(url)
        if response.ok:
            self.baseUrl = url
        else:
            print("Your Url is not OK")
            exit()

    def setUri(self,uri):
        self.uri = uri

    def getLinks(self):
        for i in range(self.nbPage):
            self.urls.append(self.baseUrl + self.uri + str(i))

class Book:

    def __init__(self, name, author, price):
        self.set_name(name)
        self.set_author(author)
        self.set_price(price)

    def set_name(self, name):
        self.name = name

    def set_author(self, author):
        self.author = author

    def set_price(self, price):
        self.price = price

    def get_name(self):
        return self.name

    def get_author(self):
        return self.author

    def get_price(self):
        return self.price



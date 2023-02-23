
from O_Toolkit import Toolkit
from O_BookEntry import BookEntry
from O_Scraper import Scraper
from O_Scrap import Scrap

class Book:
    
    def __init__(self, baseUrl, uri, nbPage):
        self.baseUrl = baseUrl
        self.uri = uri
        self.setPageMax(nbPage)
        self.urls = []
        self.endpoints = []
        self.result = []
        self.finalFileNameFields = [
            "name",
            "authors",
            "price"
            ]
    
    def setPageMax(self, pageMax):
        self.nbPage = pageMax
        return self
    
    def getLinks(self):
        for i in range(self.nbPage):
            self.urls.append(self.baseUrl + self.uri + str(i))
        return self.urls
  
    #pas besoin de Endpoints    
    
    def getFinalFieldNames(self):
        return self.finalFileNameFields
    
    
    
    def getInfoByPage(self, soup):

        fiches = []
        
        
        
        
       

        lis = soup.findAll("li", class_="dct-product clearfix fiche-produit product-availability-01")
        infos = self.swoup(self.base_url + self.uri + str(self.page)) 
        
        for soup in infos:
            books = []
            for book_card in soup:
                name = (book_card.find("a", class_="product-title").text.replace(" ", "").strip())
                author = (book_card.find("div", class_="authors").find("a").text.strip())
                price = (book_card.find("span", class_="final-price").text.strip())
                books.append(Book(name, author, price))
            #return books
        
            try:
                adress = adress.getText()
                cleanArrAdress = []
                for ele in str(adress).split("\n"):
                    #cleanAdress.push(ele)
                    if ele.strip() != "":
                        cleanArrAdress.append(ele.strip())
                
                realAdress = cleanArrAdress[0]
                
            except:
                name= ""
                author= ""
                price= ""
               
                cleanArrAdress = []
                
            fiche = BookEntry(name, author, price)
            fiches.append(fiche)
        
        self.result.extend(fiches)
        return fiches


    
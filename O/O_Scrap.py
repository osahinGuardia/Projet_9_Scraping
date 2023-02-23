from O_scraper import Scraper
from O_Book import O_Book

baseUrl = "https://www.decitre.fr"
uri = "/livres/nouveautes.html?p="
nbPage = 30

bookInstance = Book(baseUrl, uri, nbPage)

scraper = Scraper(bookInstance, "linksList.csv", "infos.csv")

scraper.exec()

print("Done")
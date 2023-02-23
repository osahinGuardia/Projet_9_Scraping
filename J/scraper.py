from bs4 import BeautifulSoup

class Scraping:

    def __init__(self,scrapInstance,linkFile,finalFile):
        self.setScrapInstance(scrapInstance)
        self.setFinalFile(finalFile)
        self.setlinkFile(linkFile)
        self.linkFileNameFields = ["id","category","link"]
        self.finalFileNameFields = self.scrapInstance.getFinalFi

        def setLinNameFields(self, fieldnames):
            self.linkFileNameFields = fieldnames


        def setScrapInstance(self,instance):
            self.scrapInstance = instance
            return self
        
        def setLinkFile(self,filePath):
            self.linkFile = filePath
            return self

        def setFinalFile(self,filePath):
            self.finalFile = filePath
            return self

        def swoup(self):
            if response.ok:
                soup = BeautifulSoup(response.text, 'html.parser')
                try:
                    return process(soup)
                except Exception:
                    print("ERROR: Impossible to process on:" + str(url))
                    return False
            else:
                print("ERROR: Failed to Connect on:"+str(url))

        def swoupMultiple(self,urls,peocess):
            result = []
            for url in urls:
                soup = self.swoup
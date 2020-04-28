class Apple:
    manufacturer = "Apple Inc"
    contactWebsite = "www.apple.com"

    def contactDetails(self):
        print(manufacturer, contactWebsite)

class MacBook(Apple):
    def __init__(self):
        self.yearOfManufacture = 2017

    def manufactureDetails(self):
        print(self.yearOfManufacture,".", self.manufacturer)

macBook = MacBook()
macBook.manufactureDetails()

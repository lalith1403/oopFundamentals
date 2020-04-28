class MusicalInstruments:
    numberOfMajorKeys = 12

class StringInstruments(MusicalInstruments):
    typeOfWood = "ToneWood"

class Guitar(StringInstruments):
    def __init__(self):
        self.numberOfStrings = 6
        print(self.numberOfMajorKeys,self.typeOfWood, self.numberOfStrings)

guitar = Guitar()

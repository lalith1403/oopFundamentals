class OperatingSystem:
    multitasking = True
    name = "MacOS"

class Apple:
    website = "www.apple.com"
    name = "WindowsOS"

class MacBook(Apple,OperatingSystem):
    def __init__(self):
        print(self.name)
        if self.multitasking:
            print("This is a multitasking system. For more details, visit {}".format(self.website))
macBook = MacBook()

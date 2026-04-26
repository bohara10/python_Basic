class Employee:
    company = "ITC"
    name = "default"
    def show(self):
        print(f"The name is {self.name} and the company is {self.company}")


class coder:
    language = "Python"
    def printLanguage(self):
        print(f"out of all the languages here is your language:  {self.language}")

class programmer(Employee, coder):
    company = "Microsoft"
    def showLangauage(self):
        print(f"The name is {self.company} and the language is {self.language}")
    
a = Employee()
b = programmer()
b.show()
b.printLanguage()
b.showLangauage()

print(a.company , b.company)
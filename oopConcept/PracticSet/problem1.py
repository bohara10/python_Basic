class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, language, address):
        self.name = name
        self.salary = salary
        self.language = language
        self.address = address

Rajan = Programmer("Rajan", 5000000, "python", "Ktm")

Roshan = Programmer("Roshan", 4000000, "java", "Lalitpur")

Will = Programmer("Will", 3000000, "c++", "Bhaktapur")

print(Rajan.company, Rajan.name, Rajan.salary, Rajan.language, Rajan.address)
print(Roshan.company, Roshan.name, Roshan.salary, Roshan.language, Roshan.address)
print(Will.company, Will.name, Will.salary, Will.language, Will.address)
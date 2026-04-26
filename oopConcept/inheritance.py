class Employee:
    company = "ITC"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")


# class programmer:
#     company = "Microsoft"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

#     def showLangauage(self):
#         print(f"The name is {self.name} and the language is {self.language}")

class programmer(Employee):
    company = "Microsoft"
    def showLangauage(self):
        print(f"The name is {self.name} and the language is {self.language}")
    
a = Employee()
b = programmer()

print(a.company , b.company)
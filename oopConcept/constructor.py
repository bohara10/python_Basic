class employee:

    language = "python"
    salary = 200000

    def __init__(self, name, salary, language):  # dunder method which is automatically called
        print("I am creating an object")
        self.name = name
        self.salary = salary
        self.language = language

    def getInfo(self):

        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("good morning")


rajan = employee("Rajan", 200000, "python")
# rajan.name= "Rajan"

print(rajan.name, rajan.salary, rajan.language)

#harry = employee()

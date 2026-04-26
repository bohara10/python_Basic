class calculator :

    num = int(input("Enter a number: "))
    # def __init__(self, num):
    #     self.num = num

    def square(self):
        print(f"The square of {self.num} is {self.num ** 2}")

    def cube(self):
        print(f"The cube of {self.num} is {self.num ** 3}") 

    def squareroot(self):
        print(f"The square root of {self.num} is {self.num ** 0.5}")

    @staticmethod
    def greet():
        print("Hello!")

    
calc = calculator()

calc.greet()
calc.square()
calc.cube()
calc.squareroot()
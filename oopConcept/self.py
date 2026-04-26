class employee:
    
    language = "python"   
    salary = 200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("good morning")

rajan = employee()
# # rajan.language = "java"  #
# print(rajan.language, rajan.salary)  
rajan.greet()
rajan.getInfo()


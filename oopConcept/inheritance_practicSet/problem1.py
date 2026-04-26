class two_Dvector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j")
class three_Dvector(two_Dvector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")

        


a = two_Dvector(1, 2)
a.show()

b = three_Dvector( 1, 2, 3)
b.show()






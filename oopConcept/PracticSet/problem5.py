from random import randint

class Train:

    def __init__(self, trainNO):
        self.trainNO = trainNO

    def book(self,  fro, to):
       print(f"Ticket is booked in train no: {self.trainNO} from {fro} to {to}")

    def getStatus(self):
       print(f"Ticket is booked in train no: {self.trainNO} is running on time")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no :{self.trainNO} from {fro} to {to} is {randint(1000, 5000)} ")
   

t1 = Train(12345)

t1.book("Delhi", "Mumbai")
# t1.getStatus(12345, "Delhi", "Mumbai")
# t1.getFare(12345, "Delhi", "Mumbai")

t1.getFare("Delhi", "Mumbai")
t1.getStatus()


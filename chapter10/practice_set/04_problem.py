from random import randint
from random import choice
# List of some Indian cities
indian_cities = [
    "Mumbai", "Delhi", "Bangalore", "Kolkata", "Chennai", "Hyderabad", 
    "Ahmedabad", "Pune", "Jaipur", "Surat", "Lucknow", "Kanpur", 
    "Nagpur", "Indore", "Patna", "Bhopal", "Vadodara", "Coimbatore", 
    "Kochi", "Chandigarh", "Visakhapatnam", "Mohali", "Rajpura"
]
class Train:
    def __init__(self, trainNo):
    # def __init__(self, trainNo, fro, to):
        self.trainNo = trainNo
        # self.fro = fro
        # self.to = to
    def book(self, fro, to):
        print(f"The is book in train no. {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train no. {self.trainNo} is running with Time")

    def getFare(self, fro, to):
        print(f"The is fare in train no. {self.trainNo} from {fro} to {to} is ₹{randint(222, 2506)}")

# Generate a random city
random_city1 = choice(indian_cities)
random_city2 = choice(indian_cities)
# Generate a random train number
t = Train(randint(153, 6001))

t.book(random_city1, random_city2)
t.getStatus()
t.getFare(random_city1, random_city2)
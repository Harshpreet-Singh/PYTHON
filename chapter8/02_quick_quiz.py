def goodday():
    name= input("Please Enter Your Name: ")
    print(f"Hello! {name}\nHave a Good Day")
    name = True
goodday()




#  DOING THE SAME THING USING ARGUEMENTS AS FOLLOWS:

def goodDay(name, ending):
    print("Good Day, " + name)
    print(ending, "\n")

first = input("Enter Name of User_1: ")
second = input("Enter Name of User_2: ")
end = "THANK YOU"

goodDay(first, end)
goodDay(second, end)
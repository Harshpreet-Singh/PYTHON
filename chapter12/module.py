def myFunc():
    print("Hello World! ")

myFunc()
print(__name__)  # this when run in main.py will give name as module as from module we are importing our code

if __name__ == "__main__":
    # If this code is run by its own file
    print("We are directly running this code")
else:
    print("We are indirectly running this code")

# name = ["Harsh", "Hari", "Harman", "Harish", "Rahul", "Bunty", "Rohan", "Shivam"]

enter = input("Enter Your Name Here: ")
for name in enter:
    # if name.lower().startswith("h"):
    if name.lower() == 'h':
        print(f"Hello, {enter}! Nice to meet you.")
        break
    else:
        print(f"Hatt {enter}")
        break


# Get the user's name as input
# user_name = input("Enter your name: ")

# # Use a for loop to check the first letter
# for letter in user_name:
#     if letter.lower() == 'h':
#         print(f"Hello, {user_name}! Nice to meet you.")
#         break  # Exit the loop once we find the first letter 'h'
# else:
#     print("Hello! Your name doesn't start with 'H', but still nice to meet you.")

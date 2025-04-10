# name = "Harshpreet" 
# enter = input("Enter your Name and Know the length of your name: ") 
# end = input("Enter Again: ")

# print(name)
# print(" ")
# print(len(enter), "is the length of your name") # len is used to know length
# print(" ")
# print(enter.endswith("preet"), "it ends with preet")
# print(" ")
# print(enter.endswith(end), "it same")
# print(enter.startswith(end), "it same")
# print(name.find("p")) # to find the place value of any digit only the first one, no repition is entertained

# enter name in enter and enter again in end endswith verifies whether both the entries are same
# ////////////////////////////////////////////////////////////////////////////////////////////////////////
# DUMMY CODE BELOW



name = "harshpreet singh"
CAPS = "    Surinder Singh"
s = "  strip  "
new = "Splits,The, String, Into, a, List"
num = "4564879"
si = "singh"

print(len(name), "is the length of harshpreet")
print(name.endswith("reet")) #it cares about CAPS and non-caps letters
print(name.startswith("Har")) #it cares about CAPS and non-caps letters
print(name.capitalize()) # it capitalize the first letter of first word only
print(CAPS.lower()) # it lowers the first letter of every word
print(name.upper())  # Converts all characters in the string to uppercase.
print(s.strip()) # Removes leading and trailing whitespace from the string.
print(CAPS.replace("Surinder", "Harshpreet")) # Replaces occurrences of a substring with another substring.
# print(name.find("a")) # to find the place value of any digit only the first one, no repition is entertained
print(name.count("e")) # 'e' is 2 times so answer will be 2
print(new.split(",")) # add print(new.split("x")) this 'x' after every word {word should be divided by "," }
print(name.isalpha()) # Returns True if all characters in the string are alphabetic.
print(name.isnumeric()) # Returns True if all characters in the string are numeric.
print(name.count("e")) # .count("x"): Counts how many times 'x' appears in the string. (as a string)
# print(name.count(si)) # .count(x): Counts how many times 'x' appears in the string. (as a varible)
print(si.center(9, '+')) # .center(x, 'y'): Centers the string, x = to belength of string, y = what to be added
print(num.zfill(20)) # .zfill(): Pads the string with zeros on the left to make the string reach a given length
print(new.swapcase())  # .swapcase(): Converts uppercase characters to lowercase and vice versa
print(new.find("a")) 

print("\n")
print("My name is \"Harshpreet\",\n I am a\t good boy") # \" can be used to add ("), \t can be used to give a tab space, \n can be used to break the line 
st = "hey Harshpreet you are amazing!"

enter = str(input("Enter Here: "))

f = open("chapter9\\02_write.txt", "+a")

'''
r = for reading
w = for writing(this replaces the existing line)
a = for appending(this adds more lines at the end)
+ = for updating (use 'w' or 'a' with it as mentioned )
rb = for reading in binary mode
rt = for reading in text mode
'''
f.write("\n")
f.write(enter)

f.close()
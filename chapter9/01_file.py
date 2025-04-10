'''
a = "very long string with emails"


'''

f = open("chapter9\\01_read.txt", "r") 
# used double \\   becuase single is read as code 
# "r" mentioned above means readable    NOT REQUIRED AS AUTOMATICALLY LETS "r"
# "w" means writable
data = f.read()

print(data)
f.close()   # IMPORTANT!
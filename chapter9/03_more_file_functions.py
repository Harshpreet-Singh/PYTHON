f = open("chapter9\\03_more.txt")

# lines = f.readlines()
# readlines() THIS READS FULL FILE AS LIST
# readline() THIS READS ONLY FIRST LINE   number of times you use this number of lines you get
# print(lines, type(lines))


oneLine = f.readline()
while(oneLine != ""): # !=  this means --> not equal to 
    print(oneLine)
    oneLine = f.readline()

f.close()
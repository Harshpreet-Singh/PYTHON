a = "{} is a good {}".format("Harshpreet", "boy")
print(a)
# ----------------------------------------------OR----------------------------------------------
entry1 = input("Enter Your Name: ")
entry2 = input("Enter Your Gender(boy/girl): ")
a = "{1} is a good {0}".format(entry1, entry2)          # this take 0,1 if we write {1}{0} like this output changes
print(a)
f = open("chapter9\\file.txt")
print(f.read())
f.close()
# ^^^^^^^^^^^^^^^^^^^^THE SAME CAN BE WRITTEN USING WITH STATEMENT LIKE THIS^^^^^^^^^^^^^^^^^^^^
print("")
with open("chapter9\\file.txt") as f:
    print(f.read())

# YOU DON'T HAVE TO CLOSE THE FILE BY f.close()

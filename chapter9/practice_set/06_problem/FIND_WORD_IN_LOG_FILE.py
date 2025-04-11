
with open("chapter9\\practice_set\\06_problem\\log.txt") as f:
    lines = f.readlines()
lineNumber = 1
for line in lines:
    if("python" in line):
        print(f"Python is present in line number: {lineNumber}")
        break  # breaking here so else na chale, verna else bhi chal jayega
    lineNumber += 1
else:
    print("No, Python is not present")
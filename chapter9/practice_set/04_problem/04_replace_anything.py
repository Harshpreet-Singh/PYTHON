with open("chapter9\\practice_set\\04_problem\\word.txt", "r") as f:
    content = f.read()

find = str(input("Enter the word with which word you want to replace: "))
replace = str(input(f"Enter the word with which you want to replace {find}: "))

contentNew = content.replace(find, replace)

if(find != ""):
    with open("chapter9\\practice_set\\04_problem\\word.txt", "w") as f:
        f.write(contentNew)
        print(f"Replaced {find} with {replace}")
else:
    print(f"{find} does not exists!")

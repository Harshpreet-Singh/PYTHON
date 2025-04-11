with open("chapter9\\practice_set\\07_problem\\copy.txt") as f:
    copy = f.read()

with open("chapter9\\practice_set\\07_problem\\copy_done.txt", "w") as f:
    f.write(copy)

with open("chapter9\\practice_set\\07_problem\\copy.txt") as f1:
    original_content = f1.read()

with open("chapter9\\practice_set\\07_problem\\copy_done.txt") as f2:
    copied_content = f2.read()


if(original_content == copied_content):
    print("Copied Properly!")
else:
    print("Failed to copy properly!")
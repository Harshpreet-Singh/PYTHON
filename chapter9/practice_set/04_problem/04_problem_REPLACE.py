with open("chapter9\\practice_set\\04_problem\\word.txt", "r") as f:
    content = f.read()

contentNew = content.replace("Donkey", "######")

with open("chapter9\\practice_set\\04_problem\\word.txt", "w") as f:
    f.write(contentNew)


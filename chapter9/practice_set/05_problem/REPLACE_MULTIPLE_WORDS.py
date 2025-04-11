words = ["Donkey", "do", "twinkle", "bad"]
with open("chapter9\\practice_set\\05_problem\\words.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

with open("chapter9\\practice_set\\05_problem\\words.txt", "w") as f:
    f.write(content)
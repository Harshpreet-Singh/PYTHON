f = open("chapter9\\practice_set\\poems.txt")
content = f.read()
if("twinkle" in content):
    print("Twinkle is present in the content ")

else:
    print("Twinkle in not present in the content")

f.close()
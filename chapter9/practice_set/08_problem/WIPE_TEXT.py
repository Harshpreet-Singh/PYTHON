with open("chapter9\\practice_set\\08_problem\\text.txt", "w") as f:
    pass
with open("chapter9\\practice_set\\08_problem\\text.txt", "r") as f1:
    content = f1.read()
    if(content == ""):
        print("Document Cleaned Successfully!")
    else:
        print("Something Went Wrong!")
try:
    with open('chapter12\\practice_set\\01_problem\\1.txt', 'r') as f:
        print(f.read())
except Exception as e:
    print(f"\033[1;91m {e} \033[0m")
try:
    with open('chapter12\\practice_set\\01_problem\\2.txt', 'r') as f:
        print(f.read())
except Exception as e:
    print(f"\033[1;91m {e} \033[0m")
try:
    with open('chapter12\\practice_set\\01_problem\\3.txt', 'r') as f:
        print(f.read())
except Exception as e:
    print(f"\033[1;91m {e} \033[0m")

print("Thank You!")
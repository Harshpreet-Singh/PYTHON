# l = [1,2,3,4,5,6,7,8]
l = [5,6,"Haru",9,4,2,7,3,10,0]

for i, item in enumerate(l):
    if i == 2 or i == 4 or i == 6:
        print(f"Item no. {i+1} is: {item}")
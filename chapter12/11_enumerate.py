l = [3, 53, 535, 65, 85, 97]
# index = 0
# for item in l:
#     index += 1
#     print(f"The Item number at index {index} is {item}")

#  THIS CAN BE SIMPLIFIED USING ENUMERATE FUNCION
for index, item in enumerate(l):
    print(f"The Item number at index {index} is {item}")
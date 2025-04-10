name = input("enter your name :")

import datetime
current_datetime = datetime.datetime.now()
current_date = datetime.date.today()
print(str(current_date))


print(f"\nGood Afternoon, {name} \n")

letter = '''\t \t Dear <|Name|>,
            \t You are selected!
            \t <|Date|> '''



print(letter.replace("<|Name|>", name).replace("<|Date|>", str(current_date)))
# print(letter.replace("<|Name|>", name).replace("2025-04-06", current_datetime))

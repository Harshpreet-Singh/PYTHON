# l = {"Harsh",
#  2, 234.09, "Rohan",True, "Kartik"}

dict={
    "Name": "Harsh",
    "Country": "INDIA",
    "Relegion": "Sikh",
    "Age": 18,
    "Year of Birth": 2007,
    "City": "Banur"
}

# Get an iterator for dictionary items
keys = list(dict.keys())
index = 0



while index < len(keys):
    key = keys[index]
    print(f"{key}: {dict[key]}")
    index += 1
def rem(l, word):
    for item in l:
        l.remove(word)
        return l

l = ["Harsh", "Rohan", "Shubham", "Suvan", "Shivam", "an"]

print(rem(l, "an"))

#   CODE MENTIONED ABOVE MEANS
#   function 'rem'with arguement 'l' and 'word' 
#   for (item) can say 'i' in 'L' i.e. list :
#   now we are in for loop
#   do an action i.e. list mein se remove krdo word ko 
#   word will be defined below
#   and uske baad return krdo mujhe l
#   inshort EK AISA FUNCTION CHALAO JO LIST MEIN SE (WORD)
#          KO REMOVE KRDE AND MUJHE LIST VAPIS DEDE I.E.
#          LIST RETURN KRDE 

print("\n\n\n\n")


def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n

    
l = ["Harsh", "Rohan", "Shubham", "Suvan", "Shivam"]

print(rem(l, "an"))


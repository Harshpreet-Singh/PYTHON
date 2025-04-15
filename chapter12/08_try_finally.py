def main():
    try:
        a = int(input("Hey! Enter a Number: "))
        print(a)
        return
    except Exception as e:
        print(e)
        return
    finally:
        print("I am inside finally")
# CODE IN FINALLY WILL RUN WITH BOTH TRY AND EXCEPT, 
# INSIDE A FUNCTION YOUR CODE(PRINT) WILL NOT RUN WITHOUT FINNALY
# AGAR MAIN FUNCTION MEIN CODE LIKH RHA HU AND MUJHE TRY EXCEPT KE BAAD KUCHH CODE LIKHNA HAI, I HAVE TO WRITE IN FINALLY
# NOT EVEN ELSE, ELSE BHI APKA CODE PRINT NHI KAREGA 
main()
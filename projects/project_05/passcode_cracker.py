import time
import itertools

pas = input("Tell the Password (4 digits only): ")

keys = ['0','1','2','3','4','5','6','7','8','9',
        'a','b','c','d','e','f','g','h','i','j','k','l','m',
        'n','o','p','q','r','s','t','u','v','w','x','y','z']

start_time = time.time()  # Start the timer

attempts = 0

# Generate all possible combinations of given length
for combo in itertools.product(keys, repeat=len(pas)):
    pwg = ''.join(combo)
    attempts += 1

    if pwg == pas:
        end_time = time.time()  # End the timer
        time_taken = end_time - start_time

        print(f"\nThe Passcode is: {pwg}")
        print(f"Total attempts: {attempts}")
        print(f"Time taken to crack: {time_taken:.2f} seconds")
        break

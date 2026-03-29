import itertools
import string
import time
characters=string.ascii_letters+ string.digits+ string.punctuation +" "
# Input taken from user
password=input("Enter the password: ")
n=len(password)
# Brute force password guesser
start_time=time.time()
guesses=itertools.product(characters,repeat=n)
attempt_counter=0
for guess in guesses:
    guessed_pass="".join(guess)
    attempt_counter+=1
    if password==guessed_pass:
        end_time=time.time()
        print(f"Password is {password}")
        print(f"Attempt taken: {attempt_counter}")
        print(f"Time taken:{end_time-start_time} seconds")
        break
else:
    print("Password not found")    

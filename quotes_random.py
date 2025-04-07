import random
from datetime import datetime

time_now = datetime.now()
format_date = time_now.strftime("%B %d, %Y")

quotes = [
    "The future belongs to those who believe in the beauty of their dreams. – Eleanor Roosevelt",
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "Do what you can, with what you have, where you are. – Theodore Roosevelt",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
    "You are never too old to set another goal or to dream a new dream. – C.S. Lewis",
    "Baho kag lobot - Nell"
]
while True:
    user_input = input("Generate a random quote?: Y/N: ")

    if user_input == 'Y' or user_input == 'y':
        print(f"{format_date}")
        print("Quote for today is: ")
        print(random.choice(quotes))
    elif  user_input == 'N' or user_input == 'n':
        print("Okay")
        continue
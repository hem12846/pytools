# this is a multitool wrote in the python programming language

from random import randint
from datetime import datetime
from datetime import time

print("What would you like to do? ")
choice = input(" 1 random number gen\n 2 current date\n 3 calculator ")
#1]  RNG
if choice == '1':
     num1 = int(input("type the first number: "))
     num2 = int(input("type the second number: "))
     result = randint(num1,num2)
     print("your number is: ", result)
#2]  Current date
elif choice == '2':
     print(f'The current date/time is: {datetime.now()}')
#3]  calculator
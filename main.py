# this is a multitool wrote in the python programming language

from random import randint
from datetime import datetime

print("What would you like to do? ")
choice = input(" 1 random number gen\n 2 current date\n 3 calculator ")
if choice == '1':
     num1 = int(input("type the first number: "))
     num2 = int(input("type the second number: "))
     result = randint(num1,num2)
     print("your number is: ", result)

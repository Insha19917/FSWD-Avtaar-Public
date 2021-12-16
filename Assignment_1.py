import random
import math
import datetime

#Taking input from user
uname = input("Enter your Username: ")

#Make a list of strings
id = [i for i in range(0, 10)]

#String initialization
random_str = ""

#For loop initialization
for i in range(6):
    index = math.floor(random.random() * 10)
    random_str += str(id[index])

#Date and time
dt = datetime.datetime.now()

#Displaying the random string
print("\nDetails are: ")
print("\nUsername: ",uname)
print("Your Unique ID is: ",random_str)
print("Date and time is: ",dt.strftime("%d-%m-%Y %H:%M:%S"))

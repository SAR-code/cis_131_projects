'''
script: cis_131_date_time.py
action: demonstrates the datetime module
author: Dylan McCallum
date: 09OCT24
'''

# import required modules
import datetime

# Getting the current time and storing it as x

x = datetime.datetime.now()
y = datetime.datetime.now()

print("Datetime object for x:", x)
print("Datetime object for y:", y)
print("\n\n")

# print the datetime objects individually

print("x's year:", x.year)
print("x's month:", x.month)
print("x's day:", x.day)
print("x's hour:", x.hour)
print("x's minute:", x.minute)
print("x's second:", x.second)

print("y's year:", y.year)
print("y's month:", y.month)
print("y's day:", y.day)
print("y's hour:", y.hour)
print("y's minute:", y.minute)
print("y's second:", y.second)
print("\n\n")

# comparing variables x and y

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x and y are equal")
    

# get the difference between x and y

date_time_difference = y - x
print("The time difference between y and x are: ", date_time_difference)
#!/usr/bin/python3

#Project Euler Problem 1: Sum of all multiples of 3 and 5 up to 1000. 

x = 0
y = 0

for i in range(0,1000,3):
	if i % 5 != 0:
		x += i


for i in range(0,1000,5):
	y += i


print(x+y)

#Result: 233168
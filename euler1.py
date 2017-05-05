#!/usr/bin/python3
x = 0
y = 0

for i in range(0,1000,3):
	if i % 5 != 0:
		x += i


for i in range(0,1000,5):
	y += i


print(x+y)

#!/usr/bin/env python3
message = 'Your grade: '
print('What is your numeric score?')
connection = float(input())
if connection >= 90:
	message = message + 'A'
elif connection >= 80:
	message = message + 'B'
elif connection >= 70:
	message = message + 'C'
elif connection >= 60:
	message = message + 'D'
elif connection <= 50 :
	message = message + 'F'
else:
	message = message + 'is not available.'
print(message)

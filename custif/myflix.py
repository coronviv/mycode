#!/usr/bin/env python3
message = 'The movie is about to begin, we recommed '
print('What is your connection speed in Mbps?')
connection = float(input())
if connection >= 25:
	message = message + 'setting video to 4k.'
elif connection >= 2:
	message = message + 'setting video to 720p.'
else:
	message = message + 'finding another access network.'
print(message)
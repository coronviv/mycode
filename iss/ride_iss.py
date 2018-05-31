#!/usr/bin/env python3

import urllib.request
import json
## Trace the ISS
majortom = 'http://api.open-notify.org/astros.json'

## Call the webservice
groundctrl = urllib.request.urlopen(majortom)

## put fileobject into helmet
helmet = groundctrl.read()

## decode json to python data structure
helmetson = json.loads(helmet.decode('utf-8'))

## display our pythonic data
print("\n\nConverted python data")
print(helmetson)

print("\n\nPeople in Space: ", helmetson['number'])
people = helmetson['people']
print(people)

###
##
#
astronauts=["Eddie Kopra","James Peake","Yuri Kopra","Buzz Aldrin"]
mission=astronauts
print("\nPeople in space: ",astronauts['number']
print(mission+" on the ISS")


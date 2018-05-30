#!/usr/bin/env python3

#My function that opens a file, writes arguments, and closes.
def newtfile(string1, string2, string3):
    vfo = open("newtfile.txt","a") #vivian file object
    print(string1, string2, string3, file = vfo)
    vfo.close()
choice = " "
while(choice.lower()!="q"):  #extra
    x = input("Give me a string: ")
    y = input("Give me a string: ")
    z = input("Give me a string: ")
    choice = input("q to quit")
    newtfile(x, y, z)


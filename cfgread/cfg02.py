#!/usr/bin/env python3
## create file object in "r"ead mode
configfile = open('vlanconfig.cfg', 'r')

## display file to the screen - .read()
configblog = configfile.read()

## break configblog.splitlines()
configlist = configfile.read()

## display list with no '\n'
print(configlist)

## Always close your file
configfile.close()

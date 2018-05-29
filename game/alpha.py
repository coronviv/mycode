#!/usr/bin/env python3
#
while(True):
    vmessage = 'This Seattle landmark is '
    print('How high is the Space needle in ft?')
    vconnection = float(input())
    if vconnection == 605:
        vmessage = vmessage + '605ft high!'
        print(vmessage)
        break
    elif vconnection >= 606:
        vmessage = vmessage + 'less than that.'
    elif vconnection >= 0:
        vmessage = vmessage + 'more than that.'
    else:
        vmessage = 'Try again.'
    print(vmessage)
#
while(True):
    jmessage = 'This Seattle landmark is ' 
    print('How high is Mount Rainier in ft?')
    jconnection = float(input())
    if jconnection == 14411:
        jmessage = jmessage + '14411ft high!'
        print(jmessage)
        break
    elif jconnection >= 14412:
        jmessage = jmessage + 'less than that.'
    elif jconnection >= 0:
        jmessage = jmessage + 'more than that.'
    else:
        jmessage = 'Try again.'
    print(jmessage)

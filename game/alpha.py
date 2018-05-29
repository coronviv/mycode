#!/usr/bin/env python3
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
#
while(True):
    cmessage = 'This Seattle landmark is ' 
    print('How high is the Great Wheel in ft?')
    cconnection = float(input())
    if cconnection == 175:
        cmessage = cmessage + '175ft high!'
        print(cmessage)
        break
    elif cconnection >= 176:
        cmessage = cmessage + 'less than that.'
    elif cconnection >= 0:
        cmessage = cmessage + 'more than that.'
    else:
        cmessage = 'Try again.'
    print(cmessage)
#
while(True):
    ymessage = 'This Seattle landmark is ' 
    print('How high is the Doppler building in ft?')
    yconnection = float(input())
    if yconnection == 524:
        ymessage = cmessage + '524ft high!'
        print(ymessage)
        break
    elif yconnection >= 525:
        ymessage = ymessage + 'less than that.'
    elif yconnection >= 0:
        ymessage = ymessage + 'more than that.'
    else:
        ymessage = 'Try again.'
    print(ymessage)
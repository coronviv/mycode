#!/usr/bin/env python3
#
numwrong=0
x=5
#
while(numwrong<5):
    vmessage = 'This Seattle landmark is '
    print('How high is the Space needle in ft?')
    vconnection = float(input())
    if vconnection == 605:
        vmessage = vmessage + '605ft high!'
        print(vmessage)
        break
    elif vconnection >= 606:
        numwrong=numwrong+1
        vmessage = vmessage + 'less than that.'
    elif vconnection >= 0:
        numwrong=numwrong+1
        vmessage = vmessage + 'more than that.'
    else:
        numwrong=numwrong+1
        vmessage = 'Try again.'
#
while(numwrong<5):
    jmessage = 'This Seattle landmark is ' 
    print('How high is Mount Rainier in ft?')
    jconnection = float(input())
    if jconnection == 14411:
        jmessage = jmessage + '14411ft high!'
        print(jmessage)
        break
    elif jconnection >= 14412:
        numwrong=numwrong+1
        jmessage = jmessage + 'less than that.'
    elif jconnection >= 0:
        numwrong=numwrong+1
        jmessage = jmessage + 'more than that.'
    else:
        numwrong=numwrong+1
        jmessage = 'Try again.'
    if numwrong<5:
        print('You win!')
    else:
        print('Nice try!')
#
while(numwrong<5):
    cmessage = 'This Seattle landmark is ' 
    print('How high is the Great Wheel in ft?')
    cconnection = float(input())
    if cconnection == 175:
        cmessage = cmessage + '175ft high!'
        print(cmessage)
        break
    elif cconnection >= 176:
        numwrong=numwrong+1
        cmessage = cmessage + 'less than that.'
    elif cconnection >= 0:
        numwrong=numwrong+1
        cmessage = cmessage + 'more than that.'
    else:
        numwrong=numwrong+1
        cmessage = 'Try again.'
#
while(numwrong<5):
    ymessage = 'This Seattle landmark is ' 
    print('How high is the Doppler building in ft?')
    yconnection = float(input())
    if yconnection == 524:
        ymessage = ymessage + '524ft high!'
        print(ymessage)
        break
    elif yconnection >= 525:
        numwrong=numwrong+1
        ymessage = ymessage + 'less than that.'
    elif yconnection >= 0:
        numwrong=numwrong+1
        ymessage = ymessage + 'more than that.'
    else:
        numwrong=numwrong+1
        ymessage = 'Try again.'
if numwrong<5:
    print('You win!')
else:
    print('Nice try!')
        


#!/usr/bin/env python3
try:
    print
    raise IOerror
except ZeroDivisionError:
    print("Computers do not like div by zero")
except IOError:
    print("This code raised an IO error")
except:
    print("We're sorry, something unexpected happened. See your IT department.")

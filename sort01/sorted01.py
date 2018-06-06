#!/usr/bin/env python3

vendors=['cisco','juniper','big_ip','f5','arista', 'hp']
print("Currently the value of the vendor:", vendors)
print("\nThe results of sorted() function:", sorted(vendors))
print("\nBut the value of the list hasn't actually changed:", vendors)
sortedvendors=sorted(vendors)
print("Our sorted vendor list looks like this: "+str(sortedvendors))
baksortvendors=sorted(vendors,reverse=True)
print("Our sorted vendor list looks like this: ", baksortvendors)

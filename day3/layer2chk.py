#!/usr/bin/env python3
while(True):
   l2proto = input("Enter a network protocol: ") 

   if l2proto.lower() == "eth": 
      print("ethernet protocol allowed")
      break
   elif l2proto.lower() == "fc":
      print("fiber channel NOT allowed")
      break
   elif l2proto.lower() == "ifb":
      print("infiniband NOT allowed")
      break
   elif l2proto.lower() == "otn":
      print("Optical Network allowed")
      break
   else:
      print("No idea what that technology is")

#!/usr/bin/env python3
#
## sudo apt install python3-pip
#
## pip install pyexcel
## python3 -m pip install pyexcel
## python3 -m pip install pyexcel-xls
import pyexcel
#
# Request data from user
def get_ip_data():
    vinput_ip=input("What is the IP address? ")
    vinput_subnet=input("\nWhat is the subnet associated with this ip? ")
    vinput_vlan=input("\nWhat is the vlan associated with this ip? ")
    v = {"IP": vinput_ip, "subnnet": vinput_subnet, "vlan": vinput_vlan}
    return v
#
## IP is the first column, subnet is the second column, vlan is the third column.
## vlistdict = [ {"IP": "172.16.2.10", "subnet": "255.255.255.0", "vlan": "210"}, {"IP": "172.16.2.20", "subnet": "255.255.255.0", "vlan": "210"} ]
## pyexcel.save_as(records=vlistdict, dest_file_name="ip_vlan_schema.xls")
#
# Runtime
vlistdict = []  # this will be our list we turn into a *.xls file
#
print("Hello! This program will make you a *.xls file")
#
while(True):
    vlistdict.append(get_ip_data()) # add an item to the list returned by get_ip_data() {"IP": value, "subnet": value, "vlan": value}
    vcontinue = input("\nWould you like to add another value? Enter to continue, or enter 'q' to quit: ")
    if (vcontinue.lower() == 'q'):
        break
    elif (vcontinue.lower() == 'n'):
        break
    elif (vcontinue.lower() == 'no'):
        break
#
vfilename = input("\nWhat is the name of the *.xls file? ")
#
pyexcel.save_as(records=vlistdict, dest_file_name=vfilename+".xls")
#
print("The file " + vfilename + ".xls should be in your local directory")

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
    vsite=input("What is the site? ")
    vswitch_hostname=input("\nWhat is the switch hostname? ")
    vswitch_location=input("\nWhat is the switch location (Bldg_Room_Row_Rack)? ")
    vinput_ip=input("\nWhat is the IP address? ")
    vinput_subnet=input("\nWhat is the subnet associated with this ip? ")
    vinput_vlan=input("\nWhat is the vlan associated with this ip? ")
    v = {"site": vsite, "hostname": vswitch_hostname, "location": vswitch_location, "IP": vinput_ip, "subnnet": vinput_subnet, "vlan": vinput_vlan}
    return v
#
## Site is the first column, Switch Hostname is the second column, Switch Location is the third column, IP is the fourth column, Subnet is the fifth column, VLAN is the sixth column.
## vlistdict = [ {"vsite": "TLG", "vswitch_hostname": "TLG-U01-AS-01", "vswitch_location": "Bldg_TLG_Room_5_Row_1_Rack_1", "IP": "172.16.2.10", "subnet": "255.255.255.0", "vlan": "210"}, "vsite": "TLG", "vswitch_hostname": "TLG-U01-AS-02", "vswitch_location": "bldg_TLG_room_5_row_1_rack_1", {"IP": "172.16.2.20", "subnet": "255.255.255.0", "vlan": "210"} ]
## pyexcel.save_as(records=vlistdict, dest_file_name="ip_vlan_schema.xls")
#
## Runtime
vlistdict = []  # this will be our list we turn into a *.xls file
#
print("Hello! This program will make you a *.xls file")
#
while(True):
    vlistdict.append(get_ip_data()) # add an item to the list returned by get_ip_data() {"site": value, "hostname": value, "location": value, "IP": value, "subnet": value, "vlan": value}
    vcontinue = input("\nWould you like to add another value? Enter to continue, or enter 'q' to quit: ")
    if (vcontinue.lower() == 'q'):
        break
    elif (vcontinue.lower() == 'n'):
        break
    elif (vcontinue.lower() == 'no'):
        break
    elif (vcontinue.lower() == 'exit'):
        break
#
vfilename = input("\nWhat is the name of the *.xls file? ")
#
pyexcel.save_as(records=vlistdict, dest_file_name=vfilename+".xls")
#
print("The file " + vfilename + ".xls should be in your local directory")

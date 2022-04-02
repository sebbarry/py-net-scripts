"""
We want to make sure that all the ips in a file are valid 
and not reserved 
"""

import os
import sys
import subprocess


def valid():
    #check the user for input of a file 
    ip_file = input("Enter file name: ")
    if os.path.isfile(ip_file): 
        print("valid file...")
    else: 
        print("file not found..")
        sys.exit()
                                # r for reading
    open_file = open(ip_file, 'r')
    open_file.seek(0) # start from teh beginning of the file
    list = open_file.readlines()
    open_file.close()
    return list

def ip_addr_valid(list=None):
    #plumbing
    if list is None: 
        print("no files found in file.")
        sys.exit()
    if len(list) == 0: 
        print("no files found in file. ")
        sys.exit()

    #validate each ip address in the list.
    for i in list: 
        i = i.rstrip("\n") #strip escape characters
        # make a list of octects
        octet_list = i.split('.')
        if (len(octet_list) == 4) and (1 <= int(octet_list[0]) <= 223) and (int(octet_list[0]) != 127) and (int(octet_list[0]) != 169 or int(octet_list[1]) != 254) and (0 <= int(octet_list[1]) <= 255 and 0 <= int(octet_list[2]) <= 255 and 0 <= int(octet_list[3]) <= 255):
            #now try and reach the ip
            reach_ip(i)
            continue
        else: 
            print("%s is invalid. ", i)


def reach_ip(ip=None): 
    if ip == None: 
        print("unreachable. ip is None")
        return
     
    ping_reply = subprocess.call(
            'ping %s /n 2' % (ip), 
            stdout=subprocess.DEVNULL, 
            stderr=subprocess.DEVNULL
            )

    if ping_reply == 0: 
        print("\n* {} is reachable :)\n".format(ip))
    else: 
        print('\n* {} not reachable :(check connectivity and try again.)'.format(ip))
        sys.exit()



if __name__ == "__main__":
    ip_addr_valid(valid())

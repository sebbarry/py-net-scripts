import random
import sys

def subnet_calc():
    try: 
        print("\n")
        while True: 
            ip_address = input("Enter an IP address: ")
            ip_octets = ip_address.split('.')
            if (len(octet_list) == 4) and (1 <= int(octet_list[0]) <= 223) and (int(octet_list[0]) != 127) and (int(octet_list[0]) != 169 or int(octet_list[1]) != 254) and (0 <= int(octet_list[1]) <= 255 and 0 <= int(octet_list[2]) <= 255 and 0 <= int(octet_list[3]) <= 255):
                break
            else: 
                print("\nThe IP address is invalid. Pleaes try again\n")
                continue

        #valid subnet masks.
        masks = [255, 254,252, 248,240,224,192,128,0]

        while True: 
            subnet_mask = input("Enter the subnet mask: ")
            mask_octets = subnet_mask.split('.')
            if (len(mask_octets) == 4) and (int(mask_octets[0]) == 255) and (int(mask_octets[1]) in masks) and (int(mask_octets[2]) in masks) and (int(mask_octets[3]) in masks) and (int(mask_octets[0]) >= int(mask_octets[1]) >= int(mask_octets[2]) >= int(mask_octets[3])):
                break
            else: 
                print("\nThe subnet mask is INVALID please try again\n")

            #convert values;
            mask_octets_binary= [
                    convert_tobin(x) 
                    for x in masks
                    ]
            binary_mask = "".join(mask_octets_binary)
            #Counting host bits in the mask and calculating number of hosts/subnet
            no_of_zeros = binary_mask.count("0")
            no_of_ones = 32 - no_of_zeros
            no_of_hosts = abs(2 ** no_of_zeros - 2) 
            #return a positive value for the /32 mask (all 255s)
             
             
            wildcard_octets = []
             
            for octet in mask_octets:
                wild_octet = 255 - int(octet)
                wildcard_octets.append(str(wild_octet))
                
             
            wildcard_mask = ".".join(wildcard_octets)

def convert_tobin(octet_value): 
    temp = bin(int(octet_value)).lstrip('0b')
    return temp.zfill(8)


if __name__ == "__main__":
    subnet_calc()

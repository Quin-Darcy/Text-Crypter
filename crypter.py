#!/usr/bin/env python3
#======================================================================================#
#======================================================================================#
#   AUTHOR: QUIN DARCY                                                                 #
#   DATE:   07/29/21                                                                   #
#   DESCRIPTION: This programs uses the fixed length one-time pad Shannon cypher and   #
#   appllies it to a given .TXT file. The encrypted file can then be decrypted by      #
#   changing the flag from 'e' to 'd'.                                                 #
#======================================================================================#
#======================================================================================#
import sys
import math
import random

#===========================================================================#
#                          Fixed-Length One-Time Pad                        #
#===========================================================================#
def FLOTP_KEY(msg):
    bin_msg = ''.join(format(ord(i), '08b') for i in msg)
    L = len(bin_msg)

    key = ['0'] * L
    num_of_ones = random.randint(0, L)
    for i in range(num_of_ones):
        m = random.randint(0, L-1)
        key[m] = '1'

    return ''.join(key)

def FLOTP_E(key, msg):
    bin_msg = ''.join(format(ord(i), '08b') for i in msg)
    L = len(bin_msg)

    encoded_msg = [0] * L
    for i in range(L):
        encoded_msg[i] = str((int(bin_msg[i]) + int(key[i])) % 2)

    msg_str = ''.join(encoded_msg)
    enc_str = ''.join(chr(int(msg_str[i*8:i*8+8],2)) for i in range(len(msg_str)//8))

    return enc_str

def FLOTP_D(key, msg):
    decoded_msg = [0] * len(msg)
    for i in range(len(msg)):
        decoded_msg[i] = str((int(msg[i]) + int(key[i])) % 2)
    msg_str = ''.join(decoded_msg)

    return ''.join(chr(int(msg_str[i*8:i*8+8],2)) for i in range(len(msg_str)//8))

#===========================================================================#
#                               Extract Message                             #
#===========================================================================#
def get_msg(file_path):
    msg = []
    file = open(file_path, 'r')
    for line in file:
        msg.append(line)
    msg = ''.join(msg)
    file.close()
    
    return msg

#===========================================================================#
#                              Make Ecrypted File                           #
#===========================================================================#
def write_file(key, enc_msg, new_file):
    file = open(new_file, 'w')
    file.write(enc_msg)
    file.close

    file = open(new_file, 'a')
    key = ''.join(chr(int(key[i*8:i*8+8],2)) for i in range(len(key)//8))
    file.write(key)
    file.close()

#===========================================================================#
#                               Extract Key                                 #
#===========================================================================#
def extract_key(msg, file_path):
    bin_msg = ''.join(format(ord(i), '08b') for i in msg)
    L = int(len(bin_msg) / 2)
    key = [bin_msg[i] for i in range(L, len(bin_msg))]
    key = ''.join(key)

    msg = [bin_msg[i] for i in range(0, L)]
    msg = ''.join(msg)
    msg = ''.join(chr(int(msg[i*8:i*8+8],2)) for i in range(len(msg)//8))
    file = open(file_path, 'w')
    file.write(msg)
    file.close()

    return key


#===========================================================================#
#                               Error Message                               #
#===========================================================================#
def check_error(args):
    if (len(args) != 4): 
        print('Usage: crypter [OPTION] SOURCE DESTINATION\n')
        print('Mandatory options:')
        print('     e       encrypt SOURCE. New file saved to DESTINATION.')
        print('     d       decrypt SOURCE. New file saved to DESTINATION.')
        return False
    elif(args[1] != 'e' and args[1] != 'd'):
        print('Usage: crypter [OPTION] SOURCE DESTINATION\n')
        print('Mandatory options:')
        print('     e       encrypt SOURCE. New file saved to DESTINATION.')
        print('     d       decrypt SOURCE. New file saved to DESTINATION.')
        return False
    else:
        return True

#===========================================================================#
#                                   Main                                    #
#===========================================================================#
def main(args):
    no_error = check_error(args)

    if (no_error):
        flag = str(args[1])
        file_path = str(args[2])
        new_file = str(args[3])

        if (flag == 'e'):
            msg = get_msg(file_path)
            key = FLOTP_KEY(msg)
            enc_msg = FLOTP_E(key, msg)
            write_file(key, enc_msg, new_file)
        elif(flag == 'd'):
            msg = get_msg(file_path)
            key = extract_key(msg, file_path)
            msg = get_msg(file_path)
            bin_msg = ''.join(format(ord(i), '08b') for i in msg)
            dec_msg = FLOTP_D(key, bin_msg)
            file = open(new_file, 'w')
            file.write(dec_msg)
            file.close()

if __name__ == '__main__':
    main(sys.argv)

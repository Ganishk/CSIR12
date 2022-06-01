#!/usr/bin/env python3
# Source Code: https://drive.google.com/file/d/1X9dSklyYWVHtvB208ccAL3EHVKTYt4cx/view?usp=sharing
from getpass import getpass;
#Used to get password as silent or hidden and it is default library atleast in UNIX systems
import os

def passwd():
 while True:
    password = getpass("\nEnter your password: ")
####Note: Entering password is not visible due to security reasons
####But printed in a statement as plaintext for verification
    SECUREPASS = 0b0000
    # 1st bit -> lowercase check
    # 2nd bit -> uppercase check
    # 3rd bit -> number check
    # 4th bit -> symbol check
    print("The password that you entered is:",password,'\n')
    if not 6<= len(password) <= 16:
        print("Password length mismatch\nRetry."); continue
    for x in password:
        SECUREPASS |= (ord('a')<=ord(x)<=ord('z')) \
                | 0b10*(ord('A')<=ord(x)<=ord('Z'))\
                | 0b100*(ord('0')<=ord(x)<=ord('9'))\
                | 0b1000*( x in "$#@" ) #Given to check these three symbols only
        #Even if we use if clause it'll check all these conditions

    if not SECUREPASS&1 :
        print("[-] Your password doesn't contain a lowercase letter [a-z]")
    if not SECUREPASS&2:
        print("[-] Your password doesn't contain an uppercase letter [A-Z]")
    if not SECUREPASS&4:
        print("[-] Your password doesn't contain an integer digit [0-9]")
    if not SECUREPASS&8:
        print("[-] Your password doesn't contain a symbol from $#@")
    if SECUREPASS==0b1111:
        print("\n[+] Congrats, you entered a strong password with our rules")
        break;
    print("Retry.")

def ascDesc():
    x = int(input("Enter no. of numbers to print: "))
    #Given example is x = 9
    for i in range(1,x+1): print(f'{i}-----{x-i+1}')

def ipInc():
 while True:
    IPSEP=" "
    ipoctet = tuple(map(int,input("Enter the ipv4 address separated by space: ").split(IPSEP)))
    if len(ipoctet)!=4 or any(filter(lambda x: x>=256 or x<0,ipoctet)):
        print("[!] Please enter a valid IPv4 address.");continue

    print("The next set of five IP address are,")

    toInt = lambda iptup: eval('0b'+''.join(map(lambda x: bin(x)[2:].zfill(8),iptup)))
    #Returns the out put as 32 bit integer
    toIP = lambda ipInt: tuple(map(eval,
        ['0b'+bin(ipInt)[2:].zfill(32)[8*i:8*(i+1)] for i in range(4)]))
    #Returns the ouptput as ipOctect
    NO_OF_IP=5
    for x in range(NO_OF_IP):
        ipInt = toInt(ipoctet)+x
        if ipInt > 0xFF_FF_FF_FF:
            print("Local broadcast IP reached.")
            #print("IP address out of range")
            break
        print(" ".join(map(str,toIP(ipInt))))
    else: break
    break

def main():
    options = (exit, passwd, ascDesc, ipInc )
    print("""What you want to do?
    1. Secure Password
    2. Ascending and Descending numbers
    3. IP increment
    0. Exit
Enter your option [0-3]: """,end="")
    opt = int(input())
    print()
    options[opt]()
    print("_"*os.get_terminal_size().columns+"\n")

if __name__=='__main__':
    while True:
        try:main()
        except KeyboardInterrupt:print("Program is exiting...");exit()

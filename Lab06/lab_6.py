#!/usr/bin/env python3

#from math import log10
"""Uncomment to here to format the triangle numbers
both efficiently and neatly"""

def specialSum():
    n = [int(input(
        f"Enter the {i} number: ")) for i in ("first","second")]
    S = sum(n)
    S = 50 if 25<=S<=50 else 60 if 50<S<=60 else S;
    return S


def trigPattern():
    """Note: The triangle can only be formed it is a triangle
    number(1,3,6,10,15,..) else we cannot form a triangle.
    instead we can take input as row and form a triangle of n rows"""
    n = int(input("Enter the no. of rows in the triangle: "))
    if n<0: raise ValueError;



    #n*(n-1)/2 can be taken as order of n**2
    #Word width default value 4 if log10 is undefined
    #assuming 2 digit numbers are used
    #Override if log10 function is defined

    """Uncomment the below line to neatly format higher order values"""
    #from math import log10
    if 'log10'in dir():
        n_deci = int(2*log10(n))
        W_WIDTH = n_deci + (n_deci&1)+2
    else: W_WIDTH = 4

    triangle_base = W_WIDTH*n-1
    S = 0;s="\n"
    for y in range(1,n+1):
        t=''
        for x in range(y):
            S+=1
            t=str(S).ljust(W_WIDTH)+t
        s+=t.center(triangle_base)+"\n"
    return s;

def nameStr():
    pass


def main():
    funcs = [exit,specialSum,trigPattern,nameStr]
    opt = input("""
What you want to do?
    1. Special sum of numbers
    2. Pattern of a triangle
    3. Name as a string
    0. Exit
Enter your option[0-3]: """)
    try:ans = funcs[int(opt)]();
    except IndexError: print("Please enter a valid option");return;
    except UnboundLocalError: print("Please enter a valid option");return;
    except ValueError: print("Please enter a correct value");return;
    print("The answer is:"+str(ans))

LETTERS = {"a":"""
   #
  # #
 #####
#     #
#     #""",
"b":"""
###
#  #
###
#  #
###""",
"c":"""
####
#
#
#
####""",
"d":"""
###
#  #
#  #
#  #
###""",
"e":"""
####
#
####
#
####""",
"f":"""
####
#
###
#
#""",
"g":"""
####
#
# ##
#  #
####""",
"h":"""
#   #
#   #
#####
#   #
#   #""",
"i":"""
###
 #
 #
 #
###""",
"j":"""
 ###
  #
  #
# #
 ##""",
"k":"""
#  #
# #
##
# #
#  #""",
"l":"""
#
#
#
#
####""",
"m":"""
#   #
## ##
# # #
#   #
#   #""",
"n":"""
#   #
##  #
# # #
#  ##
#   #""",
"o":"""
 ###
#   #
#   #
#   #
 ###""",
"p":"""
####
#   #
####
#
#""",
"q":"""
 ###
#   #
#   #
#  ##
 ### #""",
"r":"""
###
#  #
###
# #
#  #""",
"s":"""
####
#
####
   #
####""",
"t":"""
#####
  #
  #
  #
  #""",
"u":"""
#   #
#   #
#   #
#   #
 ###""",
"v":"""
#   #
#   #
#   #
 # #
  #""",
"w":"""
#       #
#       #
#   #   #
 # # # #
  #   #""",
"x":"""
#   #
 # #
  #
 # #
#   #""",
"y":"""
#   #
 # #
  #
  #
  #""",
"z":"""
#####
   #
  #
 #
#####"""}


if __name__=="__main__":
    for x in LETTERS: print(LETTERS[x])
    while True:
        try:main()
        except KeyboardInterrupt: print();exit()

#!/usr/bin/env python3

def cFromF(Ftemp):
    return (Ftemp-32)*5/9

def getF():
    F = float(input("Enter the temperature in Farenheit: "))
    return F

def outStr(C):
    print("The given temperature in centigrade is %.2f\u2103"%C)

def main():
    outStr(cFromF(getF()))

if __name__=="__main__": main()

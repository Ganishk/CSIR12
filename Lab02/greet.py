#!/usr/bin/env python3

def greet(name):
    print("Hi {0}, welcome to programming in Python3".format(name))

def getName():
    return input("Enter your name: ")

def main():
    greet(getName())

if __name__=="__main__":
    main()

#!/usr/bin/env python3
"""This file contains almost all str methods in pythons"""
import os

if __name__=="__main__":
    #Entry point as script starts here
    T_WIDTH = os.get_terminal_size().columns
    print("Single parameter methods".center(T_WIDTH)+'\n')
    s1 = input("Enter your first string: ")
    heading = lambda head: print("\n"+head.center(T_WIDTH))

    heading("Boolean methods")
    #This section describes all the default boolean functions on single string object in python3
    #Methods such as endswith and startswith are not demonstrated here
    for x in 'alnum,alpha,ascii,decimal,digit,identifier,lower,numeric,printable,space,title,upper'.split(','):
        print(("Is"+x).ljust(12)+":",eval('str.is'+x+'(s1)'))
    else: print()

    heading("Case Operations")
    #This section illustrates the case operations of ascii characters in python3
    for op in 'capitalize,casefold,lower,swapcase,title,upper'.split(','):
        print(op.capitalize().ljust(10)+':',eval('str.'+op+'(s1)'))

    print()
    heading("Double parameter methods")
    print()
    s2 = input("Enter your second string with a delimiter: ")
    dl = input("Enter your delimiter of 2nd string: ")
    heading("Justification Methods")
    #This section describes the justifications of strings with the width as T_WIDTH
    for x in "ljust,center,rjust,zfill".split(','):
        print(x.capitalize().ljust(8)+':',eval(f'str.{x}(s1,T_WIDTH-8-2)'))

    heading("Delimitter and repititive count methods")
    #This section describes the operations performed with a delimitter and other
    #short strings that are used in this method efficiently.
    for x in 'count,find,lstrip,rsplit,rstrip,split'.split(','):
        print(x.capitalize().ljust(8)+':',eval('str.{x}(s2,dl)'.format(x=x)))

    print()
    heading("Triple parameter methods")
    print()
    jd = "Enter a 2nd delimited to join: "
    jd = input(jd)
    print("\nJoined string: ",str.join(jd,s2.split(dl)))
    #Actually join function is a double input method.
    print("\nEnter a substring to replace from 2nd string {%s}"%s2,end=": ")
    s3 = input()
    s4 = input("Enter a new string to be replaced: ")
    print("\nThe replaced string is:",str.replace(s2,s3,s4))

    heading("THE END");

    """Sample input:
s1= Ganishk
s2= fsahewlewjskjlfwlejkljwfjsffsklfjaskfjslkfajsffwqfsawrfwafaf
dl= f
jd= ;
s3= hewlew
s4= 114121031"""

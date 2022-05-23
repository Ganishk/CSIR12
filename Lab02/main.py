#!/usr/bin/env python3

from helloWorld import sayHello as hello
from greet import main as greetings
from cToF import main as celcius
from extrema import main as extrema
import os

def main():
    opts = {
            1: "hello",
            2: "greetings",
            3: "celcius",
            4: "extrema",
            0: "exit"
        }
    for x in opts:
        print(f"\t{x}. {str.capitalize(opts[x])}")
    else:
        opt = input(f"Enter your option(0-{len(opts)}): ")
    print()
    try:
        exec(opts[int(opt)]+"()")
    except ValueError: print("Please enter correct value.")
    except KeyError: print("Please enter valid option.")
    except KeyboardInterrupt: pass
    print("_"*os.get_terminal_size().columns+"\n")

if __name__=="__main__":
    while True: main()

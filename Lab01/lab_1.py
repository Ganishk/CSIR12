#!/usr/bin/env python3

import os

print(" GANISHK D-114121031 ".center(os.get_terminal_size().columns,'\u2207')+'\n')

num = [ int(eval(f"input('Enter number {x} : ')")) for x in (1,2) ]

for x in list("+-%*/")+"// ** >> <<".split() + list("&|^"):
    try: exec(f"print('{num[0]} {x} {num[1]} =',{num[0]}{x}{num[1]})")
    except ZeroDivisionError: print("The divisor is zero")

else:
    print(f'~{num[0]} =',~num[0])

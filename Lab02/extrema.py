#!/usr/bin/env python3

from functools import reduce

for x,y in zip("><",("Max","Min")):
    exec(f"""
def get{y}(vals):
    return reduce(lambda x,y: x if x{x}y else y, vals)
    """)

def main():
    NUM = 3
    vals = [float(input(f"Enter number {x}: ")) for x in range(1,NUM+1)]
    minVal = getMin(vals) #minimum value
    maxVal = getMax(vals) #maximum value
    for x in "min","max":
        exec(f"""
print("The {x}imum value is",{x}Val)
        """)

if __name__=="__main__":
    try:
        main()
    except ValueError:
        print('Please give correct input.\n')
        main()
    except KeyboardInterrupt: pass

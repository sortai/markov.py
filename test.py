#!/usr/bin/python3

from markov import rchoose, markov
import sys
from time import sleep

args = sys.argv[1:]

text = ""
size = 5
ov = None
for arg in args:
    if arg.startswith("-size"):
        size = int(arg[5:])
        continue
    if arg.startswith("-ov"):
        ov = int(arg[3:])
        continue
    print("loading {}...".format(arg))
    try:
        with open(arg, "r") as cf:
            text += cf.read()+"\n\n"
        print("loading successful")
    except FileNotFoundError:
        print("loading unsuccessful")

if len(text)==0:
    print("Nothing loaded. Terminating.")
else:
    if ov is None: ov = size-1
    
    chain = markov(text, size)
    print("\nStarting chain:")
    while 1:
        out = rchoose(chain.pats)
        print(out, end='')
        while 1:
            try: out += chain.complete(out, size-ov, ov)
            except TypeError:
                print("\nChain interrupted")
                break
            out = out[-size:]
            print(out[ov-size:],end='')
            sys.stdout.flush()
            sleep(.0001)
        print("\nStarting new chain:")

import itertools
import argparse
from argparse import RawTextHelpFormatter
import re

import argparse
from argparse import RawTextHelpFormatter

#Header on the help page
parser = argparse.ArgumentParser(description="----------Program-Help-Page----------", formatter_class=RawTextHelpFormatter)

#Inline Arguments
parser.add_argument("-i", help="Input file \n")
parser.add_argument("-n", help="Append number range \n")

#Allocates the method to call the arguments to 'args'
args = parser.parse_args()

#Checks value in i argument
if args.i == None:
  print("You forgot to supply an input file.")

#Splits range argument into seperate components
if args.n:
    if len(args.n)>1:
        Splitter = re.split("-|:", args.n)
        LowerRange = Splitter[0]
        UpperRange = Splitter[1]
    else:
        Splitter = args.n
        LowerRange = Splitter
        UpperRange = Splitter

#Generates upper/lower interations of the strings in input file
with open(args.i, "r") as Input:
    for x in Input.read().splitlines():
        Iterations = map(''.join, itertools.product(*((c.upper(), c.lower()) for c in x)))

#Outputs to file
with open("{}Iterated".format(args.i), "a") as Output:
    for x in list(Iterations):
        #Appends a number in the range provided
        if args.n:
            for r in range(int(LowerRange), int(UpperRange)+1):
                Output.write("{}{}\n".format(x, str(r)))
        else:
            Output.write("{}\n".format(x))

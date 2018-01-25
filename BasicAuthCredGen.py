import argparse
from argparse import RawTextHelpFormatter
import os
import base64

#Header on the help page
parser = argparse.ArgumentParser(description="----------Program-Help-Page----------", formatter_class=RawTextHelpFormatter)

#Inline Arguments
parser.add_argument("-u", help="Specify a single username for generation. \n")
parser.add_argument("-uf", help="Specify a file containing a list of usernames for generation.  \n")
parser.add_argument("-p", help="Specify a single password for generation. \n")
parser.add_argument("-pf", help="Specify a file containing a list of usernames for generation.  \n")
parser.add_argument("-o", help="Specify an output file. \n")
parser.add_argument("-s", help="Suppress Terminal Output. \n", action="store_true")
#Allocates the method to call the arguments to 'args'
args = parser.parse_args()

Output = True
Suppress = False

if args.o == None:
    Output = False
    print("No Output File Has Been Provided.  Output Will Only Display Within Terminal.")
if args.s == True:
    Suppress = True
    print("Terminal Output Has Been Suppressed.")

def ArgumentCheck():
    #Checks validity of arguments
    if args.u  == None and args.uf == None:
        print("Please Provide Valid Username(s).")
        exit()
    if args.p  == None and args.pf == None:
        print("Please Provide Valid Password(s).")
        exit()

#Obtains the usernames for processing
def ObtainUsername():
    Username = []
    if args.u:
        Username.append(str(args.u))
    if args.uf:
        if os.path.isfile(str(args.uf))==False:
            print("Invalid User File Specified.")
            exit()
        with open(str(args.uf), "r") as Userfile:
            for line in Userfile:
                Username.append(line.strip("\n"))
    return Username

#Obtains the passwords for processing
def ObtainPasswords():
    Password = []
    if args.p:
        Password.append(str(args.p))
    if args.pf:
        if os.path.isfile(str(args.pf))==False:
            print("Invalid Password File Specified.")
            exit()
        with open(str(args.pf), "r") as Userfile:
            for line in Userfile:
                Password.append(line.strip("\n"))
    return Password

#Generates the BasicAuth format
def B64CredGenerator(Username, Password, Output, Suppress):
    Counter = 0
    if Output == True:
        WriteFile = open(args.o, "a")
    for x in Username:
        for y in Password:
            ComboString = str(x+":"+y)
            Encoded = str((base64.b64encode(bytes(ComboString, "utf-8"))))[2:-1]
            if Output == True:
                WriteFile.write(Encoded+"\n")
            if Suppress == False:
                print(Encoded)
            Counter+=1
    print(str(Counter)+" Credential(s) Generated.")

ArgumentCheck()
print("---------Initialising.---------")
B64CredGenerator(ObtainUsername(), ObtainPasswords(), Output, Suppress)
print("-----Generation-Completed.-----")

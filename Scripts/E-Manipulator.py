#!/usr/bin/python

import os
import argparse
from argparse import RawTextHelpFormatter

parser = argparse.ArgumentParser(description="----------EmailManipulator-Help-Page----------", formatter_class=RawTextHelpFormatter)

#Inline argument handling
parser.add_argument("-i", help="Specify the input file name. \n", type=str)
parser.add_argument("-o", help="Specify the output file name.  If empty, a default file is generated. \n", type=str)
parser.add_argument("-Generate", help="Generates email addresses based-off a list of names and given format. \n", action="store_true")
parser.add_argument("-Filter", help="Filters email addresses within a pre-existing list. \n", action="store_true")
parser.add_argument("-s", help="Suppress Terminal Output. \n", action="store_true")
args = parser.parse_args()

FileInput = args.i
FileOutput = args.o
SuppressOutput = args.s

def FileInputChecks(FileInput):
    #Checking for valid input file arguments
    if FileInput == None:
        print("No input found.  Please specify valid file.\n")
        exit()
    #Checks whether the input file exists
    if os.path.isfile(FileInput)==False:
        print("Invalid input file specified.  Please specify valid file.\n")
        exit()
    #Reads the input file and validity checking
    with open (FileInput) as r:
        FunctionInput = r.read().splitlines()
    if FunctionInput == None:
        print("Specified file is empty.  Please provide a valid file.\n")
        exit()
    return FunctionInput

def FileOutputChecks(FileOutput):
    #Checking for valid output file arguments
    if FileOutput == None:
        FileOutput = False
        print("No output specified.  Output will be printed to console only.")
    #Checks whether the output file can be opened/created.
    if FileOutput:
        open(FileOutput,"w").close()
        if os.path.isfile(FileOutput)==False:
            print("Invalid output file specified.  Please specify valid file.\n")
            exit()

#Generator function for creating email addresses from a list of names
def Generator(FunctionInput, FileOutput, SuppressOutput):
    Output = []
    print("Email Generator Initialised.\n<FN> - Firstname\n<FI> - First Initial\n<LN> - Last Name\n<LI> - Last Initial\n\nEnter Email Format, For Example:\n<FN><LI>@domain.com\n<FI>.<LN>@google.co.uk\n")
    EmailStandard = input("Email: ")
    FormatSpecification = ["<FN>", "<FI>", "<LN>", "<LI>"]
    for I in FunctionInput:
        EmailConvert = EmailStandard
        I = I.lower().split(" ")
        EmailConvert = EmailConvert.replace(str(FormatSpecification[0]), I[0])
        EmailConvert = EmailConvert.replace(str(FormatSpecification[1]), I[0][0])
        EmailConvert = EmailConvert.replace(str(FormatSpecification[2]), I[-1])
        EmailConvert = EmailConvert.replace(str(FormatSpecification[3]), I[-1][0])
        if SuppressOutput == False: print(EmailConvert)
        Output.append(EmailConvert)
    if FileOutput:
        with open (str(FileOutput), "a") as FileOpen:
            for I in Output:
                FileOpen.write(I+"\n")
        print("Emails Written To File: \'"+str(FileOutput)+"\'.")

#Filter function for removing undesirable email addresses from a list
def Filter(FunctionInput, FileOutput, SuppressOutput):
    Output = []
    while True:
        EmailDomain = str(input("Enter An Email Domain (If Multiple, Separate With A Comma): ").lower()).split(",")
        if EmailDomain == None: print("Invalid Email Domain Entered. Try Again.")
        with open (str(FileOutput), "a") as FileOpen:
            for Email in FunctionInput:
                for Domains in EmailDomain:
                    Domains = Domains.strip(" ")
                    if Domains in Email:
                        Output.append(Email)
                        if SuppressOutput == False: print(Email)
            if FileOutput:
                with open (str(FileOutput), "a") as FileOpen:
                    for o in Output:
                        FileOpen.write(o+"\n")
                print("Emails Written To File: \'"+str(FileOutput)+"\'.")
        break

if args.Generate and args.Filter:
    print("Cannot run -Generate and -Filter in parallel.  Please choose one.\n")
    exit()

FunctionInput = FileInputChecks(FileInput)
FileOutputChecks(FileOutput)

if args.Generate:
    print("---------Initialising.---------")
    Generator(FunctionInput, FileOutput, SuppressOutput)
    print("-----Generation-Completed.-----")
if args.Filter:
    print("-----------Filtering.----------")
    Filter(FunctionInput, FileOutput, SuppressOutput)
    print("------Filtering-Completed.-----")

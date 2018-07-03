import requests
import argparse
from argparse import RawTextHelpFormatter
import json
import time
#Header on the help page
parser = argparse.ArgumentParser(description="----------PwnedCheck-Help-Page----------", formatter_class=RawTextHelpFormatter)

#Inline Arguments
parser.add_argument("-email", help="Specify a single email to check. \n")
parser.add_argument("-file", help="Specify a file containing a list of emails to check. \n")
parser.add_argument("-output", help="Output content to file. \n")
parser.add_argument("-delay", help="Sets the time delay - by default it is 2 seconds between requests. \n", type=int)

args = parser.parse_args()
class ArgumentValues():
    Email = args.email
    File = args.file
    Output = args.output
    Delay = 2

#Grabs data on previous credential dumps using the haveibeenpwned API
def BreachedAccount(Email):
    Results = []
    time.sleep(ArgumentValues.Delay)
    APICall = requests.get("https://haveibeenpwned.com/api/v2/breachedaccount/{}".format(Email), "User-Agent: PwnedCheck.py - Cmdline Checker")
    if str(APICall) == "<Response [503]>":
        print("ERROR: Site is currently under load.  Please try again at a later time.")
        return False
    if str(APICall) != "<Response [200]>":
        return False
    APICall = json.loads(APICall.text)
    for x in APICall:
        Results.append("{}:{}".format([x["Name"]], str(x["BreachDate"])))
    SheetCreation(Results)

#Grabs data on previous pastebin dumps using the haveibeenpwned API
def PasteAccount(Email):
    Results = []
    time.sleep(ArgumentValues.Delay)
    APICall = requests.get("https://haveibeenpwned.com/api/v2/pasteaccount/{}".format(Email), "User-Agent: PwnedCheck.py - Cmdline Checker")
    if str(APICall) == "<Response [503]>":
        print("ERROR: Site is currently under load.  Please try again at a later time.")
        Exit()
    if str(APICall) != "<Response [200]>":
        return False
    APICall = json.loads(APICall.text)
    for x in APICall:
        Results.append("{}:{}".format([x["Source"]], str(x["Date"])))
    SheetCreation(Results)

#Creates the csv file if specified
def SheetCreation(Results):
    Columns = ["Email"]
    Data = [ArgumentValues.Email]
    for x in range(0, len(Results)):
        Columns.append("Breach")
        Columns.append("Date")
        Data.append(str(Results[x].split(":")[0].strip("/'[]")))
        Data.append(str(Results[x].split(":")[1]))
    Columns.append("Total Breaches")
    Data.append(str(len(Results)))

    if ArgumentValues.Output != None:
        print("Writing to file.")
        print("\n{}\n{}".format(str(",".join(Columns)), str(",".join(Data))))
        FileWrite("\n{}\n{}".format(str(",".join(Columns)), str(",".join(Data))))
    else:
        print("\n{}\n{}".format(str(",".join(Columns)), str(",".join(Data))))

#Module to append data to a file
def FileWrite(Data):
    with open("{}.csv".format(ArgumentValues.Output), "a") as Outfile:
        Outfile.write(Data)

if args.email == False and args.file == False:
    print("No Email Arguments Provided.")
    exit()

#To prevent stress on the site, a minimum of 5 seconds delay is enforced.
if args.delay:
    if args.delay > 2:
        ArgumentValues.Delay = args.delay

#Runs the email against both of the API calls
if ArgumentValues.Email:
    BreachedAccount(ArgumentValues.Email)
    PasteAccount(ArgumentValues.Email)

#Reads the file and in turn checks them using the API
if ArgumentValues.File:
    BreachedAccountCounter = 0
    PastebinAccountCounter = 0
    try:
        with open(ArgumentValues.File, "r") as ReadFile:
            Lines = list(filter(None, ReadFile.read().splitlines()))
    except IOError:
        print("ERROR: Issues reading file.  Please ensure that the file locations and permissions are valid.")
        exit()
    for Email in Lines:
        ArgumentValues.Email = Email
        Breached = BreachedAccount(Email)
        if Breached != False:
            BreachedAccountCounter +=1
        PasteAccount(Email)
        if PasteAccount != False:
            PastebinAccountCounter+=1
    FileWrite("\nNumber of accounts featured in breaches: {}\nNumber of accounts featured in Pastebin posts:{}".format(BreachedAccountCounter, PastebinAccountCounter))
    print("\nNumber of accounts featured in breaches: {}\nNumber of accounts featured in Pastebin posts:{}".format(BreachedAccountCounter, PastebinAccountCounter))

import requests
import argparse
from argparse import RawTextHelpFormatter
import json
import re
import csv
import os
from termcolor import colored

#Header on the help page
parser = argparse.ArgumentParser(description="----------Program-Help-Page----------", formatter_class=RawTextHelpFormatter)

#Inline Arguments
parser.add_argument("-t", help="Provide an individual or list-file of domains to check. \n")
#Allocates the method to call the arguments to 'args'
args = parser.parse_args()

if not args.t or args.t == "":
    print("\nNo file provided.\n")
    exit()

class Main():
    BasicInformation = {"Config File": os.path.join(os.path.dirname(__file__), "./HeaderConfig.json"), "Target":str(args.t), "OutputFile": "{}/{}Output.csv".format(os.path.dirname(__file__), str(args.t).replace("/",""))}
    #Codes returned in the event of page redirect
    RedirectCodes = [301, 302, 303, 307, 308]
    ResultCharacters= {True:"✔", False:"X"}
    Domains = []
    #Reads the security header config from the json file
    SecurityHeaders = {}
    SecurityHeadersOrder = []
    BooleanHeaders = {}

    def ReadConfig():
        Main.SecurityHeaders = json.loads(open(Main.BasicInformation["Config File"], "r").read())
        Main.SecurityHeadersOrder = list(Main.SecurityHeaders)

    def SiteRequest(Site):
        return requests.get(Site)

    def SiteMatch(Site):
        if re.match("^((http:\/\/)|(https:\/\/))(www\.)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$", Site):
            return True
        return False

    def ReadDomains():
        #Checks whether the target is a URL else assumes it's a file provided
        if Main.SiteMatch(Main.BasicInformation["Target"]):
            Main.Domains = [Main.BasicInformation["Target"]]
        else:
            Main.Domains = open(Main.BasicInformation["Target"], "r").read().splitlines()

    def SiteConnect(Site):
            #Makes sure that the URL in the file matches the regex
            CheckTheSite = Main.SiteMatch(Site)
            if CheckTheSite == False:
                print("{} - Site does not match regex.  Please ensure either \'http://\' or \'https://\' is provided.".format(Site))
                return "False"
            else:
                print("Checking \'{}\' headers.".format(Site))
            #Checks for the sites status code
            try:
                for Counter in range(10):
                    SiteReq = Main.SiteRequest(Site)
                    StatusCode = SiteReq.status_code
                    if StatusCode != 200:
                        if StatusCode not in Main.RedirectCodes:
                            print("Site: '{}' returns a HTTP status code of '{}'.  Should probably be something to double check.".format(Site, str(StatusCode)))
                            break
                        else:
                            print("Redirected to {}".format(SiteReq.url))
                            Site = SiteReq.url
            except Exception as e:
                print(e)
                print("Issue connecting to '{}'.  Make sure that you included the correct URL and that access is available.".format(Site))
                return "False"
            return Main.SiteRequest(Site).headers

    def CheckHeaders():
        for Site in Main.Domains:
            WebRequest = (Main.SiteConnect(Site))
            if WebRequest == "False":
                pass
            else:
                #Iterates through the different header titles
                for HeaderTitle in Main.SecurityHeaders:
                    if Site not in Main.BooleanHeaders:
                        Main.BooleanHeaders[Site] = {}
                    Main.BooleanHeaders[Site][HeaderTitle] = Main.ResultCharacters[False]
                    for Header in Main.SecurityHeaders[HeaderTitle]:
                        if Header in WebRequest:
                            #Checks the header values against approved ones
                            if re.search(Main.SecurityHeaders[HeaderTitle][Header], WebRequest[Header]):
                                Main.BooleanHeaders[Site][HeaderTitle] = Main.ResultCharacters[True]

    def PrintOutput():
        print("")
        for Site in Main.BooleanHeaders:
            print(Site)
            for Header in Main.BooleanHeaders[Site].keys():
                if Main.BooleanHeaders[Site][Header] == Main.ResultCharacters[True]:
                    print("     {} - {}".format(Header, colored(Main.BooleanHeaders[Site][Header], "green")))
                else:
                    print("     {} - {}".format(Header, colored(Main.BooleanHeaders[Site][Header], "red")))
            print("")


    def WriteOutput():
        with open(Main.BasicInformation["OutputFile"], "a") as CSVOutput:
            Writer = csv.writer(CSVOutput, delimiter=",")
            FormatSecHeader = [""]
            Key = ""
            #Creates index for the CSV columns
            for Num in range(0, len(Main.SecurityHeadersOrder)):
                #Writes table headers
                FormatSecHeader.append("{}".format(int(Num)))

            #Creates key for the index
            for Value in FormatSecHeader[1:]:
                Key = Key + "[{}] - {}\n".format(Value, Main.SecurityHeadersOrder[int(Value)])
            CSVOutput.write(Key)
            Writer.writerow(FormatSecHeader)

            #Outputs the site results
            for Sites in Main.BooleanHeaders:
                SpreadsheetLines = [Sites]
                for Order in Main.SecurityHeadersOrder:
                    for Header in Main.BooleanHeaders[Sites][Order]:
                        SpreadsheetLines.append(Header)
                #Writes site values
                Writer.writerow(SpreadsheetLines)
        print("\nOutput written to: \'{}\'.\n".format(Main.BasicInformation["OutputFile"]))

    def Run():
        Main.ReadConfig()
        Main.ReadDomains()
        Main.CheckHeaders()
        Main.PrintOutput()
        Main.WriteOutput()

Main.Run()

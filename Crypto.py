from lxml import html
import sys
import requests
from colorama import init, Fore, Back, Style
init(convert=True)

#Control Variables
Lines = 4           #Controls how many lines the program shows (5 is generally the max)
SpaceFix = 8        #The higher this is, the smaller the spaces are unless it surpasses the max length of the scraped date
Colour = 0          #If 0, the percents will be in colour, if anything else, they'll be without colour
StartVar = 0        #Adds spaces to the start of the data so that it isn't right beside the edge of the screen. If its 1 it'll calculate the space based off Lines and SpaceFix. If not 1, it wont add the space 

pageStr = 'https://coinmarketcap.com/'
#If a number is passed when calling the program, have it set as the line variable
if len(sys.argv) != 1:
    try:
        Lines = int(sys.argv[1])
    except:
        Lines = 4
    if (sys.argv[1] == "all"):
        pageStr = 'https://coinmarketcap.com/all/views/all/'

StartSpace = ""
if StartVar == 1:
    for x in range(0, (SpaceFix - Lines)):
        StartSpace += " "

page = requests.get(pageStr)
tree = html.fromstring(page.content)

Name = tree.xpath('//a[@class="currency-name-container link-secondary"]/text()')
Name.insert(0,"Boopleboop")
Price = tree.xpath('//a[@class="price"]/text()')
Welp = tree.xpath('//td[@class="no-wrap percent-24h  negative_change text-right" or "no-wrap percent-24h  positive_change  text-right"]/text()')
Percent = []
Meh = []
MaxLen = 0
MaxLenPercent = 0
for z in range(0, len(Welp)):
    if "%" in Welp[z]: 
        Percent.append(Welp[z])
        if len(Welp[z]) >= MaxLenPercent:
            MaxLenPercent = len(Welp[z])

for z in range(0, len(Percent)):
    if (MaxLenPercent - len(Percent[z])) == 0:
        Meh.append(0)
    elif (MaxLenPercent - len(Percent[z])) == 1:
        Meh.append(1)
    else:
        Meh.append(2)
        
for z in range(1, len(Name)):
    if len(Name[z] + "  " + Price[z - 1] + "   " + Percent[z - 1]) >= MaxLen:
        MaxLen = len(Name[z] + "  " + Price[z - 1] + "   " + Percent[z - 1])
        
Fix = 5 - Lines
MaxLen += 1
Space = ""
Space2 = ""
print(StartSpace, end="")
for welp in range(0, ((MaxLen * Lines) + (MaxLenPercent * Lines) + (len("  " + " || " + "  ") * Lines)) - (SpaceFix * Lines) - Fix):
    print("_", end = "")
    
print("")
print("")
for x in range(1, len(Name)):
    if x == 1:
        print(StartSpace, end="")
    Space = ""
    Space2 = ""
    if Meh[x - 1] == 0:
        Space2 = ""
    elif Meh[x - 1] == 1:
        Space2 = " "
    else:
        Space2 = "  "
    if MaxLen > len(Name[x] + "  " + Price[x - 1]):
        for y in range(0, (MaxLen - len(Name[x] + "   " + Price[x - 1])) - SpaceFix):
            Space += " "
    if Colour == 0:
        if Percent[x - 1].find("-") == -1:
            Percent[x - 1] = "[92m" + Percent[x - 1] + "[0m"
        else:
            Percent[x - 1] = "[91m" + Percent[x - 1] + "[0m"
    Price[x - 1] += "  " + Space2 + Percent[x - 1]
    if ((x % Lines) == 0) and (x !=0):
        print(Name[x], "  ",  Space, Price[x - 1])
        if x != (len(Name) - 1):
            print(StartSpace, end="")
    else:
        print(Name[x], "  ", Space, Price[x - 1],  " || ", end="")

if Lines == 3 or Lines == 6:
    print("")
print(StartSpace, end="")
for welp in range(0, ((MaxLen * Lines) + (MaxLenPercent * Lines) + (len("  " + " || " + "  ") * Lines)) - (SpaceFix * Lines) - Fix):
    print("_", end = "")
print("")
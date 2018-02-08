from lxml import html
import requests
from colorama import init, Fore, Back, Style
init(convert=True)

#https://coinmarketcap.com/all/views/all/
page = requests.get('https://coinmarketcap.com/')
tree = html.fromstring(page.content)

Lines = 4
SpaceFix = 8
StartSpace = ""
StartVar = 0
if StartVar == 1:
    for x in range(0, (SpaceFix - Lines)):
        StartSpace += " "
    
Name = tree.xpath('//a[@class="currency-name-container"]/text()')
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
import os
from time import sleep as wait
os.system("color a")
os.system("title YouTube ViewBot")
os.system("cls")
print("This Program Is Only Supported For Windows Operation System.")
print("And Can Only Be Executed If You Have Google Chrome Browser.")
print("This Program Will Round Your Views Input To The Nearest Tenth.")
URL = input("What Is The YouTube Video URL?\n")
DURATION = int(input("How Long Is The YouTube Video Duration? (In Seconds)\n"))
VIEWS = int(input("How Many Views Do You Want?\n"))
def Viewer(VURL, VDURATION):
    for i in range(10):
        os.system("start chrome.exe " + VURL)
        wait(0.5)
    wait(DURATION)
    os.system("taskkill /f /im chrome.exe")
    os.system("cls")
    print("This Program Is Only Supported For Windows OS.")
    print("And Can Only Be Executed If You Have Google Chrome Browser.")
    print("This Program Will Round Your Views Input To The Nearest Tenth.")
rounded = round(VIEWS/10)*10
divided = rounded/10
rounded = divided
for i in range(int(rounded)):
    Viewer(VURL=URL, VDURATION=DURATION)
print(f"Successfully Gave {URL}, {VIEWS} Views.")
print("Press Enter To Exit")
input()
exit()


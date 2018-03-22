from tkinter import *
import requests
import urllib3
import subprocess
from bs4 import BeautifulSoup
import sys
import ctypes

http = urllib3.PoolManager()


# Extracting the URL of OpenVPN client
def geturlopenvpn():
    urlopenvpn = "https://openvpn.net/index.php/open-source/downloads.html"
    con = http.request("Get", urlopenvpn)
    content = con.data
    soup = BeautifulSoup(content, "lxml")
    tb = soup.find("tbody")
    tr=tb.find_all("tr")
    for i in tr:
        td=i.find_all("td")
        if "exe" in td[1].text:
            furlopenvpn=td[1].find("a").get('href')
    return furlopenvpn

#Downloading the OpenVPN client from the URL
def getopenvpn(furlopenvpn):
    r = requests.get(furlopenvpn)
    with open("openvpn.exe", "wb") as code:
        code.write(r.content)


# Downloading vpnbook servers
def getvpnbook():
    r1 = requests.get("https://www.vpnbook.com/free-openvpn-account/VPNBook.com-OpenVPN-Euro1.zip")
    with open("Euro1.zip","wb") as code:
        code.write(r1.content)
    r2 = requests.get("https://www.vpnbook.com/free-openvpn-account/VPNBook.com-OpenVPN-Euro2.zip")
    with open("Euro2.zip","wb") as code:
        code.write(r2.content)


#Extracting vpnbook credentials
def vpncred():
    urlvpnbk="https://www.vpnbook.com/"
    con = http.request("Get", urlvpnbk)
    content = con.data
    soup = BeautifulSoup(content, "lxml")
    li = soup.find("li", {"id": "openvpn"})
    u=li.find_all("li")
    l=len(u)
    vpnbkusr=u[l-2].text.split(": ",1)[1]
    vpnbkpass=u[l-1].text.split(": ",1)[1]


def mai():
    getopenvpn(geturlopenvpn())
    #getvpnbook()
    #vpncred()
    subprocess.Popen("./openvpn.exe /S")
    # os.system("openvpn.exe")

#Main Screen, on clicking next the client will be downloaded.
def f():
    master=Tk()
    def new():
        master.destroy()
        mai()
    logo=PhotoImage(file="SplashScreen.gif")
    w=Label(master,
                compound=BOTTOM,
                padx=10,
                bg="#161515",
                fg="#40244D",
                font="Verdana 10 bold",
                text="Secure Yourself",
                image=logo).pack(side="right")
    button=Button(master,text="Next",command=new)
    button.pack()
    master.mainloop()

# Checking if the script is running with administrative rights.
# If not, the script is elevated with administrative rights and the script is then restarted
if ctypes.windll.shell32.IsUserAnAdmin():
    f()
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)


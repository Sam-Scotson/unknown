#+DarkTrace+
import os, sys, datetime
idToken = 0
date = str(datetime.date)
id = str(idToken + 1)
idNumber = id + ':' + date
#Target
def init()


def manual_ip_input():
    def octletOne():
        global oct1
        oct1 = int(input('vvv.xxx.xxx.xxx'))

    def octletTwo():
        global oct2
        oct2 = int(input('xxx.vvv.xxx.xxx'))

    def octletThree():
        global oct3
        oct3 = int(input('xxx.xxx.vvv.xxx'))

    def octletFour():
        global oct4
        oct4 = int(input('xxx.xxx.xxx.vvv'))
    a = octletOne()
    b = octletTwo()
    c = octletThree()
    d = octletFour()
    ipAd = str(a + '.' + b + '.' + c + '.' + d)
    return(ipAd)

ipAddress = manual_ip_input()
    


def nmapStealth(ipAddress):

    

    def submask():
        
        try:
            oct1 = int(input('submask first octlet'))
        except ValueError as e:
            print('error')
            submask()
        try:
            oct2 = int(input('submask second octlet'))
        except ValueError as e:
            print('error')
            submask()
        try:
            oct3 = int(input('submask third octlet'))
        except ValueError as e:
            print('error')
            submask()
        try:
            oct4 = int(input('submask fourth octlet'))
        except ValueError as e:
            print('error')
            submask()
        
    
    

    oneOct = int(range(192))
    twoOct = int(range(168))
    threeOct = int(range(1))
    fourOct = int(range(20))
    IPTarget = ['192.168.1.' + rng]
    MACTarget = ['3E:12:56:E1:A3']

def target_name():
    targetName = input('TARGET NAME')
    return(targetName)


class Target_Node:

    def __init__(self,
                 idNumber,
                 targetName,
                 targetType,
                 targetOS,
                 ipAddress,
                 macAddress,
                 gatewayAddress
                 ):
        self.id = idNumber
        self.name = targetName
        self.type = targetType
        self.os = targetOS
        self.ip = ipAddress
        self.mac = macAddress
        self.gateway = gatewayAddress

    def export(self):


#aircrack///////////////////////////////////////
#nmap//////////////////////////////////////////////
coveredNMap = os.system('proxychains nmap' + IPTarget + )
#whois////////////////////////////////////////////
#
#facetime py
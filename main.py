import requests
import sys

from ParentalControlMessage import ParentalControlMessage

def main():
    numArgs = len(sys.argv)
    if (numArgs < 3):
        print("Not enough arguments. Pass in router password and 'block' or 'unblock' or 'fortniteblock'")
        return 1
    password = sys.argv[1]
    blockOrUnblock = sys.argv[2]
    blockFortnite = False
    
    #Use testBlockStatus on my devices
    testBlockStatus = '0'
    blockStatus = '0'
    if (blockOrUnblock == "block"):
        #testBlockStatus = '1'
        blockStatus = '1'
    elif (blockOrUnblock == "unblock"):
        #testBlockStatus = '0'
        blockStatus = '0'
    elif (blockOrUnblock == "fortniteblock"):
        #testBlockStatus = '0'
        blockFortnite = True
    else:
        print("Argument failure. Second argument should be 'block' or 'unblock'")
        
    routerUrl = "http://192.168.1.1/"
    response = requests.get(routerUrl, auth=('admin', password))
    print("Response to login: " + str(response.status_code))
    
    message = ParentalControlMessage()
    
    payload = message.getPayload()
    
    message.setNumDevices('5')
    message.setDeviceBlockStatus('0', 'Jeffreys-iPhone', testBlockStatus)
    message.setDeviceBlockStatus('1', 'LyonsDesktopXPS-2', blockStatus)
    message.setDeviceBlockStatus('2', 'Chriss-iPhone', blockStatus)
    message.setDeviceBlockStatus('3', 'ChristosiPhone6', blockStatus)
    message.setDeviceBlockStatus('4', 'Justines-iPhone', 0)
    
    if (blockFortnite):
        message.addBlockedUrl('1', 'ol.epicgames.com')
        message.addBlockedUrl('1', 'epicgames.com')
        message.addBlockedUrl('1', 'tracking.epicgames.com')
        message.addBlockedUrl('2', 'ol.epicgames.com')
        message.addBlockedUrl('2', 'epicgames.com')
        message.addBlockedUrl('2', 'tracking.epicgames.com')
        message.addBlockedUrl('3', 'ol.epicgames.com')
        message.addBlockedUrl('3', 'epicgames.com')
        message.addBlockedUrl('3', 'tracking.epicgames.com')
    
    payload = message.getPayload()
    #message.printPayload()
    
    cgiApplyUrl = routerUrl + "apply.cgi"
    response = requests.post(cgiApplyUrl, auth=('admin', password), data=payload)
    print("Response to settings apply: " + str(response.status_code))
    #print(response.text)
    
if (__name__) == "__main__":
    main()
    
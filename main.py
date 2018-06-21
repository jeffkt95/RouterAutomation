import requests
import sys

from ParentalControlMessage import ParentalControlMessage

def main():
    numArgs = len(sys.argv)
    if (numArgs < 3):
        print("Not enough arguments. Pass in router password and 'block' or 'unblock'")
        return 1
    password = sys.argv[1]
    blockOrUnblock = sys.argv[2]
    
    #Use testBlockStatus on my devices
    testBlockStatus = '0'
    blockStatus = '0'
    if (blockOrUnblock == "block"):
        #testBlockStatus = '1'
        blockStatus = '1'
    elif (blockOrUnblock == "unblock"):
        #testBlockStatus = '0'
        blockStatus = '0'
    else:
        print("Argument failure. Second argument should be 'block' or 'unblock'")
        
    

    print("Hello world.")
    routerUrl = "http://192.168.1.1/"
    response = requests.get(routerUrl, auth=('admin', password))
    print(response.status_code)
    
    message = ParentalControlMessage()
    
    payload = message.getPayload()
    
    message.setNumDevices('5')
    message.setDeviceBlockStatus('0', 'Jeffreys-iPhone', testBlockStatus)
    message.setDeviceBlockStatus('1', 'LyonsDesktopXPS-2', blockStatus)
    message.setDeviceBlockStatus('2', 'Chriss-iPhone', blockStatus)
    message.setDeviceBlockStatus('3', 'ChristosiPhone6', blockStatus)
    message.setDeviceBlockStatus('4', 'Justines-iPhone', blockStatus)
    
    payload = message.getPayload()
    
    cgiApplyUrl = routerUrl + "apply.cgi"
    response = requests.post(cgiApplyUrl, auth=('admin', password), data=payload)
    print(response.status_code)
    #print(response.text)
    
if (__name__) == "__main__":
    main()
    
import requests

from ParentalControlMessage import ParentalControlMessage

def main():
    print("Hello world.")
    routerUrl = "http://192.168.1.1/"
    response = requests.get(routerUrl, auth=('admin', 'FakePassword'))
    print(response.status_code)
    
    message = ParentalControlMessage()
    
    payload = message.getPayload()
    
    message.setNumDevices('5')
    #message.setDevice0BlockStatus('Jeffreys-iPhone', '1')
    #message.setDevice1BlockStatus('Jeffreys-iPad', '1')
    message.setDeviceBlockStatus('0', 'Jeffreys-iPhone', '0')
    message.setDeviceBlockStatus('1', 'Jeffreys-iPad', '0')
    message.setDeviceBlockStatus('2', 'LyonsDesktopXPS-2', '0')
    message.setDeviceBlockStatus('3', 'Chriss-iPhone', '0')
    message.setDeviceBlockStatus('4', 'ChristosiPhone6', '0')
    
    payload = message.getPayload()
    
    cgiApplyUrl = routerUrl + "apply.cgi"
    response = requests.post(cgiApplyUrl, auth=('admin', 'FakePassword'), data=payload)
    print(response.status_code)
    #print(response.text)
    
if (__name__) == "__main__":
    main()
    
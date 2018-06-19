
class ParentalControlMessage:
        
    def __init__(self):
        self.initPayload()
    
    def getPayload(self):
        return self.payload

        
    def setNumDevices(self, numberOfDevices):
        self.payload['pcblockdev'] = numberOfDevices
    
    # blockStatus: '0' is unblocked, '1' is always blocked, '2' is specific times blocked
    def setDeviceBlockStatus(self, deviceNumber, deviceName, blockStatus):
        self.payload['pcblockpolicy' + deviceNumber] = deviceName
        self.payload['hnd_time_status' + deviceNumber] = blockStatus
        self.payload['dev_name_' + deviceNumber] = deviceName
    
    # blockStatus: '0' is unblocked, '1' is always blocked, '2' is specific times blocked
    def setDevice0BlockStatus(self, deviceName, blockStatus):
        self.payload['pcblockpolicy0'] = deviceName
        self.payload['hnd_time_status0'] = blockStatus
        self.payload['dev_name_0'] = deviceName
        self.payload['hnd_time_status'] = blockStatus
        
    # blockStatus: '0' is unblocked, '1' is always blocked, '2' is specific times blocked
    def setDevice1BlockStatus(self, deviceName, blockStatus):
        self.payload['pcblockpolicy1'] = deviceName
        self.payload['hnd_time_status1'] = blockStatus
        self.payload['dev_name_1'] = deviceName
        
    # blockStatus: '0' is unblocked, '1' is always blocked, '2' is specific times blocked
    def setDevice2BlockStatus(self, deviceName, blockStatus):
        self.payload['pcblockpolicy2'] = deviceName
        self.payload['hnd_time_status2'] = blockStatus
        self.payload['dev_name_2'] = deviceName
        
    # blockStatus: '0' is unblocked, '1' is always blocked, '2' is specific times blocked
    def setDevice3BlockStatus(self, deviceName, blockStatus):
        self.payload['pcblockpolicy3'] = deviceName
        self.payload['hnd_time_status3'] = blockStatus
        self.payload['dev_name_3'] = deviceName
        
    def initPayload(self):
        self.payload = { 'submit_button': 'PCAR',
                    'change_action': '',
                    'submit_type': '',
                    'action': 'Apply',
                    'next_page': '',
                    'pcblockdev': '1',
                    'pcblocktime': '', 
                    'pcblockurl': '', 
                    'pcblockurl_policy0': '', 
                    'pcblockurl_policy1': '', 
                    'pcblockurl_policy2': '', 
                    'pcblockurl_policy3': '', 
                    'pcblockurl_policy4': '', 
                    'pcblockurl_policy5': '', 
                    'pcblockurl_policy6': '', 
                    'pcblockurl_policy7': '', 
                    'pcblockurl_policy8': '', 
                    'pcblockurl_policy9': '', 
                    'pcblockurl_policy10': '', 
                    'pcblockurl_policy11': '', 
                    'pcblockurl_policy12': '', 
                    'pcblockurl_policy13': '', 
                    'pcblockpolicy': '', 
                    'pcblockpolicy0': '',
                    'pcblockpolicy1': '', 
                    'pcblockpolicy2': '', 
                    'pcblockpolicy3': '', 
                    'pcblockpolicy4': '', 
                    'pcblockpolicy5': '', 
                    'pcblockpolicy6': '', 
                    'pcblockpolicy7': '', 
                    'pcblockpolicy8': '', 
                    'pcblockpolicy9': '', 
                    'pcblockpolicy10': '', 
                    'pcblockpolicy11': '', 
                    'pcblockpolicy12': '', 
                    'pcblockpolicy13': '', 
                    'hnd_time_status0': '',
                    'hnd_sc_start_time0': '',
                    'hnd_sc_end_time0': '',
                    'hnd_wd_start_time0': '',
                    'hnd_wd_end_time0': '',          
                    'hnd_time_status1': '', 
                    'hnd_sc_start_time1': '', 
                    'hnd_sc_end_time1': '', 
                    'hnd_wd_start_time1': '', 
                    'hnd_wd_end_time1': '', 
                    'hnd_time_status2': '', 
                    'hnd_sc_start_time2': '', 
                    'hnd_sc_end_time2': '', 
                    'hnd_wd_start_time2': '', 
                    'hnd_wd_end_time2': '', 
                    'hnd_time_status3': '', 
                    'hnd_sc_start_time3': '', 
                    'hnd_sc_end_time3': '', 
                    'hnd_wd_start_time3': '', 
                    'hnd_wd_end_time3': '', 
                    'hnd_time_status4': '', 
                    'hnd_sc_start_time4': '', 
                    'hnd_sc_end_time4': '', 
                    'hnd_wd_start_time4': '', 
                    'hnd_wd_end_time4': '', 
                    'hnd_time_status5': '', 
                    'hnd_sc_start_time5': '', 
                    'hnd_sc_end_time5': '', 
                    'hnd_wd_start_time5': '', 
                    'hnd_wd_end_time5': '', 
                    'hnd_time_status6': '', 
                    'hnd_sc_start_time6': '', 
                    'hnd_sc_end_time6': '', 
                    'hnd_wd_start_time6': '', 
                    'hnd_wd_end_time6': '', 
                    'hnd_time_status7': '', 
                    'hnd_sc_start_time7': '', 
                    'hnd_sc_end_time7': '', 
                    'hnd_wd_start_time7': '', 
                    'hnd_wd_end_time7': '', 
                    'hnd_time_status8': '', 
                    'hnd_sc_start_time8': '', 
                    'hnd_sc_end_time8': '', 
                    'hnd_wd_start_time8': '', 
                    'hnd_wd_end_time8': '', 
                    'hnd_time_status9': '', 
                    'hnd_sc_start_time9': '', 
                    'hnd_sc_end_time9': '', 
                    'hnd_wd_start_time9': '', 
                    'hnd_wd_end_time9': '', 
                    'hnd_time_status10': '', 
                    'hnd_sc_start_time10': '', 
                    'hnd_sc_end_time10': '', 
                    'hnd_wd_start_time10': '', 
                    'hnd_wd_end_time10': '', 
                    'hnd_time_status11': '', 
                    'hnd_sc_start_time11': '', 
                    'hnd_sc_end_time11': '', 
                    'hnd_wd_start_time11': '', 
                    'hnd_wd_end_time11': '', 
                    'hnd_time_status12': '', 
                    'hnd_sc_start_time12': '', 
                    'hnd_sc_end_time12': '', 
                    'hnd_wd_start_time12': '', 
                    'hnd_wd_end_time12': '', 
                    'hnd_time_status13': '', 
                    'hnd_sc_start_time13': '', 
                    'hnd_sc_end_time13': '', 
                    'hnd_wd_start_time13': '', 
                    'hnd_wd_end_time13': '', 
                    'setdevnameflag': '0',
                    #'dev_mac_0': '64:b0:a6:9f:6b:c4',        
                    'dev_mac_0': '',        
                    'dev_mac_1': '', 
                    'dev_mac_2': '', 
                    'dev_mac_3': '', 
                    'dev_mac_4': '', 
                    'dev_mac_5': '', 
                    'dev_mac_6': '', 
                    'dev_mac_7': '', 
                    'dev_mac_8': '', 
                    'dev_mac_9': '', 
                    'dev_mac_10': '', 
                    'dev_mac_11': '', 
                    'dev_mac_12': '', 
                    'dev_mac_13': '', 
                    'dev_mac_14': '', 
                    'dev_mac_15': '', 
                    'dev_mac_16': '', 
                    'dev_mac_17': '', 
                    'dev_mac_18': '', 
                    'dev_mac_19': '', 
                    'dev_mac_20': '', 
                    'dev_mac_21': '', 
                    'dev_mac_22': '', 
                    'dev_mac_23': '', 
                    'dev_mac_24': '', 
                    'dev_mac_25': '', 
                    'dev_mac_26': '', 
                    'dev_mac_27': '', 
                    'dev_mac_28': '', 
                    'dev_mac_29': '', 
                    'dev_mac_30': '', 
                    'dev_mac_31': '', 
                    'dev_name_0': '',                
                    'dev_name_1': '', 
                    'dev_name_2': '', 
                    'dev_name_3': '', 
                    'dev_name_4': '', 
                    'dev_name_5': '', 
                    'dev_name_6': '', 
                    'dev_name_7': '', 
                    'dev_name_8': '', 
                    'dev_name_9': '', 
                    'dev_name_10': '', 
                    'dev_name_11': '', 
                    'dev_name_12': '', 
                    'dev_name_13': '', 
                    'dev_name_14': '', 
                    'dev_name_15': '', 
                    'dev_name_16': '', 
                    'dev_name_17': '', 
                    'dev_name_18': '', 
                    'dev_name_19': '', 
                    'dev_name_20': '', 
                    'dev_name_21': '', 
                    'dev_name_22': '', 
                    'dev_name_23': '', 
                    'dev_name_24': '', 
                    'dev_name_25': '', 
                    'dev_name_26': '', 
                    'dev_name_27': '', 
                    'dev_name_28': '', 
                    'dev_name_29': '', 
                    'dev_name_30': '', 
                    'dev_name_31': '',                 
                    'start': '',                 
                    'tmsss_enabled': '1',
                    #'dev_list': '64:b0:a6:9f:6b:c4',
                    'dev_list': '',
                    'hnd_time_status': '',
                    'url0': 'yourbutt.com',             
                    'url1': '', 
                    'url2': '', 
                    'url3': '', 
                    'url4': '', 
                    'url5': '', 
                    'url6': '', 
                    'url7': ''}

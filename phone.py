class Phone:
    ''' This class will represent each phone object individually.  As to track phone status, name, phone number, ect... '''
    def __init__ (self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
        self.status = 'onhook'
        self.call = None
        self.conference = None
        
    def offhook(self):
        ''' Sets the status of the phone to offhook '''
        if self.status is 'offhook':
            print(f"{self.name} - {self.phone_number} is already offhook.")
        else:
            self.status = 'offhook'
            print(f"{self.name} - {self.phone_number} hears dialtone.")
            
    def onhook(self):
        ''' Set phone status to onhook '''
        if self.status is 'onhook':
            print(f"{self.name} - {self.phone_number} is already onhook.")
        else:
            self.status = 'onhook'
            self.call = None # Phone onhook, so no call is active
            print(f"{self.name} - {self.phone_number} is onhook.")
            


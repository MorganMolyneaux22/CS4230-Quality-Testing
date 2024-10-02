# List of class respnsibilities:
# - Handle  call operations (
    # dial, 
    # offhook, 
    # onhook, 
    # transfer,
    # conference
# - List status of phone (
    # onhook, 
    # offhook, 
    # dialing, 
    # ringing)
# - 
class PhoneCallManager:
    def __init__(self, phone_book):
        self.phone_book = phone_book
        self.calls = {}  # Store active calls with phone numbers as keys
        self.statuses = {}  # Store phone statuses (onhook, offhook, dialing, ringing)

    def offhook(self, phone):
        if self.statuses.get(phone) == 'offhook':
            print(f"{phone} is already offhook.")
        else:
            self.statuses[phone] = 'offhook'
            print(f"{phone} hears dialtone.")

    def onhook(self, phone):
        if self.statuses.get(phone) == 'onhook':
            print(f"{phone} is already onhook.")
        else:
            self.statuses[phone] = 'onhook'
            self.end_call(phone)
            print(f"{phone} is now onhook.")

    def call(self, phone1, phone2):
        if self.statuses.get(phone1) != 'offhook':
            print(f"{phone1} hears silence (it must be offhook first).")
            return

        if not self.phone_book.validate_phone(phone2) and not self.phone_book.validate_name(phone2):
            print(f"{phone1} hears denial (invalid phone number or name).")
            return

        # Get phone number if name was entered
        phone2_number = self.phone_book.get_phone_by_name(phone2) or phone2

        # Handle busy phone
        if self.statuses.get(phone2_number) == 'offhook':
            print(f"{phone1} hears busy.")
        else:
            self.statuses[phone1] = 'dialing'
            self.statuses[phone2_number] = 'ringing'
            print(f"{phone1} hears ringback. {phone2_number} hears ringing.")

            # Simulate the second phone picking up
            self.offhook(phone2_number)
            print(f"{phone1} and {phone2_number} are talking.")
            self.calls[phone1] = phone2_number
            self.calls[phone2_number] = phone1

    def conference(self, phone1, phone3):
        if phone1 not in self.calls:
            print(f"{phone1} hears silence (not in a call).")
            return
        
        phone2 = self.calls[phone1]  # Get the existing call partner
        if self.statuses.get(phone3) == 'offhook':
            print(f"{phone1} hears busy (phone3 is already offhook).")
            return
        
        self.statuses[phone3] = 'ringing'
        print(f"{phone1} hears ringback. {phone3} hears ringing.")
        
        # Simulate phone3 picking up
        self.offhook(phone3)
        print(f"{phone1}, {phone2}, and {phone3} are talking.")
        self.calls[phone1] = (phone2, phone3)
        self.calls[phone2] = (phone1, phone3)
        self.calls[phone3] = (phone1, phone2)

    def transfer(self, phone1, phone3):
        if phone1 not in self.calls:
            print(f"{phone1} hears silence (not in a call).")
            return
        
        phone2 = self.calls[phone1]  # Get the existing call partner
        if self.statuses.get(phone3) == 'offhook':
            print(f"{phone1} hears busy (phone3 is already offhook).")
            return
        
        self.statuses[phone3] = 'ringing'
        print(f"{phone1} hears ringback. {phone3} hears ringing.")
        
        # Simulate phone3 picking up
        self.offhook(phone3)
        print(f"{phone2} and {phone3} are talking.")
        self.calls[phone2] = phone3
        self.calls[phone3] = phone2
        self.statuses[phone1] = 'onhook'
        print(f"{phone1} hears silence (transferred the call).")

    def end_call(self, phone):
        if phone in self.calls:
            other_party = self.calls.pop(phone)
            if isinstance(other_party, tuple):  # Conference call
                for party in other_party:
                    self.calls.pop(party, None)
                    self.statuses[party] = 'onhook'
            else:  # Regular two-party call
                self.calls.pop(other_party, None)
                self.statuses[other_party] = 'onhook'
            self.statuses[phone] = 'onhook'
            print(f"{phone}'s call has ended.")
        else:
            print(f"{phone} is not in a call.")

    def handle_illegal_operations(self, phone):
        if self.statuses.get(phone) != 'offhook':
            print(f"{phone} hears silence (must go offhook first).")
        else:
            print(f"{phone} hears denial (illegal operation).")

    def status(self):
        # Print the status of each phone
        for phone, status in self.statuses.items():
            call_info = f" and is in a call with {self.calls.get(phone)}" if phone in self.calls else ""
            print(f"{phone} is {status}{call_info}.")
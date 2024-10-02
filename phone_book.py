# List of class responsibilities:
# - load phonebook from file
# - get phone number by last name
# - get last name by phone number
# - get all phone numbers
# - get all last names
# - validate phone number typed into console is valid
# - validate last name typed into console is valid

class PhoneBook:
    def __init__(self, phone_book_file):
        self.phone_book = {}
        self.load_phone_book(phone_book_file)

    def load_phone_book(self, phone_book_file):
        # Simulate loading a phone book from a CSV file
        # For simplicity, it's simulated it with hardcoded entries
        self.phone_book = {
            'John': '12345',
            'Jane': '54321',
            'Doe': '67890',
            'Alice': '11111',
            'Bob': '22222'
        }

    def validate_phone(self, phone):
        # Check if a phone number is valid (exists in phone book or is 5 digits)
        return phone.isdigit() and len(phone) == 5

    def validate_name(self, name):
        # Check if a name is valid (exists in the phone book)
        return name in self.phone_book

    def get_phone_by_name(self, name):
        # Get phone number by name
        return self.phone_book.get(name)
import csv

class PhoneBook:
    def __init__(self, file_path):
        """
        Initializes the PhoneBook by loading phone numbers and names from a CSV file.
        The CSV should have two fields: name and phone number.
        """
        self.phone_book = {}  # Dictionary to store name -> phone number mapping
        self.load_phone_book(file_path)

    def load_phone_book(self, file_path):
        """Loads phone numbers and names from a CSV file."""
        try:
            with open(file_path, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    name, phone = row
                    self.phone_book[name] = phone
            print("Phone book loaded successfully.")
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except Exception as e:
            print(f"Error loading phone book: {e}")

    def validate_phone(self, phone):
        """Validates if the phone number exists in the phone book."""
        return phone in self.phone_book.values()

    def validate_name(self, name):
        """Validates if the name exists in the phone book."""
        return name in self.phone_book

    def get_phone_by_name(self, name):
        """Returns the phone number corresponding to a given name."""
        return self.phone_book.get(name)

    def get_name_by_phone(self, phone):
        """Returns the name corresponding to a given phone number."""
        for name, number in self.phone_book.items():
            if number == phone:
                return name
        return None

    def display_phone_book(self):
        """Displays the phone book."""
        for name, phone in self.phone_book.items():
            print(f"{name}: {phone}")

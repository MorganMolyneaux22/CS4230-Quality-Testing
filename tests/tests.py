# We will want about 9-49 test cases for this?
# Need to to find if it for each class, or overall. 



# Boundary Testing 
# Create a boundary test to find what the boundary might be 
    # - example, if the phone number is 10 digits, what happens if it is 9 digits?
    # - example, if the phone number is 10 digits, what happens if it is 11 digits?
    # - example, if the phone is on hook, what happens if it is off hook?
    # - example, if the phone is off hook, what happens if it is on hook?
    # - example, if the phone is dialing, what happens if it is ringing?
    # - example, if the phone is ringing, what happens if it is dialing?
    
# These are all hypotheticals, but I'm just writing them down while they're fresh on my head.  
# Also to give an idea of what it's asking, so we can think of better ones later. 

import pytest
from src.phone import Phone
from src.phone_book import PhoneBook

@pytest.fixture
def phone():
    return Phone("Test User", "24721")  # Create a phone object with a valid name and phone number

@pytest.fixture
def phone_book():
    return PhoneBook('phonebook.csv')


def test_phone_offhook_already_offhook(phone):  
    phone.offhook() 
    previous_status = phone.status 
    phone.offhook()
    assert phone.status == previous_status

def test_phone_number_invalid_length():
    with pytest.raises(ValueError, match="Invalid phone number. Ensure the phone number is 5 digits long."):
        Phone("Test User", "123")

def test_phone_number_invalid_characters():
    with pytest.raises(ValueError, match="Invalid phone number. Ensure the phone number contains only numbers."):
        Phone("Test User", "abcd2") 

def test_phone_offhook_valid():
    phone = Phone("Test User", "24721")
    phone.offhook()
    assert phone.status == "offhook"

def test_phone_onhook_status():
    phone = Phone("Test User", "24721")
    assert phone.status == "onhook"

def test_phone_call_valid():
    phone = Phone("Test User", "24721")
    phone.offhook()  # Ensure the phone is offhook
    phone.call = "Calling John"
    assert phone.call == "Calling John"








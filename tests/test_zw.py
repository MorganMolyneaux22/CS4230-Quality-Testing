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
from src.phone_call_manager import PhoneCallManager
from unittest.mock import patch, mock_open

@pytest.fixture
def phone():
    return Phone("Test User", "24721") 

@pytest.fixture
def phone_book():
    mock_phone_book = PhoneBook("mock_phonebook.csv")
    mock_phone_book.phone_book = {
        "John Doe": "12345",
        "Jane Smith": "67890"
    }
    return mock_phone_book

@pytest.fixture
def phone_call_manager(phone_book):
    return PhoneCallManager(phone_book)

def test_phonebook_validate_existing_phone(phone_book):
    assert phone_book.validate_phone("12345") is True


def test_phonebook_validate_nonexistent_phone(phone_book):
    assert phone_book.validate_phone("99999") is False

def test_phonebook_validate_existing_name(phone_book):
    assert phone_book.validate_name("John Doe") is True

def test_phonebook_validate_nonexistent_name(phone_book):
    assert phone_book.validate_name("Jane Doe") is False

@patch("builtins.open", new_callable=mock_open, read_data="John Doe,12345\nJane Smith,67890")
def test_phonebook_load_phone_book(mock_open_file):
    phone_book = PhoneBook("mock_phonebook.csv")
    assert phone_book.phone_book == {"John Doe": "12345", "Jane Smith": "67890"}

# Phone Boundary Tests
def test_phone_offhook_already_offhook(phone):  
    phone.offhook()
    previous_status = phone.status
    phone.offhook()
    assert phone.status == previous_status

def test_phone_onhook_status(phone):
    assert phone.status == "onhook"

def test_phone_offhook_status_change(phone):
    phone.offhook()
    assert phone.status == "offhook"

def test_phone_onhook_after_offhook(phone):
    phone.offhook()
    phone.onhook()
    assert phone.status == "onhook"

def test_phone_call_set(phone):
    phone.offhook()
    phone.call = "Calling John"
    assert phone.call == "Calling John"

def test_phone_number_invalid_length():
    with pytest.raises(ValueError, match="Invalid phone number. Ensure the phone number is 5 digits long."):
        Phone("Test User", "123")

def test_phone_number_invalid_characters():
    with pytest.raises(ValueError, match="Invalid phone number. Ensure the phone number contains only numbers."):
        Phone("Test User", "abcd2")

def test_offhook_onhook_transition(phone_call_manager):
    phone_call_manager.offhook("12345")
    assert phone_call_manager.statuses["12345"] == "offhook"

    phone_call_manager.onhook("12345")
    assert phone_call_manager.statuses["12345"] == "onhook"

def test_offhook_redundant(phone_call_manager):
    phone_call_manager.offhook("12345")
    previous_status = phone_call_manager.statuses["12345"]
    phone_call_manager.offhook("12345")
    assert phone_call_manager.statuses["12345"] == previous_status

def test_onhook_redundant(phone_call_manager):
    phone_call_manager.onhook("12345")
    previous_status = phone_call_manager.statuses["12345"]
    phone_call_manager.onhook("12345")
    assert phone_call_manager.statuses["12345"] == previous_status

def test_valid_call(phone_call_manager):
    phone_call_manager.offhook("12345")

    phone_call_manager.call("12345", "67890")

    assert phone_call_manager.calls["12345"] == "67890" 
    assert phone_call_manager.calls["67890"] == "12345" 

def test_call_busy_status(phone_call_manager):
    phone_call_manager.offhook("12345")
    phone_call_manager.offhook("67890")
    phone_call_manager.call("12345", "67890")

    assert phone_call_manager.statuses["12345"] == "offhook"
    assert "67890" not in phone_call_manager.calls

def test_call_onhook_error(phone_call_manager):
    with pytest.raises(ValueError, match="hears silence"):
        phone_call_manager.call("12345", "67890")

def test_end_call(phone_call_manager):
    phone_call_manager.offhook("12345")
    phone_call_manager.call("12345", "67890")
    phone_call_manager.onhook("12345")

    assert phone_call_manager.statuses["12345"] == "onhook"
    assert phone_call_manager.statuses["67890"] == "onhook"
    assert "12345" not in phone_call_manager.calls
    assert "67890" not in phone_call_manager.calls

def test_call_busy_phone(phone_call_manager):
    phone_call_manager.offhook("12345")
    phone_call_manager.offhook("67890")

    phone_call_manager.call("12345", "67890")

    assert "12345" not in phone_call_manager.calls
    assert "67890" not in phone_call_manager.calls

def test_end_call_resets_status(phone_call_manager):
    phone_call_manager.offhook("12345")
    phone_call_manager.call("12345", "67890")

    phone_call_manager.onhook("12345")

    assert phone_call_manager.statuses["12345"] == "onhook"
    assert phone_call_manager.statuses["67890"] == "onhook"
    assert "12345" not in phone_call_manager.calls
    assert "67890" not in phone_call_manager.calls

def test_redundant_offhook(phone_call_manager):
    phone_call_manager.offhook("12345")
    previous_status = phone_call_manager.statuses["12345"]

    phone_call_manager.offhook("12345")

    assert phone_call_manager.statuses["12345"] == previous_status

def test_redundant_onhook(phone_call_manager):
    phone_call_manager.onhook("12345")
    previous_status = phone_call_manager.statuses["12345"]

    phone_call_manager.onhook("12345")

    assert phone_call_manager.statuses["12345"] == previous_status

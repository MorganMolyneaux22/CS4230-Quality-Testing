# ################################################################################
#
#
#  ██████ ███████     ██   ██ ██████  ██████   ██████  
# ██      ██          ██   ██      ██      ██ ██  ████ 
# ██      ███████     ███████  █████   █████  ██ ██ ██ 
# ██           ██          ██ ██           ██ ████  ██ 
#  ██████ ███████          ██ ███████ ██████   ██████ 
# 
# Project Created by: Morgan Molyneaux, Zachary Webb, Caden Black, James West
# 
# Purpose:
# - 
# -
#
# Features:
# - 
# - 
# - 
#
################################################################################


import random
import string
import csv

# List of BASE phone commands (the foundation of this project)
# ------ At any instance, the phone might be referenced as the phone number or last name ------
# - phone dials another phone
# - phone goes offhook
# - phone goes onhook
# - phone is transfered to another phone
# - phone is put into a conference call
# - list status of phone (onhook, offhook, dialing, ringing))

from phone_book import PhoneBook
from phone_call_manager import PhoneCallManager

def main():
    phone_book_file = "phonebook.csv"  # Placeholder, as we simulate the phone book
    phone_book = PhoneBook(phone_book_file)
    phone_call_manager = PhoneCallManager(phone_book)

    # Simulate phone operations:
    phone_call_manager.offhook("12345")
    phone_call_manager.call("12345", "54321")
    phone_call_manager.conference("12345", "67890")  # Adding a third phone for conference
    phone_call_manager.transfer("12345", "67890")  # Transferring the call to another phone
    phone_call_manager.handle_illegal_operations("12345")  # Trying an illegal operation
    phone_call_manager.onhook("12345")
    phone_call_manager.status()

if __name__ == "__main__":
    main()
   

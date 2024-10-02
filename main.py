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
    phone_book_file = "phonebook.csv"  # Load the phone book from a CSV file
    phone_book = PhoneBook(phone_book_file)
    phone_call_manager = PhoneCallManager(phone_book)

    print("Welcome to the Phone Call Simulator!")
    print("Available commands:")
    print(" - 'p': Print the phone book")
    print(" - 'call <phone1> <phone2>': Call from one phone to another")
    print(" - 'offhook <phone>': Take the phone offhook")
    print(" - 'onhook <phone>': Put the phone onhook")
    print(" - 'transfer <phone1> <phone2>': Transfer call from phone1 to phone2")
    print(" - 'conference <phone1> <phone3>': Add phone3 to the call between phone1 and phone2")
    print(" - 'end_call <phone>': End the current call for the specified phone")
    print(" - 'status': Display the status of all phones")
    print(" - 'quit': Exit the simulator")
    
    # TODO: Add object reference to each individual phone object as to track the status of each phone, name for testing purposes 
    # TODO: Hunt for logic error, bugs, anything that could be improved upon
    # TODO: Testing, testing, testing
    # TODO: Update the README.md file with the project's purpose, features, and instructions on how to run the program
    # TODO: Update the header of each file with the project name, purpose, features, and the names of the authors (COPIED FROM MAIN)
    
    # Notes while running: The phone that is set to ring will be the one that is called.
    # As a result it must be on hook, and the dialing phone must be offhook.
    # Example: 
    # Enter a command: call 43727 23072, 
    # 43727 hears silence (it must be offhook first).
    # Enter a command: offhook 43727
    # 43727 hears dialtone.
    # Enter a command: call 43727 23072
    # 43727 hears ringback. 23072 hears ringing.
    # 23072 hears dialtone.
    # 43727 and 23072 are talking.

    while True:
        command = input("\nEnter a command: ").strip().lower()
        
        if command == 'p':
            phone_book.display_phone_book()  
        
        elif command.startswith('call'):
            try:
                _, phone1, phone2 = command.split()  
                phone_call_manager.call(phone1, phone2)  
            except ValueError:
                print("Invalid command format. Use: call <phone1> <phone2>")
        
        elif command.startswith('offhook'):
            try:
                _, phone = command.split()  
                phone_call_manager.offhook(phone)  
            except ValueError:
                print("Invalid command format. Use: offhook <phone>")
        
        elif command.startswith('onhook'):
            try:
                _, phone = command.split()  
                phone_call_manager.onhook(phone)  
            except ValueError:
                print("Invalid command format. Use: onhook <phone>")
        
        elif command.startswith('transfer'):
            try:
                _, phone1, phone2 = command.split()  
                phone_call_manager.transfer(phone1, phone2) 
            except ValueError:
                print("Invalid command format. Use: transfer <phone1> <phone2>")
        
        elif command.startswith('conference'):
            try:
                _, phone1, phone3 = command.split() 
                phone_call_manager.conference(phone1, phone3) 
            except ValueError:
                print("Invalid command format. Use: conference <phone1> <phone3>")
        
        elif command.startswith('end_call'):
            try:
                _, phone = command.split()  
                phone_call_manager.end_call(phone)  
            except ValueError:
                print("Invalid command format. Use: end_call <phone>")
        
        elif command == 'status':
            phone_call_manager.status()  
        
        elif command == 'quit':
            print("Exiting the simulator.")
            break
        
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()
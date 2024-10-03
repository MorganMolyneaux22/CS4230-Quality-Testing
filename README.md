# CS4230-Quality-Testing

## Description

This repository contains the project code for **Project 1 - Telephone Switching Simulation** in the CS 4230 Quality Testing course. The project simulates a telephone switching system, demonstrating concepts related to call routing, resource management, and error handling.

## Code Design

The code is structured using an object-oriented approach with the following key classes:

- **`PhoneBook`:** Manages a collection of `Phone` objects constructed from the file "phonebook.csv". Allows searching for phone numbers by name or vice versa, and can print its entire contents.
- **`PhoneCallManager`:** Handles the logic for initiating, managing, and terminating calls between `Phone` objects. This includes tasks like finding available lines, routing calls, and updating phone statuses.
- **`Phone`:** Represents an individual telephone with properties like its phone number, active calls, and current status (e.g., available, ringing, in use).

The design emphasizes modularity and testability, with clear separation of concerns between classes and comprehensive tests using PyTest.

## Usage

**Please note that "phone" may be used to reference the phone number or the last name associated with it.**

### BASE phone commands (the foundation of this project)

- A phone dials another phone.
- A phone goes offhook.
- A phone goes onhook.
- A phone is transferred to another phone.
- A phone is put into a conference call.
- List status of phone (onhook, offhook, dialing, ringing).

### How to run the simulation

1. **Clone the repository:** `git clone https://github.com/your-username/CS4230-Quality-Testing.git`.
2. **Navigate to the project directory:** `cd CS4230-Quality-Testing`.
3. **Run the main script:** `python main.py` or `python3 main.py`.

### Optional arguments

- `-n <number_of_phones>`: Specifies the number of phones to simulate (default: 10).
- `-c <number_of_calls>`: Specifies the number of calls to simulate (default: 20).  
  **Example:** `python main.py -n 20 -c 50`

## Contributors

- **Morgan Molyneaux**
- **Zachary Webb**
- **Caden Black**
- **James West**

## License

This program is licensed under the `MIT License`. For more information, please see the [LICENSE](LICENSE.txt) file.

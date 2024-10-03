from src import strings


class Phone:
    """This class will represent each phone object individually.  As to track phone status, name, phone number, ect..."""

    def __init__(self, name, phone_number):
        self._name = ""
        self._phone_number = ""

        self.name = name
        self.phone_number = phone_number
        self.status = "onhook"
        self.call = None
        self.conference = None

    @property
    def phone_number(self) -> str:
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value: str):
        if len(value) != 5:
            raise ValueError(strings.INVALID_PHONE_LENGTH)
        if not value.isnumeric():
            raise ValueError(strings.INVALID_PHONE_CHARS)

        self._phone_number = value

    def offhook(self):
        """Sets the status of the phone to offhook."""
        if self.status == "offhook":
            print(f"{self.name} - {self._phone_number} is already offhook.")
        else:
            self.status = "offhook"
            print(f"{self.name} - {self._phone_number} hears dialtone.")

    def onhook(self):
        """Set phone status to onhook."""
        if self.status == "onhook":
            print(f"{self.name} - {self._phone_number} is already onhook.")
        else:
            self.status = "onhook"
            self.call = None  # Phone onhook, so no call is active
            print(f"{self.name} - {self._phone_number} is onhook.")

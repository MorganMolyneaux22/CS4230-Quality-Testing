import pytest

import src.strings as strings
from src import Phone


def test_0_digit_phone_number():
    with pytest.raises(ValueError) as e_info:
        Phone("Gonzalez", "")
    assert str(e_info.value) == strings.INVALID_PHONE_LENGTH


def test_4_digit_phone_number():
    with pytest.raises(ValueError) as e_info:
        Phone("Sakura", "0280")
    assert str(e_info.value) == strings.INVALID_PHONE_LENGTH


def test_6_digit_phone_number():
    with pytest.raises(ValueError) as e_info:
        Phone("Johansen", "028190")
    assert str(e_info.value) == strings.INVALID_PHONE_LENGTH

    # - example, if the phone is on hook, what happens if it is off hook?
    # - example, if the phone is off hook, what happens if it is on hook?
    # - example, if the phone is dialing, what happens if it is ringing?
    # - example, if the phone is ringing, what happens if it is dialing?


def test_phone_on_hook():
    pass

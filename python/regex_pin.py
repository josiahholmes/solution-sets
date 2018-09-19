#!/usr/bin/env python3
import re


def validate_pin(pin: str) -> bool:
    pattern = re.compile(r"^\d{4}|\d{6}$")
    if pattern.fullmatch(pin):
        return True
    return False
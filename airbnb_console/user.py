#!/usr/bin/python3
"""Creates User class that inherits from BaseModel."""
from models.base_model import BaseModel


class User(BaseModel):
    """User Class Implementation."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""


#!/usr/bin/python3
"""Creates City class that inherits from BaseModel."""
from models.base_model import BaseModel


class City(BaseModel):
    """City Class Implementation."""

    state_id = ""
    name = ""

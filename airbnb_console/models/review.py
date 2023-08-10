#!/usr/bin/python3
"""Creates Review class that inherits from BaseModel."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review Class Implementation."""

    place_id = ""
    user_id = ""
    text = ""

#!/usr/bin/python3
"""Implementation of the Review Module"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Creates all Reviews"""

    place_id: str = ''
    user_id: str = ''
    text: str = ''

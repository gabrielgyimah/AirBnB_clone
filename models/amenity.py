#!/usr/bin/python3
"""Implementation of the Amenity Module"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Creates all Amenity"""

    name: str

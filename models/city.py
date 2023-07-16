#!/usr/bin/python3
"""Implementation of the City Module."""

from models.base_model import BaseModel


class City(BaseModel):
    """Creates all cities."""

    state_id: str
    name: str

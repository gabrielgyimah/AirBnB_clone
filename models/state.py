#!/usr/bin/python3
"""Implementation of the State Module."""

from models.base_model import BaseModel


class State(BaseModel):
    """This class represent all States/counties."""

    name: str = ''

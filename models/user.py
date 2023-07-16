#!/usr/bin/python3
# Implementation of the User Model


from models.base_model import BaseModel


class User(BaseModel):
    # User Model

    email: set
    password: str
    first_name: str
    last_name: str

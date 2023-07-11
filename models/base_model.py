#!/usr/bin/python3
#  The BaseModel

from datetime import datetime
import uuid


class BaseModel:
    # Defines all common attributes/methods for it child classes

    def __init__(self, **kwargs):
        # Initializes the BaseModel instances

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        
        if kwargs:
            for key, value in kwargs.items():
                self.key = value

    def save(self):
        # updates the public instance attribute updated_at

        self.updated_at = datetime.now()

    def to_dict(self):
        # Returns a dictionary represnetation of the instance

        # converting created_at and updated_at to ISO formats string representation
        self.created_at = str(self.created_at.isoformat())
        self.updated_at = str(self.updated_at.isoformat())

        obj_dict = self.__dict__
        obj_dict["__class__"] = self.__class__.__name__

        return obj_dict


    def __str__(self):
        # Returns the official string representation of an instance

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

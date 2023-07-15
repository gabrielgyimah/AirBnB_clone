#!/usr/bin/python3
# BaseModel - Defines and initilizes
# all the common attributes and methods


from datetime import datetime
import uuid


class BaseModel:

    def __init__(self, *arg, **kwargs) -> None:
        """Initializes instances of the BaseModel"""

        if kwargs:
            attr = kwargs.copy()
            if '__class__' in attr:
                del attr['__class__']
            if 'created_at' in attr:
                attr['created_at'] = datetime.strptime(
                    attr['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
            if 'updated_at' in attr:
                attr['updated_at'] = datetime.strptime(
                    attr['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")

            for key in attr:
                setattr(self, key, attr[key])
        else:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self) -> str:
        # Returns the official string
        # representation of the instance

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        # Updates the public instance
        # attribute updated_at with the current
        # datetime
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        # Returns a dictionary containing
        # all keys/values of __dict__ of the
        # instance

        self.created_at = str(self.created_at.isoformat())
        self.updated_at = str(self.updated_at.isoformat())
        obj = self.__dict__
        obj['__class__'] = self.__class__.__name__

        return obj

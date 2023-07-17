#!/usr/bin/python3
# Implementation of the FileStorage Model

import json


class FileStorage:
    # Serializes instances to a JSON file and deserializes JSON file to
    # instances

    __file_path = 'file.json'
    __objects: dict = {}

    def all(self):
        # Returns the dictionary __objects
        return self.__objects

    def new(self, obj):
        # Sets in __objects the obj with key <obj class name>.id
        if not obj:
            return
        attr = obj.to_dict()
        key = attr['__class__'] + '.' + attr['id']
        self.__objects[key] = obj

    def save(self):
        # serializes __objects to the JSON file (path: __file_path)
        objs = {}
        existing_data = {}
        for key in self.__objects:
            objs[key] = self.__objects[key].to_dict()
        try:
            with open(self.__file_path, 'r', encoding='UTF-8') as file:
                existing_data = json.load(file)
        except Exception:
            pass

        existing_data.update(objs)

        try:
            with open(self.__file_path, 'w', encoding='utf-8') as f:
                json.dump(existing_data, f, indent=8)
        except Exception:
            pass

    def reload(self):
        # Deserializes the JSON file to __objects
        # (only if the JSON file (__file_path)
        # exists ; otherwise, do nothing.
        # If the file doesn’t exist, no
        # exception should be raised)
        try:
            with open(self.__file_path, "r", encoding="UTF-8") as file:
                seriralized_obj = json.loads(file.read())

                for key, obj_dict in seriralized_obj.items():
                    if key not in self.__objects:
                        name = obj_dict['__class__']
                        base = eval(f"{name}(**obj_dict)")
                        self.new(base)

        except Exception:
            pass

    @property
    def get_file(self):
        # Getter method for the __filepath attribute
        return self.__file_path

#!/usr/bin/python3
# Implementation of the FileStorage Model

import json
import os


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

        for key in self.__objects:
            objs[key] = self.__objects[key].to_dict()
        try:
            with open(self.__file_path, 'w', encoding='utf-8') as f:
                json.dump(objs, f, indent=4)
        except Exception as e:
            pass

    def reload(self):
        # Deserializes the JSON file to __objects
        # (only if the JSON file (__file_path)
        # exists ; otherwise, do nothing.
        # If the file doesn’t exist, no
        # exception should be raised)
        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    for key, obj_data in data.items():
                        self.__objects[key] = obj_data
            except Exception:
                pass
        else:
            return

    @property
    def get_file(self):
        # Getter method for the __filepath attribute
        return self.__file_path

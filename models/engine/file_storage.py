#!/usr/bin/python3
"""
Module for FileStorage class
"""

import json
from models.base_model import BaseModel
from datetime import datetime


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(new_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                loaded_dict = json.load(f)
                for key, value in loaded_dict.items():
                    cls_name, obj_id = key.split('.')
                    obj_dict = value
                    for k, v in obj_dict.items():
                        if k in ['created_at', 'updated_at']:
                            obj_dict[k] = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f')
                    new_obj = eval(cls_name)(**obj_dict)
                    self.__objects[key] = new_obj
        except FileNotFoundError:
            pass


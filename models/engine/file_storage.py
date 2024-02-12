#!/usr/bin/python3
""" Module for FileStorage class """

import json
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    """ Class for serializing and deserializing instances to JSON file """

    __file_path = "file.json"
    __objects = {}
    classes = {"BaseModel": BaseModel, "User": User}

    def all(self):
        """ Returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file """
        obj_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """ Deserializes the JSON file to __objects """
        try:
            with open(FileStorage.__file_path, mode="r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    cls_name = value["__class__"]
                    if cls_name in FileStorage.classes:
                        FileStorage.__objects[key] = FileStorage.classes[cls_name](**value)
        except FileNotFoundError:
            pass


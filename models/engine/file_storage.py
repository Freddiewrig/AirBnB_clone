#!/usr/bin/python3
import json
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    __file_path = "file.json"
    __objects = {}
    classes = {
            'BaseModel': BaseModel,
            'User': User,
            'City': City,
            'State': State,
            'Place': Place,
            'Amenity': Amenity,
            'Review': Review,
            }

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        with open(self.__file_path, "w") as f:
            data = {key: obj.to_dict() for key, obj in self.__objects.items()}
            json.dump(data, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as f:
                data = json.load(f)
            for key, obj_dict in data.items():
                obj_class = globals()[obj_dict["__class__"]]
                self.__objects[key] = obj_class(**obj_dict)
        except FileNotFoundError:
            pass

#!/usr/bin/python3
import json
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

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects
    
    def new(self, obj):
        """sets in __objects the obj with key """
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        serial_obj = {}
        for key, obj in FileStorage.__objects.items():
            serial_obj[key] = obj.to_dict()

        """serializes __objects to the JSON file"""
        with open(FileStorage.__file_path, "w") as f:
            json.dump(serial_obj, f)
    
    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            print("file path: ", FileStorage.__file_path)
            with open(FileStorage.__file_path, "r") as f:
                load_obj = json.load(f)

            FileStorage.__objects = {}
            for key, obj_dict in load_obj.items():
                class_name, obj_id = key.split('.', 1)
                obj_class = globals()[class_name]
                obj_instance = obj_class(**obj_dict)
                FileStorage.__objects[key] = obj_instance
        except FileNotFoundError:
            pass

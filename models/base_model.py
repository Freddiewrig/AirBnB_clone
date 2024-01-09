#!usr/bin/python3
from uuid import uuid4
from datetime import datetime
import models
"""Define class BaseModel"""


class BaseModel:
    """Init basemodel"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
            for key, Value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, Value)
            else:
                self.id = str(uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()
                models.storage.new(self)
                
    def save(self):
        """Update the update_at with the curent time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns dict.self"""
        model_dict = self.__dict__.copy()
        model_dict["__class__"] = self.__class__.__name__
        model_dict["created_at"] = self.created_at.isoformat()
        model_dict["updated_at"] = self.updated_at.isoformat()
        return model_dict

    def __str__(self):
        """prints [<class name>] (<self.id>) <self.__dict__>"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)
    
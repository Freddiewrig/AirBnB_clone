#!usr/bin/python3
from uuid import uuid4
from datetime import datetime
"""Define class BaseModel"""

class BaseModel:
    """Init basemodel"""
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def save(self):
        """Update the update_at with the curent time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns dict.self"""
        model_dict = self.__dict__.copy()
        model_dict["__class__"] = self.__class__.__name__
        model_dict["created_at"] = self.created_at.isoformat()
        model_dict["updated_at"] = self.updated_at.isoformat()
        return model_dict
    
    def __str__(self):
        """prints [<class name>] (<self.id>) <self.__dict__>"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
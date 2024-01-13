#!/usr/bin/python3
from models.base_model import BaseModel
"""Write a class User that inherits from BaseModel"""


class User(BaseModel):
    """Public class 
    attributes:
        email: string - empty string
        password: string - empty string
        first_name: string - empty string
        last_name: string - empty string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
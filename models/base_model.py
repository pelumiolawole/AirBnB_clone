#!/usr/bin/python3
""" Base Model Module
"""
from datetime import datetime
import uuid


class BaseModel():
    """ defines all common attributes and methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """ BaseMode constructor

            Args:
                *args: all arguments
                **kwargs: named argumnts
            Return:
        """
        # check if kwargs is empty
        if (len(kwargs) < 0):
            # loop through to get the keys and set the values
            for key, value in kwargs.item():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        value = datetime.fromisoformat(value)
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """ String represention
        """
        return f"[{self.__class__.__name__}]\
             ({self.id}) {self.__dict__}"

    def save(self):
        """ updates the date and time when an instance gets modified
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dict with all keys/values of the instance

            Return: a dict containing all key/values of __dict__
        """
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['id'] = self.id
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict

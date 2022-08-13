#!/usr/bin/python3
""" Base Model Module
"""
from datetime import datetime
import uuid
import models


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
        if (len(kwargs) > 0):
            self.my_number = kwargs['my_number']
            self.name = kwargs['name']
            self.created_at = datetime.strptime(
                kwargs['created_at'],
                '%Y-%m-%dT%H:%M:%S.%f'
            )
            self.id = kwargs['id']
            self.updated_at = datetime.strptime(
                kwargs['updated_at'],
                '%Y-%m-%dT%H:%M:%S.%f'
            )
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ String represention
        """
        return f"[{self.__class__.__name__}]\
             ({self.id}) {self.__dict__}"

    def save(self):
        """ updates the date and time when an instance gets modified
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dict with all keys/values of the instance

            Return: a dict containing all key/values of __dict__
        """
        my_dict = {}
        for key, value in self.__dict__.items():
            if type(value) is datetime:
                my_dict[key] = value.isoformat()
            else:
                my_dict[key] = value
            my_dict['__class__'] = self.__class__.__name__
        return my_dict

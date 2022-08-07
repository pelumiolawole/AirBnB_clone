#!/usr/bin/python3
""" file storage module
"""
import json


class FileStorage():
    """ serializes and deserializes between objects and JSON
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ Returns the dictionary __object
        """
        return FileStorage.__objects

    def new(self, obj):
        """ sets the __objects with obj key
            Args:
                obj: The key
        """
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes object to the JSON file
        """
        new_obj = {}
        temp = FileStorage.__objects
        for key, value in temp.items():
            new_obj[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as my_file:
            string_data = json.dumps(new_obj, indent=2)
            my_file.write(string_data)

    def reload(self):
        """ deserializes JSON file to object
        """
        from models.base_model import BaseModel
        filename = FileStorage.__file_path

        try:
            with open(filename, 'r', encoding='utf-8') as file:
                string_data = file.read()
                dict_data = json.loads(string_data)
            for (key, value) in dict_data.items():
                if key not in FileStorage.__objects.keys():
                    FileStorage.__objects[key] = BaseModel(dict_data)
            
        except IOError:
            pass

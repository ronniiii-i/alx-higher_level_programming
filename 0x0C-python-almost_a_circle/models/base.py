#!/usr/bin/python3
"""Defines a base model class"""

import json


class Base:
    """
    Represent the base model.
    Represents the "base" for all other classes in project 0x0C*.
    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the Base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: The JSON string representation of the list of dictionaries.
        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances inheriting from Base.
        """
        if list_objs is None:
            list_objs = []
        json_list = [obj.to_dictionary() for obj in list_objs]
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            file.write(cls.to_json_string(json_list))

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string representation to a list of dictionaries.

        Args:
            json_string (str): JSON string representing a list of dictionaries.

        Returns:
            list: A list of dictionaries.
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with all attributes already set.

        Args:
            **dictionary: A dictionary of attribute values.

        Returns:
            Base: Instance with attributes set based on the provided dictionary
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            return None

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        '''Loads string from file and unjsonifies.'''
        from os import path
        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf-8") as f:
            return [cls.create(**d) for d in cls.from_json_string(f.read())]

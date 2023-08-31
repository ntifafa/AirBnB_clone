#!/usr/bin/python3
"""FileStorage module"""
import json
from models.base_model import BaseModel


class FileStorage:
    """
        class serializes instances to a JSON
        file and deserializes JSON to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """
            sets in __objects the obj with key <obj class name>.id

            Args:
                obj - an instance object
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to JSON file
        first converts object to dictionary format
        """
        obj_dict = {}
        for key, val in FileStorage.__objects.items():
            # print(f"{type(val)}")
            # print(f"{type(FileStorage.__objects)}")
            # break
            obj_dict[key] = val.to_dict()

        with open(FileStorage.__file_path, mode='w', encoding="UTF8") as fd:
            json.dump(obj_dict, fd)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, mode='r') as fd:
                jstring = fd.read()
                if jstring is None:
                    return
                data = json.loads(jstring)
                for key, obj_dict in data.items():
                    # class_name = obj_dict["__class__"]
                    obj = BaseModel(**obj_dict)
                    FileStorage.__objects[key] = obj

        except FileNotFoundError:
            pass

    def valid_class_names(self):
        """Return a list of valid class names"""
        return ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"] 

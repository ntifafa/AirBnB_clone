#!/usr/bin/python3
"""
This module forms the basis for all other classes
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """defines base class"""

    def __init__(self, *args, **kwargs):
        """initialize instance attributes"""
        if kwargs:
            if "__class__" in kwargs:
                del kwargs["__class__"]
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime
                            (value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """"
            returns string representation of BaseModel class
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """
            updates the updated_at attribute
            with the current datetime
        """
        self.updated_at = datetime.now()
        # storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
            returns a dictionary containing all
            keys/values of __dict__ instance
        """
        my_dict = self.__dict__.copy()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["__class__"] = self.__class__.__name__
        return my_dict

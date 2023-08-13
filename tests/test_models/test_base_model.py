#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
"""
Unittest ests for the BaseModel Class
"""


class TestBaseModel(unittest.TestCase):
    """ TestBaseMode class """

    def test_uuid(self):
        """
        Test cases for uuid
        Two instances are created of the BaseModel class
        to test their uuids
        """
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertIsInstance(bm1, BaseModel)
        self.assertTrue(hasattr(bm1, "id"))
        self.assertNotEqual(bm1.id, bm2.id)
        self.assertIsInstance(bm1.id, str)

# from models.base_model import BaseModel

# my_model = BaseModel()
# my_model.name = "My First Model"
# my_model.my_number = 89
# print(my_model)
# my_model.save()
# print(my_model)
# my_model_json = my_model.to_dict()
# print(my_model_json)
# print("JSON of my_model:")
# for key in my_model_json.keys():
#     print("\t{}: ({}) - {}".format(key,
# type(my_model_json[key]), my_model_json[key]))

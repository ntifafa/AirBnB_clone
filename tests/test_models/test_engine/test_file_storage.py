#!/usr/bin/python3
"""
Unittest tests for the FileStorage Class
"""
import unittest
import json
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage_instant(unittest.TestCase):
    """
    Testing instantiation of the FileStorage class.
    """

    def test_FStorage_instant_with_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FStorage_instant_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializing(self):
        self.assertEqual(type(models.storage), FileStorage)

    def test_initialization(self):
        self.assertIsInstance(self.storage, FileStorage)

    def test_new_and_all_methods(self):
        # Create a dummy object
        dummy_obj = {'__class__': 'BaseModel', 'id': 'test_id'}
        self.storage.new(dummy_obj)

        # Check if the dummy object is in the storage
        objects = self.storage.all()
        self.assertIn('BaseModel.test_id', objects)

    def test_save_and_reload(self):
        # Create a dummy object
        dummy_obj = {'__class__': 'BaseModel', 'id': 'test_id'}
        self.storage.new(dummy_obj)

        # Save and reload the storage
        self.storage.save()
        self.storage.reload()

        # Check if the reloaded storage contains the dummy object
        objects = self.storage.all()
        self.assertIn('BaseModel.test_id', objects)

    def test_save_and_reload_file(self):
        # Create a dummy object
        dummy_obj = {'__class__': 'BaseModel', 'id': 'test_id'}
        self.storage.new(dummy_obj)

        # Save and reload the storage
        self.storage.save()
        self.storage.reload()

        # Check if the content of the reloaded file matches the dummy object
        with open(self.temp_file_path, 'r') as file:
            data = json.load(file)
            self.assertIn('BaseModel.test_id', data)


if __name__ == '__main__':
    unittest.main()

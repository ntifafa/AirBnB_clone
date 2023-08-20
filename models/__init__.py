#!/usr/bin/python3
"""package initializer"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User

storage = FileStorage()
storage.reload()

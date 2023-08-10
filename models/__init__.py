#!/usr/bin/python3
"""package initializer"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

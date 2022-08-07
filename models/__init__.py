#!/usr/bin/python3
""" Creating unique filestorage instance """

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

#!usr/bin/env python
# -*- coding: utf-8 -*-
""" Task 04: Create the PickleCache Class"""

import os
import os.path
import pickle


class PickleCache(object):
    """create pickle cache class"""

    __file_object = None
    __data = {}

    def __init__(self, file_path='datastore.pkl'):
        """constructor"""

        self.__file_path = file_path

    def set(self, key, value):
        """public set method"""

        self.__data[key] = value

    def get(self, key):
        """public get method"""

        if key in self.__data:
            return self.__data[key]
        else:
            print "Error: No value found for key: '{}'".format(key)

    def delete(self, key):
        """public delete method"""

        if key in self.__data:
            del self.__data[key]
        else:
            print "Error: No value found for key: '{}'".format(key)

    def open(self):
        """public open method"""

        if os.path.exists(self.__file_path):
            if os.path.getsize(self.__file_path) > 0:
                self.__file_object = open(self.__file_path, 'rb')
                self.__data = pickle.load(self.__file_object)
                self.__file_object.close()
        self.__file_object = open(self.__file_path, 'wb')

    def flush(self, reopen=True):
        """pickle dump"""

        pickle.dump(self.__data, self.__file_object)
        self.__file_object.close()

        if reopen:
            self.open()

    def close(self):
        """close method"""

        self.flush(reopen=False)
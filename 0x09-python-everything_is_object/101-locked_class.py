#!/usr/bin/python3
"""this module has only one class called LockedClass"""


class LockedClass:
    """defining a method that allow to set attribute first_name automatically"""
    def __setattr__(self, name: str, value):
        if not hasattr(self, "first_name") and name != "first_name":
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")

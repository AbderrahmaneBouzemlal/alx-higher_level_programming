#!/usr/bin/python3
"""this module has only one class called LockedClass"""


class LockedClass:
    """definning a method that allow to set attribute first_name automatically"""
    def __setattr__(self, name: str, value) -> None:
        if not hasattr(self, "first_name") and name != "first_name":
            raise AttributeError("f'{slef.__class__.__name__}' object has no attribute '{name}'")
        super().__setattr__(name, value)

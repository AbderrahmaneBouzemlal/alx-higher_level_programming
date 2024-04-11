#!/usr/bin/python3


class LockedClass:
    def __setattr__(self, name: str, value) -> None:
        if not hasattr(self, "first_name") and name != "first_name":
            raise AttributeError("f'{slef.__class__.__name__}' object has no attribute '{name}'")
        super().__setattr__(name, value)

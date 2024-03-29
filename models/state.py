#!/usr/bin/python3
"""This module contains the State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """State class that inherits from BaseModel."""

    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize State class."""
        super().__init__(*args, **kwargs)


#!/usr/bin/python3
"""Defines MyInt class"""


class MyInt(int):
    """Parent class"""
    def __eq__(self, other):
        """Inverts the behavior of =="""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inverting the behavior of !="""
        return super().__eq__(other)

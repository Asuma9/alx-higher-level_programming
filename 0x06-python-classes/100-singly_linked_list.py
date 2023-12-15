#!/usr/bin/python3
"""Defines a singly linked list class Node"""


class Node:
    """Creates a class Node"""
    def __init__(self, data, next_node=None):
        """Method to initialize a node"""
        self.__data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter to retrieve data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter to manipulate data"""
        self.__data = value
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """Getter to retrieve next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter to manipulate the next node"""
        self.__next_node = value
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """Defines a singly linked list"""
    def __str__(self):
        """Prints string representatioj of a singlyLinkedList."""
        rtn = ""
        ptr = self.__head

        while ptr is not None:
            rtn += str(ptr.data)
            if ptr.next_node is not None:
                rtn += "\n"
            ptr = ptr.next_node

        return rtn

    def __init__(self):
        """Initializes linked list instance"""
        self.__head = None

    def sorted_insert(self, value):
        """Prints a sorted list in increasing order"""
        ptr = self.__head

        while ptr is not None:
            if ptr.data > value:
                break
            ptr_prev = ptr
            ptr = ptr.next_node

        newnode = Node(value, ptr)
        if ptr == self.__head:
            self.__head = newnode
        else:
            ptr_prev.next_node = newnode

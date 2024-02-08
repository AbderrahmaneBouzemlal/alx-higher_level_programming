#!/usr/bin/python3
"""Singly Linked Lists module.

This module contains methods about the creation and hendling of
SinglyLinkedList and Node objects.

"""


class Node:
    """Defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Sets the necessary attributes for the Node object.

        Args:
            data (int): the value of the node
            next_node (Node): the next Node
        """

        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Get or set the data value of a node."""

        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get or set the next node of the current node."""

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    def __init__(self):
        """Initializes an empty singly linked list"""
        self.__head = None

    def __str__(self):
        """Sets the print behavior of the SinglyLinkedList object."""

        result = ""
        ptr = self.__head
        while ptr:
            result += str(ptr.data) + "\n"
            ptr = ptr.next_node
        return result[:-1]

    def sorted_insert(self, value):
        new = Node(value)
        if self.__head is None or self.__head.data >= value:
            new.next_node = self.__head
            self.__head = new
        current_node = self.__head
        while current_node.next_node and current_node.next_node.data < value:
            current_node = current_node.next_node
        new.next_node = current_node.next_node
        current_node.next_node = new

#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node= next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value != None:
            raise TypeError("next_node must be a Node object")
class SinglyLinkedList:
    def __init__(self):
        """Initializes an empty singly linked list"""
        self.__head = None
    def __str__(self):
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

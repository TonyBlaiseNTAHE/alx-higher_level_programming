#!/usr/bin/python3

class Node:
    """
    Represents a Node in a singly linked list.

    Attributes:
    - data (int): The data stored in the Node.
    - next_node (Node): The reference to the next Node in the linked list.
    """
    def __init__(self, data, next_node=None):
        """
        Initializes a Node with the given data and next_node.

        Args:
            data (int): The data to be stored in the Node.
            next_node (Node, optional): Reference to the next
            Node. Defaults to None.
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """int: Returns the data stored in the Node."""
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the data of the Node.

        Args:
            value (int): The new data value for the Node.

        Raises:
            TypeError: If the value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Node: Returns the reference to the next Node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next_node of the Node.

        Args:
            value (Node): The new next_node for the Node.

        Raises:
            TypeError: If the value is not a Node object or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object or None")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """Represent a singly-linked list."""

    def __init__(self):
        """Initalize a new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.
        The node is inserted into the list at the correct
        ordered numerical position.
        Args:
            value (Node): The new Node to insert.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))

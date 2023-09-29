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
    """
    Represents a Singly Linked List.

    Attributes:
    - head (Node): The head of the linked list.
    """
    def __init__(self):
        """Initializes an empty SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the linked list.

        Args:
            value (int): The value to be inserted into the linked list.
        """
        new_node = Node(value)
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and \
                    current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Represents the linked list as a string.

        Returns:
            str: The linked list represented as a string.
        """
        result = ""
        current = self.__head
        while current is not None:
            result += str(current.data) 
            if current.next_node is not None:
                result += "\n"
            current = current.next_node
        return result

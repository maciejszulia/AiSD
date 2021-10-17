from typing import Any


class Node:
    def __init__(self, value: Any):
        self.value = value
        self.next = None  # domyslnie tail


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        output = ""
        this_node = self.head
        while this_node is not None:
            output += str(Node.value)
            if this_node.next is not None:
                output += " -> "
        return output

    def print(self):
        print(str(self.__repr__()))


list_ = LinkedList()
assert list_.head == None
LinkedList.print(self=list_)
from typing import Any


class Node:
    def __init__(self, value: Any):
        self.value = value
        self.next_Node = None  # domyslnie tail?? chyba tak

        """
        klasa Node:
            zkonstruuj obiekt Node:
                wartość = value
                następny_węzeł = None
        """


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

        """
        klasa ListaPołączona:
            zkonstruuj obiekt LinkedList:
                głowa = None
                ogon = None
        """

    def __repr__(self):
        out = ""
        Node = self.head
        while Node is not None:
            out += str(Node.value)
            out += " -> "
        return out

    def __print__(self):
        return self.__repr__()

    def push(self, value: Any) -> None:
        element = Node(value)
        self.head = element
        element.next_Node = element
        if self.tail is None:
            self.tail = element


list_ = LinkedList()
assert list_.head is None  # ok

list_.push(1)
list_.push(0)

assert str(list_) == "0 -> 1"

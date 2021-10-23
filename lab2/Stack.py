from typing import Any
from LinkedList import LinkedList


class Stack:
    _storage: LinkedList

    def __init__(self):
        self._storage = LinkedList()
        self.head = None

    def isempty(self):
        if self.head is None:
            return True
        else:
            return False

    def push(self, element: Any) -> None:
        self.append(element)

Stack.push(1)
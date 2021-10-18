from typing import Any


class Node:
    def __init__(self, value: Any, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def __repr__(self):
        output = ""
        current_node = self.head
        while current_node is not None:
            output += str(current_node.value)
            if current_node.next_node is not None:
                output += " -> "
            current_node = current_node.next_node
        return output

    def print(self):
        print(str(self.__repr__()))

    def append(self, value: Any) -> None:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while True:
            if current_node.next_node is None:
                current_node.next_node = new_node
                break
            current_node = current_node.next_node

    def push(self, value: Any) -> None:
        new_node = Node(value)


list_ = LinkedList()
assert list_.head is None
list_.append(9)
list_.append(10)
assert str(list_) == '9 -> 10'

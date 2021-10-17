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
            output += str(this_node.value)
            if this_node.next is not None:
                output += " -> "
            this_node = this_node.next
        return output

    def push(self, value: Any) -> None:
        this_node = Node(value)
        this_node.next = self.head
        self.head = this_node
        if self.tail is None:
            self.tail = this_node

    def print(self):
        print(str(self.__repr__()))


list_ = LinkedList()
assert list_.head == None

list_.push(1)
list_.push(0)

#assert str(list_) == '0 -> 1'
LinkedList.print(self=list_)

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

    def __str__(self):
        return str(self.__repr__())

    def print(self):
        print(str(self.__repr__()))

    def push(self, value: Any) -> None:
        new_node = Node(value)
        new_node.next_node = self.head
        self.head = new_node

    def append(self, value: Any) -> None:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node is not None:  # while True is now while current_node is not None
            if current_node.next_node is None:
                current_node.next_node = new_node
                break
            current_node = current_node.next_node

    def get_node(self, at: int) -> Node:
        if at == 0:
            return self.head
        counter = 0
        current_node = self.head
        while current_node is not None:
            if counter == at:
                return current_node
            else:
                current_node = current_node.next_node
                counter += 1

    def insert(self, value: Any, after: Node) -> None:
        current_node = self.head
        temp_node = Node
        while current_node is not None:
            if current_node is after:
                if current_node.next_node is None:
                    self.append(value)
                    break
                current_node = current_node.next_node
                temp_node.value = current_node.value
                temp_node.next_node = current_node.next_node
                current_node.value = value
                current_node.next_node = temp_node
            current_node = current_node.next_node

    def remove(self, after: Node) -> Any:
        if after.next_node is None:
            return
        if after.next_node.next_node is not None:
            after.next_node = after.next_node.next_node
        else:
            after.next_node = None
            self.tail = after


list_ = LinkedList()
assert list_.head is None
list_.append(2)
list_.append(3)
list_.push(1)
middle_node = list_.get_node(at=1)
list_.remove(after=middle_node)
# assert str(list_) == '9 -> 10'
list_.print()
print(list_.get_node(1))

from typing import Any


class Node:
    value: Any
    next_node: 'Node'

    def __init__(self, value: Any, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList:
    head: Node
    tail: Node

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def __repr__(self):
        output = []
        node = self.head
        while node is not None:
            output.append(node.value)
            node = node.next_node
        return output

    def __str__(self):
        str_out = map(str, self.__repr__())
        return " -> ".join(str_out)

    def __len__(self):
        length = 0
        current_node = self.head
        while current_node is not None:
            length += 1
            current_node = current_node.next_node
        return length

    def push(self, value: Any) -> None:
        new_node = Node(value)
        new_node.next_node = self.head
        self.head = new_node

    def append(self, value: Any) -> None:  # todo#1: da sie to zrobic ładniej ALE NIE MAM NA TO CZASU!!!!!!!!!
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

    def get_node(self, at: int) -> Node:  # todo#1
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

    def insert(self, value: Any, after: Node) -> None:  # todo#1
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

    def pop(self) -> Any:  # funckja zwraca typ any więc przy returnie jest popped_node.value
        if self.head is None:
            return None
        popped_node = self.head
        self.head = self.head.next_node
        popped_node.next_node = None
        return popped_node.value

    def remove_last(self) -> Any:   # todo#1
        if self.head is None:
            return None
        current_node = self.head
        while current_node is not None:
            if current_node.next_node.next_node is self.tail:
                removed = current_node.next_node.value
                current_node.next_node = self.tail
                return removed
            current_node = current_node.next_node

    def remove(self, after: Node) -> Any:
        if after.next_node is None:
            return
        if after.next_node.next_node is not None:
            after.next_node = after.next_node.next_node
        else:
            after.next_node = None
            self.tail = after


# list_ = LinkedList()
# assert list_.head is None
# print(str(list_))
#
# list_.push(1)
# list_.push(0)
# assert str(list_) == '0 -> 1'
# print(str(list_))
#
# list_.append(9)
# list_.append(10)
# assert str(list_) == '0 -> 1 -> 9 -> 10'
# print(str(list_))
#
# middle_node = list_.get_node(at=1)
# list_.insert(5, after=middle_node)
# assert str(list_) == '0 -> 1 -> 5 -> 9 -> 10'
# print(str(list_))
#
# first_element = list_.get_node(at=0)
# returned_first_element = list_.pop()
# assert first_element.value == returned_first_element
#
# last_element = list_.get_node(at=3)
# returned_last_element = list_.remove_last()
# assert last_element.value == returned_last_element
#
# assert str(list_) == '1 -> 5 -> 9'
# print(str(list_))
#
# second_node = list_.get_node(at=1)
# list_.remove(second_node)
# assert str(list_) == '1 -> 5'
# print(str(list_))

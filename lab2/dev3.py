from typing import Any


class Node:
    def __init__(self, value: Any):
        self.value = value
        self.next = None  # domyslnie tail

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
        output = ""
        this_node = self.head
        while this_node is not None:
            output += str(this_node.value)
            if this_node.next is not None:
                output += " -> "
            this_node = this_node.next
        return output

    """ __reprezentacja__(LinkedList)
        output = ""     "" - string
        glowa listy wskazuje na ten_node
        while this_node nie jest None (pusty):  ten while literuje węzły
            dodaj do output this_node.value
            jeżeli wskaźnik do następnego node nie jest None:
                do output dodaj " -> "
             ten_node to teraz next node
             ((skok do początku while))
        return output
    """

    def print(self):
        print(str(self.__repr__()))

    def push(self, value: Any) -> None:
        this_node = Node(value)
        this_node.next = self.head
        self.head = this_node
        if self.tail is None:
            self.tail = this_node

    """
    def push(LinkedList, value):
        ten_node = Node(value)
        głowa = ten_node.nastepny
    """

    def append(self, value: Any) -> None:
        this_node = Node(value)
        this_node.next = self.tail
        self.tail = this_node
        if self.head is None:
            self.head = this_node




list_ = LinkedList()
assert list_.head is None
print("ok")

list_.push(1)
list_.push(0)
# list_.push(2)
# list_.push(2)
# list_.push(3)

assert str(list_) == '0 -> 1'

list_.append(9)
LinkedList.print(self=list_)

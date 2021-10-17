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

    # def __repr__(self):
    #     return self.value


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

    def __repr__(self):  # jaaaaaaaaaaaaaa pierdoleeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        output = ""
        this_node = self.head  # head to wzkaznik na pierwszy wezel, nie posiada wartosci(value)
        while this_node is not None:
            output += str(this_node.value)
            this_node = this_node.next_Node
            # if this_node is not None: # czemu nie dziala, nie wiem
            output += " -> "
        return output[:-4]

        """ __pokazsie__(LinkedList)
            output = ""     # "" - string
            glowa listy = ten_node (glowa wskazuje na ten_node)
            while this_node nie jest None:
        """

    def print(self):
        return print(self.__repr__())

    def push(self, value: Any) -> None:
        this_node = Node(value)
        this_node.next_Node = self.head
        self.head = this_node
        if self.tail is None:
            self.tail = this_node

        """ push(LinkedList)
            ten_node to Node(value)
            
        """

    def append(self, value: Any) -> None:
        new_node = Node(value)
        current_node = self.head
        while current_node.next_Node is not None:
            current_node = current_node.next_Node
        current_node = new_node

list_ = LinkedList()
assert list_.head is None  # ok

list_.push(1)
list_.push(0)

assert str(list_) == '0 -> 1'
list_.append(9)
list_.append(10)

# assert str(list_) == '0 -> 1 -> 9 -> 10'

LinkedList.print(self=list_)

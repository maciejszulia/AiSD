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

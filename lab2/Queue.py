from typing import Any
from LinkedList import LinkedList


class Queue:
    _storage: LinkedList

    def __init__(self):
        self._storage = LinkedList()

    def __len__(self):
        pass

    def __repr__(self):
        output = []
        node = self._storage.head
        while node is not None:
            output.append(node.value)
            node = node.next_node
        return output

    def __str__(self):
        str_out = map(str, self.__repr__())
        return ", ".join(str_out)

    def peek(self) -> Any:
        return self._storage.get_node(0)

    def enqueue(self, element: Any) -> None:
        self._storage.append(element)

    def dequeue(self) -> Any:  # return Node?
        return self._storage.pop()


queue = Queue()
# assert len(queue) == 0

queue.enqueue('klient1')
queue.enqueue('klient2')
queue.enqueue('klient3')
print(str(queue))
# assert str(queue) == 'klient1, klient2, klient3'

from typing import Any, List, Callable, Union
from lab02.Queue import Queue


class TreeNode:
    value: Any
    children: List['TreeNode']

    def __init__(self, value):
        self.value = value
        self.children = []

    def __str__(self):
        return str(self.value)

    def is_leaf(self) -> bool:
        if len(self.children) == 0:
            return True

        return False

    def add(self, child: 'TreeNode') -> None:
        self.children.append(child)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)

        for child in self.children:
            child.for_each_deep_first(visit)

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)
        _queue = Queue()

        for child in self.children:
            _queue.enqueue(child)

        while len(_queue) != 0:
            top_elem = _queue.dequeue()
            visit(top_elem)

            for i in top_elem.childern:
                _queue.enqueue(i)

    def search(self, value: Any) -> Union['TreeNode', None]:

        def fun():
            output: List['TreeNode'] = [TreeNode.value]
            return output


class Tree:
    root: TreeNode

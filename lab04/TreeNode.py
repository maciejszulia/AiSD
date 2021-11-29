from typing import Any, List, Callable, Union
from lab02.Queue import Queue


class TreeNode:
    value: Any
    children: List['TreeNode']

    def __init__(self, value):
        self.value = value
        self.children = []
        self.parent = None

    def __str__(self):
        return str(self.value)

    def is_leaf(self) -> bool:
        if self.children:
            return True
        else:
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

        while _queue:  # while len(_queue) != 0:
            this_node = _queue.dequeue()
            visit(this_node)
            for i in this_node.childern:
                _queue.enqueue(i)

    #todo da sie to lepiej
    def search(self, value: Any) -> Union['TreeNode', None]:
        output: List[TreeNode] = []

        def fun(node: 'TreeNode'):
            if node.value == value:
                output.append(node)

        self.for_each_level_order(fun)

        if output:
            return output[0]
        else:
            pass


tree: 'TreeNode' = TreeNode(2)
assert tree.value == 2
tree.add(TreeNode(1))
assert tree.children[0].value == 1
tree.add(TreeNode(4))
assert tree.children[1].value == 4
tree.children[0].add(TreeNode(3))
assert tree.children[0].children[0].value == 3
tree.children[1].add(TreeNode(6))
assert tree.children[1].children[0].value == 6

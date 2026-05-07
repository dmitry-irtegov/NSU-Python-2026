from typing import Generic, Optional, TypeVar, runtime_checkable, Protocol, Any, Iterator
from enum import Enum


class Color(Enum):
    RED = 1
    BLACK = 2


@runtime_checkable
class SupportsLessAndEqThan(Protocol):
    def __lt__(self, other: Any) -> bool: ...

    def __eq__(self, other: Any) -> bool: ...

K = TypeVar("K", bound=SupportsLessAndEqThan)
T = TypeVar("T")

class SortedDictNode(Generic[K, T]):
    def __init__(self,
                 key: Optional[K] = None,
                 value: Optional[T] = None):

        self.key : Optional[K] = key
        self.value : Optional[T] = value

        self.color : Color = Color.RED
        self.rightChild : Optional[SortedDictNode[K, T]] = None
        self.leftChild : Optional[SortedDictNode[K, T]] = None
        self.parent : Optional[SortedDictNode[K, T]] = None


class SortedDict(Generic[K, T]):
    def __init__(self) -> None:
        self._noneNode : SortedDictNode[K, T] = SortedDictNode[K, T]()
        self._noneNode.color = Color.BLACK
        self._noneNode.leftChild = self._noneNode
        self._noneNode.rightChild = self._noneNode
        self._noneNode.parent = self._noneNode

        self._root : SortedDictNode[K, T] = self._noneNode


    def __getitem__(self, key: K) -> T:
        node : Optional[SortedDictNode[K, T]] = self._findNode(key)
        if node is None:
            raise KeyError("dict doesn't have key " + str(key))

        assert node.value is not None

        return node.value

    def _findNode(self, key: K) -> Optional[SortedDictNode[K, T]]:
        node: SortedDictNode[K, T] = self._root
        while node != self._noneNode:
            # По построению алгоритма все эти параметры гарантированно не None
            # Только noneNode имеет ключ и значение None
            assert node.key is not None

            if node.key == key:
                return node

            if node.key < key:
                assert node.rightChild is not None
                node = node.rightChild
            else:
                assert node.leftChild is not None
                node = node.leftChild

        return None

    def __setitem__(self, key: K, value: T) -> None:
        existedNode : Optional[SortedDictNode[K, T]] = self._findNode(key)
        if existedNode is not None:
            existedNode.value = value
            return

        newNode : SortedDictNode[K, T] = SortedDictNode[K, T](key, value)
        newNode.leftChild = self._noneNode
        newNode.rightChild = self._noneNode
        newNode.parent = self._noneNode

        assert newNode.key is not None

        parent : SortedDictNode[K, T] = self._noneNode
        node : SortedDictNode[K, T] = self._root
        while node != self._noneNode:
            assert node.key is not None

            parent = node
            if newNode.key < node.key:
                assert node.leftChild is not None
                node = node.leftChild
            else:
                assert node.rightChild is not None
                node = node.rightChild

        newNode.parent = parent
        if parent == self._noneNode:
            self._root = newNode
        elif newNode.key < parent.key:
            parent.leftChild = newNode
        else:
            parent.rightChild = newNode

        self._insertFixup(newNode)


    def _insertFixup(self, newNode: SortedDictNode[K, T]) -> None:
        node : SortedDictNode[K, T] = newNode
        uncle: SortedDictNode[K, T] = node

        assert node.parent is not None
        while node.parent.color == Color.RED:
            assert node.parent is not None
            assert node.parent.parent is not None
            assert node.parent.parent.rightChild is not None
            assert node.parent.parent.leftChild is not None

            if node.parent == node.parent.parent.leftChild:
                uncle = node.parent.parent.rightChild

                if uncle.color == Color.RED:
                    node.parent.color = Color.BLACK
                    uncle.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    node = node.parent.parent
                else:
                    assert node.parent is not None

                    if node == node.parent.rightChild:
                        node = node.parent
                        self._left_rotate(node)

                    assert node.parent is not None
                    assert node.parent.parent is not None

                    node.parent.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    self._right_rotate(node.parent.parent)
            else:
                assert node.parent is not None
                assert node.parent.parent is not None
                assert node.parent.parent.leftChild is not None

                uncle = node.parent.parent.leftChild

                if uncle.color == Color.RED:
                    node.parent.color = Color.BLACK
                    uncle.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    node = node.parent.parent
                else:
                    assert node.parent is not None

                    if node == node.parent.leftChild:
                        node = node.parent
                        self._right_rotate(node)

                    assert node.parent is not None
                    assert node.parent.parent is not None

                    node.parent.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    self._left_rotate(node.parent.parent)
        self._root.color = Color.BLACK


    def _left_rotate(self, node: SortedDictNode[K, T]) -> None:
        assert node is not None
        assert node.parent is not None
        assert node.rightChild is not None

        rightChild : SortedDictNode[K, T] = node.rightChild

        assert rightChild.leftChild is not None

        node.rightChild = rightChild.leftChild
        if rightChild.leftChild != self._noneNode:
            rightChild.leftChild.parent = node

        rightChild.parent = node.parent
        if node.parent == self._noneNode:
            self._root = rightChild
        elif node == node.parent.leftChild:
            node.parent.leftChild = rightChild
        else:
            node.parent.rightChild = rightChild

        rightChild.leftChild = node
        node.parent = rightChild


    def _right_rotate(self, node: SortedDictNode[K, T]) -> None:
        assert node is not None
        assert node.parent is not None
        assert node.leftChild is not None

        leftChild : SortedDictNode[K, T] = node.leftChild

        assert leftChild.rightChild is not None

        node.leftChild = leftChild.rightChild
        if leftChild.rightChild != self._noneNode:
            leftChild.rightChild.parent = node

        leftChild.parent = node.parent
        if node.parent == self._noneNode:
            self._root = leftChild
        elif node == node.parent.rightChild:
            node.parent.rightChild = leftChild
        else:
            node.parent.leftChild = leftChild

        leftChild.rightChild = node
        node.parent = leftChild

    def __delitem__(self, key: K) -> None:
        node : Optional[SortedDictNode[K, T]] = self._findNode(key)
        if node is None:
            raise KeyError("dict doesn't have key " + str(key))

        assert node.rightChild is not None
        assert node.leftChild is not None
        assert node.parent is not None

        delNode : SortedDictNode[K, T] = node
        nodeForFixup : SortedDictNode[K, T] = node
        fixupParent : SortedDictNode[K, T] = self._noneNode
        originalColor : Color = node.color

        if node.leftChild == self._noneNode:
            nodeForFixup = node.rightChild
            fixupParent = node.parent
            self._replaceNodes(node, node.rightChild)
        elif node.rightChild == self._noneNode:
            nodeForFixup = node.leftChild
            fixupParent = node.parent
            self._replaceNodes(node, node.leftChild)
        else:
            delNode = self._minimum(node.rightChild)

            assert delNode.rightChild is not None
            assert delNode.leftChild is not None
            assert delNode.parent is not None

            originalColor = delNode.color
            nodeForFixup = delNode.rightChild

            if delNode.parent == node:
                fixupParent = delNode
            else:
                self._replaceNodes(delNode, delNode.rightChild)
                delNode.rightChild = node.rightChild
                delNode.rightChild.parent = delNode
                fixupParent = delNode.parent


            self._replaceNodes(node, delNode)
            delNode.leftChild = node.leftChild
            delNode.leftChild.parent = delNode
            delNode.color = node.color

        if originalColor == Color.BLACK:
            self._deleteFixup(nodeForFixup, fixupParent)


    def _replaceNodes(self, u : SortedDictNode[K, T], v : SortedDictNode[K, T]) -> None:
        assert u.parent is not None

        if u.parent == self._noneNode:
            self._root = v
        elif u == u.parent.leftChild:
            u.parent.leftChild = v
        else:
            u.parent.rightChild = v

        if v != self._noneNode:
            v.parent = u.parent

    def _minimum(self, u : SortedDictNode[K, T]) -> SortedDictNode[K, T]:
        node : SortedDictNode[K, T] = u

        assert node.leftChild is not None

        while node.leftChild != self._noneNode:
            node = node.leftChild
            assert node.leftChild is not None

        return node

    def _deleteFixup(self, nodeForFixup : SortedDictNode[K, T], parent : SortedDictNode[K, T]) -> None:
        brother: SortedDictNode[K, T] = nodeForFixup
        while nodeForFixup != self._root and nodeForFixup.color == Color.BLACK:
            assert parent is not None
            assert parent.leftChild is not None
            assert parent.rightChild is not None

            if nodeForFixup == parent.leftChild:
                brother = parent.rightChild

                if brother.color == Color.RED:
                    brother.color = Color.BLACK
                    parent.color = Color.RED
                    self._left_rotate(parent)
                    brother = parent.rightChild

                assert brother.leftChild is not None
                assert brother.rightChild is not None
                assert parent.parent is not None

                if brother.leftChild.color == Color.BLACK and brother.rightChild.color == Color.BLACK:
                    brother.color = Color.RED
                    nodeForFixup = parent
                    parent = parent.parent
                else:
                    if brother.rightChild.color == Color.BLACK:
                        brother.leftChild.color = Color.BLACK
                        brother.color = Color.RED
                        self._right_rotate(brother)

                        assert parent is not None
                        assert parent.rightChild is not None

                        brother = parent.rightChild

                    assert parent is not None
                    assert brother.rightChild is not None

                    brother.color = parent.color
                    parent.color = Color.BLACK
                    brother.rightChild.color = Color.BLACK
                    self._left_rotate(parent)

                    nodeForFixup = self._root
                    parent = self._noneNode
            else:
                assert parent is not None
                assert parent.leftChild is not None

                brother = parent.leftChild

                if brother.color == Color.RED:
                    brother.color = Color.BLACK
                    parent.color = Color.RED
                    self._right_rotate(parent)
                    brother = parent.leftChild

                assert brother.leftChild is not None
                assert brother.rightChild is not None
                assert parent.parent is not None

                if brother.rightChild.color == Color.BLACK and brother.leftChild.color == Color.BLACK:
                    brother.color = Color.RED
                    nodeForFixup = parent
                    parent = parent.parent
                else:
                    if brother.leftChild.color == Color.BLACK:
                        brother.rightChild.color = Color.BLACK
                        brother.color = Color.RED
                        self._left_rotate(brother)

                        assert parent is not None
                        assert parent.rightChild is not None
                        assert parent.leftChild is not None

                        brother = parent.leftChild

                    assert parent is not None
                    assert brother.leftChild is not None

                    brother.color = parent.color
                    parent.color = Color.BLACK
                    brother.leftChild.color = Color.BLACK
                    self._right_rotate(parent)

                    nodeForFixup = self._root
                    parent = self._noneNode

        nodeForFixup.color = Color.BLACK

    def __iter__(self) -> Iterator[K]:
        return SortedDictKeyIterator(self._root, self._noneNode)

    def items(self) -> Iterator[tuple[K, T]]:
        return SortedDictItemIterator(self._root, self._noneNode)

    def __contains__(self, key : K) -> bool:
        return self._findNode(key) is not None

class SortedDictKeyIterator(Generic[K, T]):
    def __init__(self, root: SortedDictNode[K, T], none_node: SortedDictNode[K, T]) -> None:
        self._stack : list[SortedDictNode[K, T]] = []
        self._none : SortedDictNode[K, T] = none_node
        self._current : SortedDictNode[K, T] = root
        self._go_left()

    def _go_left(self) -> None:
        while self._current != self._none:
            assert self._current.leftChild is not None

            self._stack.append(self._current)
            self._current = self._current.leftChild

    def __iter__(self) -> Iterator[K]:
        return self

    def __next__(self) -> K:
        if not self._stack:
            raise StopIteration
        node : SortedDictNode[K, T] = self._stack.pop()

        assert node.key is not None

        result : K = node.key

        assert node.rightChild is not None

        self._current = node.rightChild
        self._go_left()

        return result

class SortedDictItemIterator(Generic[K, T]):
    def __init__(self, root: SortedDictNode[K, T], none_node: SortedDictNode[K, T]) -> None:
        self._stack : list[SortedDictNode[K, T]] = []
        self._none : SortedDictNode[K, T] = none_node
        self._current : SortedDictNode[K, T] = root
        self._go_left()

    def _go_left(self) -> None:
        while self._current != self._none:
            self._stack.append(self._current)

            assert self._current.leftChild is not None

            self._current = self._current.leftChild

    def __iter__(self) -> Iterator[tuple[K, T]]:
        return self

    def __next__(self) -> tuple[K, T]:
        if not self._stack:
            raise StopIteration
        node : SortedDictNode[K, T] = self._stack.pop()

        assert node.key is not None
        assert node.value is not None

        result : tuple[K, T] = (node.key, node.value)

        assert node.rightChild is not None

        self._current = node.rightChild
        self._go_left()

        return result

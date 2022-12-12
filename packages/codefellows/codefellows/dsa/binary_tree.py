from collections import deque


class BinaryTree:
    """
    Standard Binary Tree with adding, depth-first
    and breadth-first traversals
    """

    def __init__(self, root=None, values=None):
        self.root = root
        if values:
            for value in values:
                self.add(value)

    def __iter__(self):
        def value_generator():
            def walk(root):

                if not root:
                    return None

                yield root.value

                yield from walk(root.left)

                yield from walk(root.right)

            return walk(self.root)

        return value_generator()

    def pre_order(self, action=lambda x: None):
        """Pre Order traversal of tree.
        Applies optional action function to each node's value

        Args:
            action ([type], optional): [description]. Defaults to lambdax:None.
        """

        def walk(root, action):

            if not root:
                return

            action(root.value)
            walk(root.left, action)
            walk(root.right, action)

        walk(self.root, action or print)

    def in_order(self, action=lambda x: None):
        """In Order traversal of tree.
        Applies optional action function to each node's value

        Args:
            action ([type], optional): [description]. Defaults to lambdax:None.
        """

        def walk(root, action):

            if not root:
                return

            walk(root.left, action)
            action(root.value)
            walk(root.right, action)

        walk(self.root, action or print)

    def post_order(self, action=lambda x: None):
        """Post Order traversal of tree.
        Applies optional action function to each node's value

        Args:
            action ([type], optional): [description].
            Defaults to lambda x:None.
        """

        def walk(root, action):

            if not root:
                return

            walk(root.left, action)
            walk(root.right, action)
            action(root.value)

        walk(self.root, action or print)

    def breadth_first(self, action=lambda x: None):
        """Breadth First / Level Order traversal of tree.
        Applies optional action function to each node's value

        Args:
            action ([type], optional): [description]. Defaults to lambdax:None.
        """

        if not self.root:
            return

        action = action or print

        breadth = Queue()

        breadth.enqueue(self.root)

        while not breadth.is_empty():
            front = breadth.dequeue()

            action(front.value)

            if front.left:
                breadth.enqueue(front.left)

            if front.right:
                breadth.enqueue(front.right)

    def add(self, value):
        """Stores the given value in first empty spot following Breadth First search.

        Args:
            value (any): The value to store
        """

        node = Node(value)

        if not self.root:
            self.root = node
            return

        breadth = Queue()

        breadth.enqueue(self.root)

        while not breadth.is_empty():
            front = breadth.dequeue()
            if not front.left:
                front.left = node
                return
            else:
                breadth.enqueue(front.left)

            if not front.right:
                front.right = node
                return
            else:
                breadth.enqueue(front.right)

    def find_maximum_value(self):

        max = self.root.value

        def max_check(value):
            nonlocal max
            max = value if value > max else max

        self.pre_order(max_check)

        return max


class BinarySearchTree(BinaryTree):
    def add(self, value):
        def walk(root, node_to_add):

            if not root:
                return

            if node_to_add.value < root.value:
                if root.left:
                    walk(root.left, node_to_add)
                else:
                    root.left = node_to_add
            else:
                if root.right:
                    walk(root.right, node_to_add)
                else:
                    root.right = node_to_add

        node = Node(value)

        if not self.root:
            self.root = node
            return

        walk(self.root, node)

    def contains(self, value):
        def walk(value, root):

            if not root:
                return False

            return (
                root.value == value
                or walk(value, root.left)
                or walk(value, root.right)
            )

        return walk(value, self.root)


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Queue:
    def __init__(self):
        self.storage = deque()

    def enqueue(self, value):
        self.storage.appendleft(value)

    def dequeue(self):
        return self.storage.pop()

    def peek(self):
        return self.storage[-1]

    def is_empty(self):
        return len(self.storage) == 0

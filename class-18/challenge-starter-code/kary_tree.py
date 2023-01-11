from data_structures.queue import Queue


class KaryTree:
    def __init__(self, root=None):
        self.root = root

    def breadth_first(self):
        """
        returns list of values in breadth-first order, aka level order
        """
        queue = Queue()
        collection = []
        queue.enqueue(self.root)

        while not queue.is_empty():
            front = queue.dequeue()
            collection.append(front.value)
            for child in front.children:
                queue.enqueue(child)

        return collection

    def clone(self):
        """
        returns a "shallow" copy of the current tree as a new tree.
        Very handy for cases where you don't want to modify the original tree.
        """
        if not self.root:
            return KaryTree()

        def walk(source_root, clone_root):
            """
            recursive method to clone Nodes
            """
            if not source_root:
                return

            for source_child in source_root.children:
                clone_child = Node(source_child.value)
                clone_root.children.append(clone_child)
                walk(source_child, clone_child)

        clone_tree = KaryTree()

        clone_tree.root = Node(self.root.value)
        walk(self.root, clone_tree.root)

        return clone_tree


class Node:
    """K-Ary Tree Node"""

    def __init__(self, value):
        self.value = value
        self.children = []

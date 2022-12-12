class LinkedList:
    """
    Singly Linked List
    """

    def __init__(self, head=None, values=None):
        self.head = head

        if values:
            for value in reversed(values):
                self.insert(value)

    def __iter__(self):
        def value_generator():

            current = self.head

            while current:

                yield current.value

                current = current.next

        return value_generator()

    def insert(self, value):
        """
        Adds value to beginning (aka head) of list
        """
        self.head = Node(value, self.head)

    def includes(self, value):
        """
        returns True/False if value found in list
        """

        current = self.head

        while current:

            if current.value == value:
                return True

            current = current.next

        return False

    def __str__(self):
        """returns linked list in stringy form

        Returns:
            [string] -- e.g. { apple } -> { banana } -> NULL
        """
        output = ""

        for value in self:
            output += f"{{ {value} }} -> "

        return output + "NULL"

    def __eq__(self, other):
        """compares two linked lists for equivalent content

        Args:
            other ([list]): the
            "other" list

        Returns:
            [bool]: [True if equivalent]
        """

        if len(list(self)) != len(list(other)):
            return False

        other_iter = iter(other)

        for value in self:
            if next(other_iter) != value:
                return False

        return True

    def append(self, value):
        """"adds value to end of list"""

        node = Node(value)

        if not self.head:
            self.head = node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = node

    def insert_before(self, value, new_value):
        """"inserts new_value before the given value"""

        current = self.head

        while current and current.next:
            if current.next.value == value:
                node = Node(new_value, current.next)
                current.next = node
                return

            current = current.next

        raise TargetError(f"{value} not in list")

    def insert_after(self, value, new_value):
        """"inserts new_value before the given value"""

        current = self.head

        while current:
            if current.value == value:
                node = Node(new_value, current.next)
                current.next = node
                return

            current = current.next

        raise TargetError(f"{value} not in list")

    def kth_from_end(self, k):
        """returns the item k back from end"""

        leader = self.head

        follower = None

        paces_behind = 0

        while leader:

            leader = leader.next

            if follower:
                follower = follower.next
            elif paces_behind == k:
                follower = self.head
            else:
                paces_behind += 1

        if not follower:
            raise TargetError("k is out of range")

        return follower.value

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

        return self

    def __getitem__(self, index):
        if not self.head:
            raise IndexError()

        if index < 0:
            try:
                return self.kth_from_end(index + 1)
            except TargetError:
                raise IndexError

        current = self.head

        k = 0

        while current and k < index:
            current = current.next
            k += 1

        if current is None:
            raise IndexError()

        return current.value

    def __setitem__(self, index, value):
        # TODO: Should setting at empty indices be supported?
        current = self.head
        k = 0
        while current and k < index:
            current = current.next
            k += 1

        current.value = value

class Node:
    """
    Node for use in a Linked List
    """

    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_


class TargetError(ValueError):
    pass

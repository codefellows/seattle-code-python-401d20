class LinkedList:

    def __init__(self):
        self.head = None


    def __len__(self):
      return len(list(iter(self)))

    def __iter__(self):

      def generator_func():

        current = self.head

        while current:
          yield current.value
          current = current.next

      return generator_func()

    def append(self, value):

        node = Node(value)

        if not self.head:
            self.head = node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = node


class Node:
    def __init__(self, value, next_ = None):
        self.value = value
        self.next = next_


if __name__ == "__main__":
    produce = LinkedList()
    produce.append('apple')
    produce.append('banana')
    produce.append('cucumber')
    produce.append('dates')
    produce.append('endives')
    produce.append('falafel')

    # for item in produce:
    #     print(item)

    print('length = ', len(produce))





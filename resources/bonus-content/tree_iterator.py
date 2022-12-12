from codefellows.dsa.binary_tree import BinaryTree
import string

class IterableBinaryTree(BinaryTree):

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


tree = IterableBinaryTree(values=string.ascii_lowercase)

print(list(tree))

# for item in tree:
#     print(item)

uppers = [char.upper() for char in tree]

print(uppers)

vowels = [char for char in tree if char.lower() in 'aeiou']

print(vowels)

obj_tree = IterableBinaryTree(values=[
    {"name":"spam","votes":23},
    {"name":"bacon","votes":27},
    {"name":"eggs","votes":19},
])


most_popular = max(obj_tree, key = lambda o: o["votes"])

print("Most popular:", most_popular)

print(*obj_tree)

all_vowels = all([char in 'aeiou' for char in tree])

print(all_vowels)

any_a = any([char == 'a' for char in tree])

print(any_a)



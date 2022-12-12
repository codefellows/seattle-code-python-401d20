from codefellows.dsa.binary_tree import BinaryTree as BaseBinaryTree, Node


class BinaryTree(BaseBinaryTree):
    def to_grid(self):
        def binary_tree_to_grid(root, grid, row=0, column=0):

            if not root:
                return

            # create a new row in the grid when needed. Will be twice as long as previous row
            if len(grid) < row + 1:
                grid.append([None] * (2 ** row))

            # insert value in correct position
            grid[row][column] = root.value

            # double the column to left
            binary_tree_to_grid(root.left, grid, row + 1, column * 2)

            # double the column + 1 to the right
            binary_tree_to_grid(root.right, grid, row + 1, column * 2 + 1)

        grid = []

        binary_tree_to_grid(self.root, grid)

        return grid

    def render(self):

        grid = self.to_grid()

        # give appropriate amount of breathing room
        width = 2 ** (len(grid) + 2)

        fill = " "

        result = ""

        for index, row in enumerate(grid):
            if any([item for item in row]):
                padding = width // (2 ** index)
                line = ""
                for item in row:
                    section = f"( { item } )" if item else "*"
                    line += section.center(padding, fill)
                result += line + "\n\n"

        return result


if __name__ == "__main__":

    tree = BinaryTree(values=["A", "B", "C", "D", "E", "F", "G"])

    # Tweak things to make sure we handle sparse trees
    tree.root.right.left.left = Node("Z")
    tree.root.left.right = None
    tree.root.right.right.left = Node("X")

    result = tree.render()

    print(result)

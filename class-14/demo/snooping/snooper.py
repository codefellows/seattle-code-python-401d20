import pysnooper

@pysnooper.snoop(normalize=True)
def brackets_are_balanced(text):
    stack = []
    for ch in text:
        if ch == "{":
            stack.append(ch)
        elif ch == "}":
            if stack[-1] == "{":
                stack.pop()
            else:
                return False

    return len(stack) == 0


@pysnooper.snoop(normalize=True)
def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n - 1)


if __name__ == "__main__":

    # assert brackets_are_balanced("{x}")
    # assert not brackets_are_balanced("{}{")

    assert factorial(3) == 6

    print("*" * 36)
    print("*" * 10, "All Tests Pass", "*" * 10)
    print("*" * 36)

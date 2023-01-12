# Warm-Up Exercise: Lambda Functions

> Fix `calculate` function to flexibly handle math operations on two numbers.

## Feature Tasks

```python
"""
Calculator:
Your job is refactor this code to use a single calculate function
E.g. add, subtract,multiply, and divide.
Pass in lambda function.
"""

def calculate(a, b, operator_func):
    """
    Description of what calculate does
    Arguments:
      a (int or float)
      b (int or float)
      operator_func (function)
    Return:
      String
    """
    result = 0 # FIX ME
    return f"Given {a} and {b} the result of your operation is {result}"

if __name__ == "__main__":
    assert calculate(5,10, lambda x,y: 0) == "Given 5 and 10 the result of your operation is 15"
    assert calculate(5,10, lambda x,y: 0) == "Given 5 and 10 the result of your operation is -5"
    assert calculate(5,10, lambda x,y: 0) == "Given 5 and 10 the result of your operation is 50"
    assert calculate(5,10, lambda x,y: 0) == "Given 5 and 10 the result of your operation is 0.5"

    print("TESTS PASSED")
```

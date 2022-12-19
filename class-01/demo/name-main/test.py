def print_name():
    # __name__ is a built-in variable which evaluates to the name of the current module
    print(__name__)


# $ python test.py
if __name__ == "__main__":
    print_name()  # __main__

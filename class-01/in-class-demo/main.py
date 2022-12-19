from textwrap import dedent

def hello_world():
    print("Hello World!")


def favorite_color():
    """
    Asks for and prints a user's favorite color.
    """
    print("What is your favorite color?")
    fav_color = input("> ")
    print(f"Your favorite color is {fav_color}")

    print(dedent("""
    this
    is
    a
    test
    """))

    color_dict = {

    }

    ask_again = True
    while ask_again:
        print("Give another color?")
        choice = input("> ")
        if choice == "y":
            print("What is your favorite color?")
            fav_color = input("> ")
            print(f"Your favorite color is {fav_color}")
            if fav_color in color_dict:
                color_dict[fav_color] += 1
            else:
                color_dict[fav_color] = 1
        else:
            break
    print(f"the color choices are {color_dict}")


if __name__ == "__main__":
    # hello_world()
    favorite_color()

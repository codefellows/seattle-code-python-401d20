"""
Let's create the classic guessing game I Spy. We'll need...
- A list of things to guess
  - Each thing should be a dictionary with name and hints attributes
  - name is a string
  - hints is a list of strings
"""
things = [
    {
        "name": "billboard",
        "hints": [
            "bigger than a bread box",
            "rectangular",
            "changes periodically",
            "tells you something",
            "sells you something",
            "often see them in a rush",
        ],
    },
    {
        "name": "chair",
        "hints": [
            "has multiple legs",
            "has a restful interface",
            "not used in stand up meetings",
            "avoid electric ones",
        ],
    },
    {
        "name": "???",
        "hints": [
            "copies what you do",
            "is always changing color",
            "careful or it will bring you bad luck",
            "never lies to you",
            "fine with mom but not with mama",
        ],
    },
]


def guess_a_thing(riddle_index):

    thing = things[riddle_index]

    success = False

    guess = input("I spy with my little eye... ")

    hints = thing["hints"]

    correct_answer = thing["name"]

    while len(hints):

        if guess == correct_answer:
            success = True
            break

        hint = hints.pop(0)

        print(f"Nope, but here's a hint - {hint}")

        guess = input("I spy with my little eye... ")

    if success or guess == correct_answer:
        print("Crushed it")
    else:
        print(f"Too bad. It's a {correct_answer}")


if __name__ == "__main__":
    riddle_index = 0

    response = ""
    while response != "n":
        guess_a_thing(riddle_index)
        riddle_index += 1
        if riddle_index > 1:
            break
        response = input("Wanna play?")

    print("Thanks for playing!")

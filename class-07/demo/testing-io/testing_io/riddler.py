class Riddler:
    def __init__(self, riddle="my favorite color", answer="green"):
        self.riddle = riddle
        self.answer = answer

    def play(self):
        print("What is your name?")
        name = input("> ")
        print(f"Hi, {name}!")
        print(f"Step right up and guess {self.riddle}!")

        while True:
            print("What is your guess?")
            guess = input("> ")

            if guess == self.answer:
                print("You got it!")
                break
            else:
                print("Nope, that's not it.")

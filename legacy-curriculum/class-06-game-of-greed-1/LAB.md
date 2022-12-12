# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 06: Game of Greed

## Game of Greed 1

**This is a Solo assignment**

<!-- short description of project -->
Today you'll begin working on a command line version of the dice game `greed` using core Python tools and understanding of the basics of the language. The game is also known as Ten Thousand, Zilch or Foo.

## Specifications
<!-- Write a specification for the features required in this lab assignment -->
- Review [rules of game](https://en.wikipedia.org/wiki/Dice_10000){:target="_blank"}
- Play game [online](http://www.playonlinedicegames.com/farkle){:target="_blank"}

### Setup
- Create a repository with the exact name of `game-of-greed`.
- Start a branch in your `game-of-greed` repository called `class-01`
- Create a new virtual environment where we can locally scope our project installations and dependencies
- Create a file called `game_of_greed.py`
- Write a `README.md` file describing the program and how to run it. See the [README guidelines](../../resources/readme_guidelines.md){:target="_blank"} for tips on how to write an appropriate `README.md`. **Without a well documented and updated `README.md` you will lose 20% credit on the assignment.**

### Features
- Today is all about tackling the highest risk features - **scoring** and the **game flow**.
    - Define a Game class.
    - Handle calculating score for dice roll
        - Add `calculate_score` instance method to Game class.
        -   The input to `calculate_score` is a tuple of integers that represent a dice roll.
        -   The output from `calculate_score` is an integer representing the roll's score according to **rules of game**.
    - Begin work on verifying the game proceeds according to **game flow**
        - Add `play` instance method to Game class
        - Ensure that the initial **game flow** is followed
            - Greet user by printing 'Welcome to Game of Greed'
            - Prompt user with 'Wanna play?'
            - if user enters 'y' then print 'Great! Check back tomorrow :D'
            - if user enters anything else print 'OK. Maybe another time'
        - NOTE: use `Dependency Injection` to handle input/output.

### Testing - Game Flow
- When calling `play` method ensure...
    - proper greeting is displayed
    - proper prompt is then shown
    - proper display based on user input of 'y' or anything else

### Testing - Calculate Score
- test_zilch
	- non scoring roll should return 0
- test_ones
	- rolls with various number of 1s should return correct score
- test_twos
	- rolls with various number of 2s should return correct score
- test_threes
	- rolls with various number of 3s should return correct score
- test_fours
	- rolls with various number of 4s should return correct score
- test_fives
	- rolls with various number of 5s should return correct score
- test_sixes
	- rolls with various number of 6s should return correct score
- test_straight
	- 1,2,3,4,5,6 should return correct score
- test_three_pairs
	- 3 pairs should return correct score
- test_two_trios
	- 2 sets of 3 should return correct score
- test_leftover_ones
	- 1s not used in set of 3 (or greater) should return correct score
- test_leftover_fives
	- 5s not used in set of 3 (or greater) should return correct score

## Submission
1. Create a pull request from your feature branch to your `master` branch.
2. In your open pull request, leave as a comment [a checklist](https://github.com/blog/1825-task-lists-in-all-markdown-documents){:target="_blank"} of the specifications, with the actual specifications you completed checked off.
3. Copy the link to your open pull request and paste it into the Canvas assignment for this day.
4. Leave any comments you may have about the assignment in the comments box. This includes any difficulties you may have had with the assignment.
5. Merge your feature branch into `master`

## Rubric
- 7pts: Program meets all requirements described in Lab directions.

	Points  | Reasoning |
	 ------------ | :-----------: |
	7       | Program runs as expected, no exceptions during execution |
	5       | Program meets all of the  functionality requirements described above (including tests) // Program runs/compiles, Program contains logic/process errors|
	4       | Program meets most of the functionality requirements described above (including tests)  // Program runs/compiles, but throws exceptions during execution |
	3       | Program missing most of the functionality requirements described above // Program runs/compiles |
	2       | Missing Readme Document // Readme Document does not meet standards |
	0       | Program does not compile/run. Build Errors // Required naming conventions not met |
	0       | No Submission |

- 3pts: Code meets industry standards
	- These points are only awardable if you score at minimum a 5/7 on above criteria

	Points  | Reasoning |
	 ------------ | :-----------: |
	3       | Code meets Industry Standards // method and variable names are appropriate // Selective and iterative statements are used appropriately, Fundamentals are properly executed // Clearly and cleanly commented // Frequent Commits |
	2       | syntax for naming conventions are not correct (camelCasing and PascalCasing are used appropriately) // slight errors in use of fundamentals // Missing some comments // minimal or no commits |
	1       | Inappropriate naming conventions, and/or inappropriate use of fundamentals // Code is not commented  |
	0       | No Submission or incomplete submission |

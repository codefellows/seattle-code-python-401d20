# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 08: Game of Greed

## Game of Greed 3

**This is a Solo assignment**

<!-- short description of project -->
Today you'll continue work on a command line version of the dice game `greed`.

## Specifications
<!-- Write a specification for the features required in this lab assignment -->
- Review [rules of game](https://en.wikipedia.org/wiki/Dice_10000){:target="_blank"}
- Play game [online](http://www.playonlinedicegames.com/farkle){:target="_blank"}

### Setup
- Continue work in `game-of-greed` repository.
- Start a branch in your `game-of-greed` repository called `class-03`
- Activate virtual environment where we can locally scope our project installations and dependencies
- Add to `README.md` file as needed

### Features
- Application should implement features from class 1 and 2
- Particularly should test for `flow` using the approach in `test_game_flow.py` found in today's demo folder.
- Should handle when cheating occurs.
    - Or just typos.
    - E.g. roll = `[1,3,5,2]` and user keeps `1, 1, 1, 1, 1, 1`
- Should allow user to continue rolling with 6 new dice when all dice have scored in current turn.
- Handle **zilch**
    - No points for round, and round is over
- Any other questions refer to game doc or the online game or ask.


### Testing
- define tests to confirm new features

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

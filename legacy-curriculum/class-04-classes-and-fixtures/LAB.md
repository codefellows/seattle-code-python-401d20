# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 04: Classes

## Classes in Python

**This is a Solo assignment**

<!-- short description of project -->
Pythonic Garage Band

## Specifications
<!-- Write a specification for the features required in this lab assignment -->
Use Python classes to model a `Band` made up of different kinds of musicians. Start with `Guitarist`,`Bassist`, and `Drummer`. Make use of a `Musician` base class to handle common functionality which particular kinds of musicians will inherit.

### Setup
- create a `pythonic-garage-band` repo in Github
- Start a branch in your repository called `class-04`
- Create a new virtual environment where we can locally scope our project installations and dependencies
- Add any standard configuration files such as `.editorconfig`, `.gitignore`, etc.
- Write a `README.mnd` file describing the program and how to run it. See the [README guidelines](../../resources/readme_guidelines.md){:target="_blank"} for tips on how to write an appropriate `README.md`. **Without a well documented and updated `README.md` you will lose 20% credit on the assignment.**

### Features/Testing

- `Band` Tests
    - A `Band` instance should have a `name` attribute which is a string.
    - A `Band` instance should have a `members` attribute which is a list of instances that inherit from `Musician` base (or super) class.
    - A `Band` instance should have a `play_solos` method that asks each member musician to play a solo, in the order they were added to band.
    - A `Band` instance should have appropriate `__str__` and `__repr__` methods.
    - A `Band` should have a class method `to_list` which returns a list of previously created `Band` instances
    - A `Band` should have a static method `create_from_data` which takes a collection of formatted data and returns a created `Band` instance. The `Band` instance should have its members be set to musicians based on info from the input.
- `Musician` Subclass Tests
    - Each kind of `Musician` instance should have appropriate `__str__` and `__repr__` methods.
    - Each kind of `Musician` instance should have a `get_instrument` method that returns string.
    - Each kind of `Musician` instance should have a `play_solo` method that returns string.



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

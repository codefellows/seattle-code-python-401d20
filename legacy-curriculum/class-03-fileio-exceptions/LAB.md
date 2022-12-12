# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 03: File IO and Exceptions

## File IO and Exceptions

**This is a Solo  assignment**
<!-- short description of project -->
In this lab assignment you will be creating another command line game which takes advantage of Python's built in capabilities for reading and writing files.


## Specifications
<!-- Write a spefication for the features required in this lab assignment -->

### Setup
- Create a repository with the exact name of `madlib-cli`.
- Start a branch in your repository called `class-03`
- Create a new virtual environment where we can locally scope our project installations and dependencies
- Add any standard configuration files such as `.editorconfig`, `.gitignore`, etc.
- Write a `README.mnd` file describing the program and how to run it. See the [README guidelines](../../resources/readme_guidelines.md){:target="_blank"} for tips on how to write an appropriate `README.md`. **Without a well documented and updated `README.md` you will lose 20% credit on the assignment.**


### Features
- Create a file called `madlib.py`, which will contain all of the Python code that you will write relating to your Madlib game.
- Create a file called `test_madlib.py` which will be used to test your executable command line script.
- Keeping in mind the concept of [Single Responsibility Principle](https://en.wikipedia.org/wiki/Single_responsibility_principle){:target="_blank"}, build a command line tool which will perform the following:
    - Print a welcome message to the user, explaining the Madlib process and command line interactions
    - Read a template Madlib file ([Example](./assets/sample_template.txt){:target="_blank"}), and parse that file into usable parts.
        - _You need to decide what components of this file are useful, and how to break those useful pieces apart_
    - Once you know what parts of the template need user input, such as `Adjective`, prompt the user to submit a series of words to fit each of the required components of the Madlib template.
    - With the collected user inputs, populate the template such that each provided input is placed into the correct position within the template.
    - After the resulting Madlib has been completed, provide the completed response back to the user in the command line.
    - Write the completed template ([Example](./assets/sample_output.txt){:target="_blank"})to a new file on your file system (in the repo).


### Testing
- Every bit of functionality that you add should be tested.
- As a general rule at this time, you should have a test for valid, invalid, and edge case variants for every function that you define. There are exceptions. The exceptions are not the rule.


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

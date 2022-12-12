# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 02: Modules and Testing

## Modules and Testing

**This is a Solo assignment**
<!-- short description of project -->
The [Fibonacci Series](http://en.wikipedia.org/wiki/Fibbonaci_Series){:target="_blank"} is a numeric series starting with the integers 0 and 1. In this series, the next integer is determined by summing the previous two. This gives us:
```python
0, 1, 1, 2, 3, 5, 8, 13, ...
```
The [Lucas Numbers](http://en.wikipedia.org/wiki/Lucas_number){:target="_blank"} are a related series of integers that start with the values 2 and 1 rather than 0 and 1. The resulting series looks like this:
```python
2, 1, 3, 4, 7, 11, 18, 29, ...
```

## Specifications
<!-- Write a spefication for the features required in this lab assignment -->

### Setup
- Create a repository with the exact name of `math-series`.
- Start a branch in your repository called `class-02`
- Create a new virtual environment where we can locally scope our project installations and dependencies
- Add any standard configuration files such as `.editorconfig`, `.gitignore`, etc.
- Write a `README.mnd` file describing the program and how to run it. See the [README guidelines](../../resources/readme_guidelines.md){:target="_blank"} for tips on how to write an appropriate `README.md`. **Without a well documented and updated `README.md` you will lose 20% credit on the assignment.**

### Features
- Create a module `series.py`.
- Add a file `test_series.py` to your repository. As you work on the tasks below, use TDD practices. Write tests first, then implement code. Make small changes with many cycles of Red-Green-Refactor

_This is not an overly long assignment, so take the time to do the testing right._

- Create a function called `fibonacci`. The function should have one parameter `n`. The function should return the nth value in the fibonacci series. You may implement the function using recursion or iteration. If you are feeling particularly frisky, do both as separate functions.

- Ensure that your function(s) has a well-formed docstring

- In your `series.py` module, add a new function `lucas` that returns the nth value in the lucas numbers Again, you may use recursion or iteration, or both. Again, ensure that your function has a well-formed docstring.

- Both the fibonacci series and the lucas numbers are based on an identical formula. Add a third function called `sum_series` with one required parameter and two optional parameters. The required parameter will determine which element in the series to print. The two optional parameters will have default values of 0 and 1 and will determine the first two values for the series to be produced.

- Calling this function with no optional parameters will produce numbers from the fibonacci series. Calling it with the optional arguments 2 and 1 will produce values from the lucas numbers. Other values for the optional parameters will produce other series. Again, you may use recursion or iteration, or both. Again, ensure that your function has a well-formed docstring.

- Add your `series.py` and `test_series.py` modules to your repository and commit frequently while working on your implementation. Include good commit messages that explain concisely both what you are doing and why.


### Testing
- Your test requirements for today are simple. Do what you can, but try. Flex those new muscles!!


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

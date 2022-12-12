# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 44: Open-Source Software

## Find and contribute to an Open Source Project!

**This is a Pair assignment**
<!-- short description of project -->
Today you and your partner will find and develop a meaningful way to contribute back to the Python development community at large by finding an open source project which you can participate in (you may not actually make it all the way to a PR today).

## Specifications
<!-- Write a spefication for the features required in this lab assignment -->

### Setup
- Review the resources in today's [Readings](./READINGS.md){:target="_blank"} for ideas on how and where to start with finding a project that interests you and your partner
    - *Note: Documentation fixes are not acceptable for this assignment unless approved by your instructor*
    - Focus your search on areas which you can contribute to the code base or writing additional tests!
- Once you've found a project of interest and, more specifically, an issue which you and your partner feel you can meaningfully contribute to... fork and clone the project
- Add your partner to the fork as a collaborator

### Features
- Identify a specific issue (documented or not) within the project of your choosing, and document your findings in a [Root Cause Analysis](https://en.wikipedia.org/wiki/5_Whys){:target="_blank"}
    - *Note: your 5-whys RCA should be created and stored outside of your project fork (it's for your own purposes, but you will turn that in with this assignment)*
    - For example:
        1. Update a small library from Python 2.7 to 3.6
        2. Write three meaningful tests (testing areas which have poor coverage) within an existing library to provide further test coverage withing the library
        3. Identify an area of code which could be optimized by refactoring the codebase; i.e. list comprehension vs map (circumstantial...)
- Determine a solution to the issue with your partner, and document your solution in your RCA
- Determine what areas of the project you need to improve outside of just code contributions; i.e. documentation, testing, etc...

- (Stretch) Implement your changes, and submit a PR to the upstream repository

### Testing
- No standalone testing requirements for this lab. You should test as necessary as part of your contributions.

## Submission
1. Create a pull request from your feature branch to your `master` branch.
2. In your open pull request, leave as a comment [a checklist](https://github.com/blog/1825-task-lists-in-all-markdown-documents){:target="_blank"} of the specifications, with the actual specifications you completed checked off.
3. Copy the link to your open pull request and paste it into the Canvas assignment for this day.
4. Upload your RCA document, and leave any comments you may have about the assignment in the comments box. This includes any difficulties you may have had with the assignment.
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

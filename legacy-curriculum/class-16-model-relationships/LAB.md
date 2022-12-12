# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 16: Model Relationships

## One to Many Relationships with SQLAlchemy

**This is a Solo  assignment**

<!-- short description of project -->
Build a RESTful API with 2 or more related tables.


### Setup
- Refer to today's demo for required dependencies


### Features
- Use Flask, Flask-SQLAlchemy, Flask-Migrate to create RESTful API for 2 resources
	- Use demo as guide, but don't use Band and Artist of course ;)
- Use Application Factory pattern to allow easy testing of Database
- Relate the models as `1 to Many`
- Use Pytest fixtures to test API routes
- Properly initialize and migrate Models to datbase

### Testing
- Test Get All, Get One and Create Routes for each resource
- Store cross module test fixtures in conftest.py
	- NOTE: Back off to coding in each test module as needed
- WARNING: If unexpected pytest import errors occur try `python -m pytest` from root of project



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

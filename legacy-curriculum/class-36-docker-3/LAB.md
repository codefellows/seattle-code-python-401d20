# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 36: CircleCI

## Continous Integration with CircleCI

**This is a Solo  assignment**

<!-- short description of project -->
Configure your Python application to be automatically verified before allowing feature branch to be merged with master.

## Specifications
- Work in your own `snakes-on-a-plane/backend` repository
- Set up account with CircleCI
    - I logged in with Github authentication which made integration easier
- In root of project (aka the root of repo) create a `.circleci` folder
    - Within folder create `config.yml` file  
    - Copy full config.yml from bottom of [Configuring a Python Application on CircleCI](https://circleci.com/docs/2.0/language-python/){:target="_blank"}
		- Tweak as needed for desired versions of Python and Postgres
- Install CircleCI Local CLI following [these steps](https://circleci.com/docs/2.0/local-cli/){:target="_blank"}
    - This is optional (strictly speaking) but allows you to catch config issues early which is always better
    - Much of the doc covers alternate work flows as well, so skim over those and just use as reference for the work we do together today
    - run `$ circleci local execute` 
		- Takes a while the first time
	- Eventually, if no tests fail, you'll see something like below near end of terminal output
	```
	Ran X tests in y.000s

	OK
	```
	- Or you'll see a report about failing tests.
	- If you don't already have a failing test then add one now
		- e.g. 
	```
	def test_fail(self):
		self.assertTrue(False) 
	```
- Integrate CircleCI with Github
- Add your Github project with CircleCI
	- Make sure you've selected your `snakes-on-a-plane` organization.
- Protect `master` branch to require `ci/circleci:build` status checks to pass.
- Push a feature branch with failing test and create a pull request
- View pull request status in Github and confirm that failed status is reflected.
- Fix the bug and push change to Github.
- Confirm that pull request now passes status check
	


## Submission
- Submit 2 screenshots
	1. A screenshot of Pull Request failing status check
	2. A screenshot of Pull Request passing status check

## Stretch:
- Research the Deplyment options

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

# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 18: Deployment

## Deploying Front and Back End Apps

**This is a Solo  assignment**

<!-- short description of project -->
We will use a Platform as a Service Provider to host our apps. Each type of app has different hosting requirements and potential price points.

## Specifications
<!-- Write a spefication for the features required in this lab assignment -->
Apps do not need to be feature complete but they do need to be deployable. Aka must not have any fatal errors that prevent running.


### Setup
- Sign up with render.com
    - No need for credit card
- Follow instructions for deploying Flask app
- STRETCH: Follow instructions for deploying Create React App

### Features
- Add gunicorn as a dependecy
	- `pipenv install gunicorn`
- You will need to convert your dependencies to requirements.txt
	- `pipenv run pip freeze > requirements.txt`
	- commit generated requirements.txt
	- regenerate requirements.txt whenever dependencies are updated
		- Note: Make sure you've run `pipenv install` before freezing requirements
- In case of issues refer to [example](https://github.com/render-examples/flask-hello-world){:target="_blank"}

### Testing
- No testing requirements

## Submission
1. Submit url(s)s for app(s) deployed on render.com
4. Leave any comments you may have about the assignment in the comments box. This includes any difficulties you may have had with the assignment.

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

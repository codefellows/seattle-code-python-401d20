# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 38: DRF

## Implement RESTful endpoints for authentication in your application

**This is a Solo assignment**
<!-- short description of project -->
Today you'll implement token-based authentication for your application through the use of RESTful architecture. Your users will have the ability to register and login to your app through an endpoint provided by Django REST Framework.

## Specifications
<!-- Write a spefication for the features required in this lab assignment -->

### Setup
- Working in your `budget_tool` repository, create a well named branch for today's work
- Install DRF as a dependency in your project
- Create a new app in your project called `budget_api`

### Features
- In your `budget_api` app
    - Create a `UserSerializer` class for handling `User` model interactions through your API
    - Create a `UserAPIView` class for handling both a creation and retrieval of a `User` model instance
        - `POST` should accept valid inputs and create the new user and return that user data (**without the password**) to the client
        - `POST` should accept valid inputs for authentication and return a token to the client for subsequent authenticated requests to the API
    - Create a `user/` endpoint to handle the class views for this portion of the API, and ensure that these endpoints are mounted to a base path of `api/v1/` at the project root's `urls.py`

### Testing
- You are required to meet or exceed an 80% coverage benchmark for this application.
- Your focus today is to integration test your API; specifically the new RESTful endpoints created for user registration and login


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

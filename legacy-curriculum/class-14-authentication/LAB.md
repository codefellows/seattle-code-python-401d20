# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 14: Authentication

## Adding Security and Permissions to your API

**This is a Solo assignment**
<!-- short description of project -->
Today will mark a point of basic functionality for your application. You will implement user authentication and authorization, which completes what could be considered basic requirements for the app to function independently and securely. We aren't done yet with features for this app, but your job today is to implement the ability for users to be registered, logged in, and then subsequently interface with the application. If the auth portion is not functional anyone can interact with anything, and that's just not okay!

## Specifications
<!-- Write a spefication for the features required in this lab assignment -->

### Setup
- Working in your `stocks_portfolio` repository, create a well named branch for today's work.

### Features
- In `models.py`:
    - Create a `User` model with a `__init__` method, which allows your users password to be hashed by `passlib` before being stored in the database
    - Ensure that your model relationships are updated to support the [entity rel diagram provided](./assets/entity_rel_diagram.png){:target="_blank"}
    - Create a `check_credentials` class method on your `User` model which allows a verification of email and password, and returns `False` on validation failure or `True` on validation success.
- In the `src/` directory, create a new file called `auth.py` 
    - Create a new view controller for each of the following:
        - `register` - Create a new user, and 
        - `login`
        - `logout`
    - Create a new decorator for views called `login_required` which restricts view controller logic to authenticated users, and redirects to the `/login` route if a user attempts to manually navigate to one of those views. 

### Testing
- You are required to meet or exceed an 80% coverage benchmark for this application.
- As of today you will need to allow your tests to make authenticated requests, which requires some additional set up an tear down for your test suite. Ensure that you're able to associate an authenticated user with your test client for these tests!


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

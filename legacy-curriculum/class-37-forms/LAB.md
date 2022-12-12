# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 37: Django Forms

## Add form inputs to your Django application

**This is a Solo assignment**
<!-- short description of project -->
Today you'll be adding form inputs to your templates, which will allow you to add new Budgets and Transactions to your site.

## Specifications
<!-- Write a spefication for the features required in this lab assignment -->

### Setup
- Working in your `budget_tool` repository, create a well named branch for today's work

### Features
- Construct views in your `budgets` application that allow the creation of `Budget` and `Transaction` instances
- From the primary view of your budgets (list view), add a prominent button that allows for easy navigation to a form input for a new `Budget`
- From the detail view of any `Budget` instance, add a prominent button that allows for easy navigation to a form input for a new `Transaction`
- When a form is submitted, the user should be redirected to the list or detail view which provided the form link in reference

### Testing
- You are required to meet or exceed an 80% coverage benchmark for this application.
- You do **not need** to test the form inputs themselves; i.e. Selenium testing or some other headless browser test feature
- You do **need** to unit test the endpoints, and additional view controller or model functionality
- You do **need** to integration test the endpoints and req/res cycle throughout your application


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

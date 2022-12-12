# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 42: React/Django

## Build a React Client for your Django Application

**This is a Pair assignment**
<!-- short description of project -->
Today you'll be building a ReactJS client-side application, which will closely mirror to existing Django application you've already built! Despite the resemblance, your React app will interact exclusively with your DRF endpoints.

## Specifications
<!-- Write a spefication for the features required in this lab assignment -->

### Setup
- Create a new repository called `budget_client`, and add your partner as a collaborator
- In your `budget_client` repository, create a well named branch for today's work

### Features
- Create the following components and structure them according to the following diagram
```
App
    Landing
        LoginForm
    Main
        BudgetList
            BudgetDetail
                TransactionList (Stretch)
                TransactionForm (Stretch)
        BudgetForm
```
- Wire up your React front end to the previously built restful API from Lab 39
- Show Landing component when not logged in.
- Show Main component when logged in.
- Determine best location for application state.
- BudgetForm should collect user input required to create a budget via restful API.
- Create Budget via API when BudgetForm submitted
- Ensure your restful API supports Cross Origin Requests.
- ***Stretch:*** Style components (even better with Sass)
- ***Stretch:*** Add TransactionList and TransactionForm components
- ***Stretch:*** Add ability to register a user. Otherwise use HttPie/Postman to register user directly on your API

### Testing
- No testing requirements for this lab.


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

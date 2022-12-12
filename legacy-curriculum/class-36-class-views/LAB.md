# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 36: Class-based Views

## Simple Budgeting Application with Django

**This is a Solo assignment**
<!-- short description of project -->
Today you'll be scaffolding a new Django application to help manage some of your basic financial data, though probably best to not put any actual data in here just yet! Your focus today is scaffolding, deployment and implementing the new class-based view controllers in place of function views.

## Specifications
<!-- Write a spefication for the features required in this lab assignment -->

### Setup
- Create a new repository called `budget_tool` and a well named branch for today's work
- Implement `django-registration` for this application to allow for user sign-up/sign-in

### Features
- Create a `budgets` application within the project
    - Implement a `Budget` model for your application which should have the following attributes:
        - `id`: Primary Key / Integer
        - `user`: ForeignKey(`User`)
        - `name`: String
        - `total_budget`: Float
        - `remaining_budget`: Float (`@property` calculation)
            - Stretch: figure out `@property` on own, otherwise ask TA/Teacher.

    - Implement a `Transaction` model for your application which should have the following attributes:
        - `id`: Primary Key / Integer
        - `budget`: ForeignKey(`Budget`)
        - `type`: Choices(withdrawal, deposit)
        - `amount`: Float
        - `description`: String

    - Create class views for this application:
        - `BudgetListView`: List all available budgets owned by current user
        - `BudgetDetailView`: List all available transactions within the selected budget

    - Create a template for each of the above view controllers
    - Configure the application's `urls` with the projects `urls`
    - Ensure that your site is styled, and that you are managing any other static assets appropriately

### Testing
- You are required to meet or exceed an 80% coverage benchmark for this application
- As of today, you will have a fairly basic application, though some of your previous tests should translate pretty quickly to what you've created here
- Ensure that you've unit tested all of your view controllers, and that your integration tests have at least covered basic status codes and response content for each endpoint
- Stretch: explain use of Factories


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

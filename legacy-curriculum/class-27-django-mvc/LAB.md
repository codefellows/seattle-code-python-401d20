# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 27: Django MVC

## Add Models, Views, and Controllers

**This is a Solo assignment**
<!-- short description of project -->
Today you will continue building an application for managing all the various books you own (*lets assume you own a lot...*). In order to implement this application, you will need to iterate on your `django_lender` application and add a model, views (templates), and controllers (views).

## Specifications
<!-- Write a spefication for the features required in this lab assignment -->

### Setup
- Working in your `django_lender` repository, create a well named branch for today's work

### Features
- Add your new app to the `settings.py`, and configure the `urls` for this new app at the root level of your project
- Working in the `lender-books/` directory:
    - Create a new model for `Book`, which represents an item that will be lent to another person, with the following attributes
        - `title`: Text field
        - `author`: Text field
        - `year`: Integer field for year published
        - `status`: Multiple choice field for `available` or `checked-out` statuses
        - `date_added`: Auto-generated date field
        - `last_borrowed`: Auto-updated date field
    - Create a new template called `book_list.html` that inherits from `base.html`, which will render out a list of all books in the system for the current user
    - Create a new template called `book_detail.html` that inherits from `base.html`, which will render out the detail for a single book
    - Create a simple view controller for each of the templates defined above
    - Create a `urls.py` for this app, which connects your view controllers and their templates to your application at an appropriate route
- Use `docker-compose` to run `makemigrations` and `migrate` once you've configured your new model.
- You will want to use the Admin console to add some records to your database, so you can verify that data is correctly rendering on the site
- Run your application and ensure that all things are as they should be!

### Stretch Goals
- Use 3rd party or custom template tags to render out `date_added` and `last_borrowed`


### Testing
- You are required to meet or exceed an 80% coverage benchmark for this application.
- Your focus for the time being will be unit testing your view controllers and models, and you should follow our standard format of roughly three test assertions for each controller or model you define for the application
    - *Note: Be sure you do not test functionality that Django provides*


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

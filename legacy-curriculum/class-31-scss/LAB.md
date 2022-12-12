# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 31: SASS/SCSS

## Style your application

**This is a Pair assignment**
<!-- short description of project -->
Today you and your partner will focus on the fundamentals of managing static assets, you will also begin working with a preprocessed style syntax (SCSS). You'll also get to exercise what you've already learned by rebuilding a small Django app from scratch before working on today's lab!

## Specifications
<!-- Write a spefication for the features required in this lab assignment -->

### Setup
- Create a new repository called `kickstarter_projects`, and add your partner as a collaborator
- Working in your new repository, create a well named branch for today's work
- Navigate to the Kaggle page for [Kickstarter Projects Data set](https://www.kaggle.com/kemical/kickstarter-projects/data){:target="_blank"} and download the 2018 `csv` data-set into an `assets/` directory within your repo
- Create a new Django application in the root of your repository, and configure your project scaffold
    - update your settings to use environment variables rather than hard-coded values
    - change your database connections
- Create a new app in the project called `project_data`
    - configure a `Project` model to match the data that you'll be loading into your database
    - Using `pandas` and `sqlalchemy` (as developer dependencies) clean your data set and ensure that there are no `NA` fields, and that the columns of data are in a generally usable state for analysis
    - create your migrations and migrate your new model to a database table
    - using the [provided script](./assets/load_db.py){:target="_blank"} as a base (you need to fine tune and further configure) load your data-set into the database
    - configure your `urls` and `views` to provide routing and responses for either a list of projects or a single detail project page view
    - create your `templates` for each view; list or detail

- *Note: you do not need to add authentication to this application*

- You should have a basic application that shows database records for Kickstarter project data at this point - in the form of a list of projects and a single project's detail page

### Features
- Following the general guidelines of SMACSS principles, create a series of `*.scss` stylesheets for your application, beginning with a `base.scss`, `vars.scss`, and any other generalized stylesheets
- Within your Django app, you should also have localized `*.scss` stylesheets which are specific to the `project_data` component
- In order to process those stylesheets into `*.css` static files, you will be implementing the`django-sass-processor` package found [HERE](https://github.com/jrief/django-sass-processor){:target="_blank"}
    - Follow the installation instructions, and then further the setup instructions on GitHub to set up and provide a processor for your application's stylesheets
    - Ensure that you've followed the instructions all the way through understanding how this package enables collection of static assets for production deployment

### Testing
- No test requirements for this lab.

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

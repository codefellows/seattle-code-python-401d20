# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 27: Django Models

## Django Models

Django has a powerful Object Relational Mapper that allows us to persist data using Python instead of SQL.

Today you'll build out a project with one model, wire up that model using Django Views, and give it a little style as well.

**This is a Solo assignment**

## Setup

- Create `django-models` repo

## Features

**NOTE: Replace `blog` and `Post` with names of your choosing.**

- create `blog` project
- create `blog` app
- migrate data
- create `Post` model
  - Have 3 fields, one must be ForeignKey related to `auth.User` E.g.
    - add `title` CharField property
    - add `author` ForeignKey property related to `auth.User` with CASCADE delete option.
    - add `body` TextField property
- activate the model
- add model to admin
- modify `Post` model have user friendly display in admin
- create migrations and migrate data
- create a super user
- create `HomePageView`
  - extend `ListView`
  - give a template of `home.html`
  - associate `Post` model
- create `home.html` template
  - in `templates` folder in root of project
  - register `templates` folder in project settings
  - use `Django Templating Language` to display each post's title and body
- create `base.html` ancestor template
  - add main html document
  - use `Django Templating Language` to allow child templates to insert content
- update `HomePageView` to provide explicit name for object list
- update url patterns for app and project
- add 4 posts in admin
- view home page and confirm 4 posts showing properly
- create `PostModelTest`
  - create `Post` object in set up
  - create test to verify the post's text is correct
- create `HomePageViewTest`
  - test view's status code
  - test view using correct template
  - use url name instead of hard coded path
- add styling
  - create static folder at root of project
  - update STATICFILES_DIRS
  - create base.css file which styles base.html elements
  - load static css in base.html file
- add detail view
  - link `post_detail.html` template
  - associate `Post` model
- create `post_detail.html` template
  - template should extend base
  - content should display post title and body
- update app urlpatterns to handle detail view
  - account for primary key in url
- add link in home page template to related post detail page
- add blog tests
  - create a user and post before each test
  - verify proper string representation of a `Post` instance
  - verify `Post` instance content
  - verify `PostListView`
  - verify `PostDetailView`

## Stretch Goals

- add multiple models
- use an alternate test runner
- add more advanced fields to models, e.g. created time stamp

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

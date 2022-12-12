# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 31: Django REST Framework & Docker

Use Django REST Framework to create an API, then "containerize" it.

**This is a Solo assignment**

## Setup

**NOTE: Replace `blog` and `Post` with names of your choosing.**

- Create `blog-api` Github repository.
- Create Django project
- Install Docker
  - Refer to today's readings for directions.
- Create a Docker container to host your Django site.

## Features - Django REST Framework

- Install `django` and `djangorestframework` packages.
- Create `blog_project` Django project
- Create `posts` app.
- Add/Update `models, views, urls and serializers` portions of site to enable a DRF driven API.
- Confirm your app is working by "kicking the tires" with the development tools available. E.g.
  - Admin console
  - DRF browsable API
  - Development server

## Features - Docker

- **NOTE** Refer to today's readings for built out `Dockerfile` and `docker-compose.yml` examples.
- create `Dockerfile` based off `python:3.7-slim`
- create `docker-compose.yml` to run Django app as a `web` service.
- enter `docker-compose up --build` to start your site.
- Go to browsable api and confirm site is operational.

## Stretch Goals

- Research using a production server vs. the built in development server.
- Research using postgres instead of sqlite as database.

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

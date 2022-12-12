# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 33: Authentication & Production Server

Let's move our API closer to production grade by adding Authentication and switching to a Production Server

**This is a Solo assignment**

## Setup

- Update Github repository from previous lab.
- Install Docker if haven't already in previous lab.
- Create a Docker container to host your API.

## Features - Django

- Add JWT Authentication to your API.
  - Install needed libraries in Pipfile and/or site settings.
- Keep existing authentication so DRF Browsable API still usable.
  - That includes keeping the styling
  - Install needed libraries in Pipfile and/or site settings.


## Features - Docker

- Create a boilerplate `Dockerfile` and `docker-compose.yml` so you don't need to start from scratch each time.
- Switch to using [Gunicorn](https://gunicorn.org/){:target="_blank"} instead of Django's built in development server.
  - mind the number of workers to avoid sluggishness
- **Warning** You will run into styling issues when you switch over to Gunicorn. On Django side you'll need to properly handle static files.

## Snippets

- Refer to [SNIPPETS](./resources/SNIPPETS.md){:target="_blank"} as needed.

## Stretch Goals

- Research deployment options for Docker/Postgres/Django and report findings to class
- Create a `seed` project on Github so that you can have a running start on next DRF project.

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

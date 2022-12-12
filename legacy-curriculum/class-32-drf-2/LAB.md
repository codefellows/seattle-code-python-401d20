# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 32: DRF Permissions / Postgresql

Let's move our site closer to production grade by adding Permissions and Postgresql Database.

**This is a Solo assignment**

## Setup

**NOTE: Replace `blog` and `Post` with names of your choosing.**

- Create new `blog-api` Github repository.
  - Yes, from scratch.
- Install Docker if haven't already in previous lab.
- Create a Docker container to host your Django site.

## Features - General

- Get messy!
  - add more models
  - relate those models
  - make additionss/changes to models in several steps

## Features - Django REST Framework

- Make your site a DRF powered API as you did in previous lab.
- Adjust project's permissions so that only authenticated user's have access to API.
- Add a custom permission so that only author of blog post can update or delete it.
- Add ability to switch user's directly from browsable API.


## Features - Docker

- **NOTE** Refer to previous lab for built out `Dockerfile` and `docker-compose.yml` examples.
- create `Dockerfile` based off `python:3.7-slim`
- create `docker-compose.yml` to run Django app as a `web` service.
- enter `docker-compose up --build` to start your site.
- add `postgres 11` as a service
  - include a volume so that data can persist when container is shut down.
- Go to browsable api and confirm site properly restricts users based on their permissions.

## Stretch Goals

- Try different permission levels, including custom ones.
- Figure out how to directly access postgres running inside container. Hint: it will take research.

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

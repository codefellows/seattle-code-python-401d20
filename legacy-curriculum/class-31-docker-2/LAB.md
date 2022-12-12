# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 31: Docker 2

## Docker 2 - Compose Snakes

**This is a Solo  assignment**

<!-- short description of project -->
Create an `api` repo within a new `snakes-on-a-plane` organization. This repo will contain an API that we'll be building out for `Snakes on a Plane` project. Today's assignment will be to supply `Flight, Seat and Passenger` model data using `Docker Compose` to bundle a `PostgreSQL` and `Web` service.

## Specifications
<!-- Write a spefication for the features required in this lab assignment -->
- Create a `Dockerfile` for a custom Docker `service` named `web` to represent your Django api.
	- Use `python:3.7-slim` as base image
- Create a `docker-compose.yml` to manage your `web` service as well as launch a `db` service using PostgreSQL database.
	- Use `postgres:10.1-alpine` as base image.

### Setup
- Ensure `Docker` and `Docker Compose` are installed correctly
	- Refer to today's readings for instructions


### Features
- Create a `Flight` model
	- Add `name` attribute with a String type (e.g. PAL127) 
	- and `airborne` attribute with a Boolean type
- Create a `Seat` model
	- Add `name` attribute with type String (e.g. 12D)
	- Add a One to Many Relationship with `Flight`
	- Add a One to One Relationship with `Passenger`
- Add ability to manage models via `admin` panel

### Testing
- STRETCH: Research how to add Unit Tests using an alternate Postgres instance for testing only.


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

# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 32: Query Caching

## Title

**This is a Pair assignment**
<!-- short description of project -->
Today is all about performance improvements, mainly through the use of pagination and caching your queries. We'll use a variety of tooling for today's lab, but more notably you and your partner will be using a cache system called Redis to performance tweak your application.

## Specifications
<!-- Write a spefication for the features required in this lab assignment -->

### Setup
- Working in your `kickstarter_projects` repository, create a well named branch for today's work
- `npm i -g loadtest` to install the LoadTest tool on your machine

### Testing (do this before building your features)
- Run `loadtest -n 10 -k http://127.0.0.1:8000` testing against your application to benchmark
    - It should pretty much be painful to watch

### Features
- Implement the ability to paginate your responses for the list view of your kickstarter project queries
    - Your page should be able to easily navigate forward and backward between paginated query responses
    - Start off with somewhere around 20 records per page; you can adjust this as you see fit
- Implement caching in your backend, and configure your cache to store queries on the first request
    - Any subsequent request, for the configured parameter (time, updates, etc), will then reap the benefits!
- Using the developer tools (Network pane) as a visual guide, do some manual 'trial by fire' testing and tweaking of both your paginator values, and your caching values to see if your can see a noticeable difference in your response load times in the browser!

### Testing (running your benchmarks after building your features)
- Run `loadtest -n 100 -k http://127.0.0.1:8000` testing against your application to benchmark
    - It should much less painful now
- Try running with more requests `... -n 500 ...`

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

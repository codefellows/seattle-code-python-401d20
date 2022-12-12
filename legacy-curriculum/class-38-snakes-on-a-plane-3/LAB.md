# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 38: Snakes on a Plane III

## Moving around the Cabin, in Style

**This is a Solo  assignment**

<!-- short description of project -->
It's time to move the player around the cabin BUT only where allowed. In other words, aisles are great, seats beside player ok, etc. But NOT ok to walk through a wall, off the edge of the plane, and so on. Luckily, there's a API available who knows all the movement rules. Your job is just to process user's input and let API know where the player would like to go. Then the API will move the player if a legal move. Othewise player stays put!

And by the way, let's dress up for the occasion and apply some swanky style to our traveler and plane.

### Setup
- Create a `frontend-react` repo within your `snakes-on-a-plane` organization.
- Run `create-react-app` at top level of repo.
- Install `node-sass` library.

### Features
- Render initial state of plane and player by getting starting data from api
	- e.g. `https://the-api.com/api`
- **Note** Check demo and/or instructor for latest api url as it will intentionally change during development.
- Capture user's input - up, down, left or right.
- Pass player's current position and movement direction to api.
	- e.g. `https://the-api.com/api?direction=up&x=2&y=2`
- Render updated state of player and plane based off response from api.
- Make the plane and player gorgeous. Or at least better than the hot mess you got as a demo.

### Testing
- No testing requirements


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

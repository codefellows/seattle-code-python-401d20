# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 37: Intro to React

## React Odometer

**This is a Solo assignment**

## Specifications

- Create an Odometer web page using ReactJS.

### Setup

- Create github repo named `react-odometer`
- Create a new React project using [Creact React App](https://create-react-app.dev/docs/getting-started){:target="_blank"}
  - GOTCHA WARNING: instructions will use `npx` vs `npm` in different situations.
- Use `.gitignore` file and remember to add `node_modules` to it.
  - [gitignore.io](http://gitignore.io/){:target="_blank"} is handy resource. Enter `react` and see what gets generated.

### Features

- Display an odometer with 4 digits
  - Pad with zeroes as needed (e.g. 0045)
    - JavaScript has a method for this. Research as needed.
- Add buttons to increment/decrement the ones place, the tens, the hundeds place and the thousands place.
  - Roll over when odometer value exceeds 9999
  - Odometer should remain at zero when decrementing below zero.
- The root `App` component should contain `Odometer`,`Header` and `Footer` class based components.
  - `Header` component should receive a `greeting` value via props.
  - `Footer` component should receive a `trademark` value via props.
  - `Odometer` component should store numeric value in it's state.
    - Remember to update state in the React way.

### Testing

- No automated testing required

### Stretch Goals

- Convert class based components to functions.
- Add styling
- Store odometer's value in `App` component while keeping UI logic in `Odometer`.

### Useful Terminal Commands

- `npx create-react-app eggs`
- `npm start`

## Submission

1. Copy the link for your github pull request and paste it into the Canvas assignment for this day.
2. Leave any comments you may have about the assignment in the comments box. This includes any difficulties you may have had with the assignment.


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

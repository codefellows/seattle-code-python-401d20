# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 38: Getting to Know React

## List of Things

### This is a Solo assignment

## Specifications

- Create a ReactJS web application that displays a list of things, and allows creating new things.

### Setup

- Create github repo named `react-things`
- Create a new React project using [Creact React App](https://create-react-app.dev/docs/getting-started){:target="_blank"}
  - GOTCHA WARNING: instructions will use `npx` vs `npm` in different situations.
- Use `.gitignore` file and remember to add `node_modules` to it.
  - [gitignore.io](http://gitignore.io/){:target="_blank"} is handy resource. Enter `react` and see what gets generated.
- GOTCHA WARNING: This lab will primarily assume the use of class based components. Many tutorials will use a mix of class based and function based components. React community is still making up its mind on this one. Welcome to modern front end development.

### Features

- Create a web app with a top level `App` component
  - `App` component should...
    - have `thingList` data stored in its state.
    - render 3 nested components
      - `Header`
      - `ThingList`
      - `Footer`
  - `thingList` should be an array of plain old JavaScript objects (aka POJO) that represent a thing that has a name.
    - E.g. {name:'rake'}
  - `Header` component should...
    - receive a `things count` as a prop
    - display a heading
    - display the current count of things
  - `ThingList` component should...
    - receive a `list of things` as a prop
    - receive a function to call when a new `thing` is created.
    - Display an unordered list composed of `ThingItem` components
    - Display a form that allows creation of a `thing`
    - When user creates new `thing` the rest of application should update appropriately.
      - `Header` thing count should update
      - `ThingList` should add a new `ThingItem` to end of list
  - `ThingItem` component should...
    - receive a `name` as a prop
  - `Footer` component should...
    - Display some placeholder text (e.g. lorem ipsum)


### Testing

- No automated testing required

### Stretch Goals

- read in `things` data from an external JSON file


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

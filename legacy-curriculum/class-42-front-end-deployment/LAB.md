# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 42: Front End Deployment

## Full Stack Snacks

### This is a Solo assignment

## Specifications

- Create a React Single Page Application aka SPA
  - The app will route user to different "pages"
  - The app will load resources from provided [external api](http://167.172.203.221:8000){:target="_blank"}
    - Login credentials supplied in class
  - The app will be styled using Sass

### Setup

- Create github repo named `full-stack-snacks`
- Create a new React project using [Creact React App](https://create-react-app.dev/docs/getting-started){:target="_blank"}
  - **GOTCHA WARNING**: instructions will use `npx` vs `npm` in different situations.
- Use `.gitignore` file and remember to add `node_modules` to it.
  - [gitignore.io](http://gitignore.io/){:target="_blank"} is handy resource. Enter `react` and see what gets generated.
- **GOTCHA WARNING**: This lab will assume a mixture of functional and class based components. Be prepared to use both, and refactor to switch between them as needed.
- **GOTCHA WARNING**: You will likely get an error when first using Sass. Read the error, it will help you.

### Features

- The `Application` should...
  - have a top level `App` component
  - load initial list of resources using the appropriate lifecycle event to trigger load.
    - use a 3rd party http request library to handle external data flow.
  - maintain a list of `snacks` in the appropriate component's state.
  - **NOTE:** what counts as **appropriate** is for you to figure out.
- `App` component should...
  - Use `React Router` to manage site navigation
  - Render a `LoginForm` component when application launches at path "/"
  - Render list of `snacks` at "/" path once `snacks` user has logged in and resources have been loaded
- `SnackList` component should ...
  - render list of snacks
  - allow user to create a new snack via a `SnackForm` component
  - allow user to view details about a particular thing by navigating to snack detail route
  - be styled
- `SnackDetail` component should...
  - display info about a single snack
  - allow user to update information about the snack via a Form
    - Consider modifying `SnackForm` to handle both creation and updating
  - allow user to delete the snack
  - any modifications should update application's state appropriately
  - be styled
- You should be [Thinking in React](https://reactjs.org/docs/thinking-in-react.html){:target="_blank"} throughout this process.
  - If you spot places where a new component may be good then create one.
  - Functional vs. Class based? Try each and see what happens
  - Where's the best place for application state to be store? Re-Read: [React - Lifting State](https://reactjs.org/docs/lifting-state-up.html){:target="_blank"}

### Testing

- No automated testing required

### Stretch Goals

- Use your own API vs. provided snack api
  - If you go with own API then no need to create new repo, just extend previous React lab repo instead.
- Style to match the `browsable api` that Django REST Framework provides


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

# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 41: ReactJS Intro

## Introduction to Components and State Management

**This is a Pair assignment**
<!-- short description of project -->
Today you'll be working client-side with a JavaScript library called React (we'll get back to Python soon!).

## Specifications
<!-- Write a spefication for the features required in this lab assignment -->

### Setup
- Create a new repository called `reddit_search`, and add your partner as a collaborator
- In your `reddit_search` repository create a well named branch for today's work

### Features
- Create the following components and structure them according to the following diagram
```
App
  SearchForm
  SearchResultList
```
###### App Component
- should contain all of the **application state**
- should contain methods for modifying the application state
- the state should have a topics array for holding the results of the search

###### SearchForm Component
- should contain a text input for the user to supply a Reddit board to look up
- should contain a number input for the user to limit the number of results to return
    - the number must be more than 0 and less than 100
    - `onSubmit` the form should make a request to Reddit
    - it should make a get request to `https://www.reddit.com/r/${this.state.searchFormBoard}.json?limit=${this.state.searchFormLimit}`
        - _Note: `www` is **required** for the api call to complete successfully._
    - on success it should pass the results to the application state
    - on failure it should add a class to the form called error and turn the form's inputs borders red

###### SearchResultList Component
- Should inherit all search results through props
- This component does not need to have its own state
- If there are topics in the application state it should display an unordered list
- Each list item in the unordered list should contain the following
    - an anchor tag with a href to the topic.url
        - inside the anchor a heading tag with the topic.title
        - inside the anchor a p tag with the number of topic.ups

### Testing
- No testing requirements for this lab

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

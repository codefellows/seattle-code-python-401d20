# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 12: Regressions

## Exploratory Analysis with Linear Regressions

**This is a Solo assignment**
<!-- short description of project -->
Today you'll perform exploratory analysis by using Linear Regressions on the Kaggle data set of your choice.

## Specifications
<!-- Write a specification for the features required in this lab assignment -->

### Setup
- In your `data_analysis` repository, create a well named branch for today's work.
- Start a new Jupyter notebook called `regressions`, and add a markdown header or two with a title and any description information you'd prefer to include.

### Features
- Select a [Kaggle data set](https://www.kaggle.com/datasets?search=linear+regression){:target="_blank"} that is suitable for Linear Regression
    - **Note** make sure the data set has csv file/s to download.
- Load the data you receive into a Pandas `DataFrame`
- Show the first five rows of the data set
- Show the `description` and the `info` of the data set
- Ensure that any `date` columns have been cast into a `datetime` object in your DataFrame
- Using a regression model, split your data into train and test data
- Fit your training split to the regression model
- Draw at least three conclusions from your regression model


### Stretch Goals
- Use a polynomial regression
- Stream a `big query` instead of loading a csv file

### Testing
- No test requirements for today's lab

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


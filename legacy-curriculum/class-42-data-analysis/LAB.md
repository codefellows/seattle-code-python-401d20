# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 16: Data Analysis

## Introduction to Data Science

**This is a Solo assignment**
<!-- short description of project -->
Today we're taking a detour into Data Science to learn a bit more about the field and tools used before moving back to our stock portfolio and implementing more features!

The best way to hone your data analysis skills is consistent, deliberate practice.
One of the best places to acquire data for analysis is [Kaggle](https://www.kaggle.com/), so practice your abilities with some [Kaggle](https://www.kaggle.com/datasets) data sets.

Sign up for a Kaggle account (if you don't already have one).

## Specifications
<!-- Write a spefication for the features required in this lab assignment -->

### Setup
- Create a new repository for today's lab assignment called `data_analysis`
- In your `data_analysis` repository, create a well named branch for today's work

### Features
- Find and download the following data sets:
    + [Video Game Sales](https://www.kaggle.com/gregorut/videogamesales){:target="_blank"} - Sales data from more than 16,500 games
    + [Cycle Share Data set](https://www.kaggle.com/pronto/cycle-share-dataset){:target="_blank"} - Bicycle Trip Data from Seattle's Cycle Share System
- Start two Jupyter Notebooks called `vg-stats` and `bike-stats`
- Add a markdown cell at the top of each notebook with the title of this assignment, an appropriate name for the data set, as well as your name and the date
- Load up each of these data sets into a Pandas DataFrame within each respective file.
    - _NOTE: There's an issue with one of the CSV files. You will need to find a way to handle that error... Google it, and work around it!_

- In the `vg-stats` notebook answer the following questions/do the following tasks. Note that the numbers quoted for sales are in the millions, and apply only for those games with over 10,000 sales.:
    1. Which company is the most common video game publisher?
    1. What’s the most common platform?
    1. What about the most common genre?
    1. What are the top 20 highest grossing games?
    1. For North American video game sales, what’s the median?
        - Provide a secondary output showing 'about' ten games surrounding the median sales output
    1. For the top-selling game of all time, how many standard deviations above/below the mean are its sales for North America?
    1. The Nintendo Wii seems to have outdone itself with games. How does its average number of sales compare with all of the other platforms?
    1. Come up with 3 more questions that can be answered with this data set.

- In the `bike-stats` notebook, answer the following questions/do the following tasks:
    1. What is the average trip duration for a borrowed bicycle?
    1. What's the most common age of a bicycle-sharer?
    1. Given all the weather data here, find the average precipitation per month, and the median precipitation.
    1. What’s the average number of bikes at a given bike station?
    1. When a bike station is modified, is it more likely that it’ll lose bikes or gain bikes? How do you know?
    1. Come up with 3 more questions that can be answered with this data set.

- When you're done answering all of the questions for each data set, clean up your notebooks leaving only cells that contain relevant data and calculations. Then restart and run your notebook so that the cell numbering is sequential from top to bottom

- **Have fun with the data!! Play around a bit, and see if there's anything else you can/want to do with the info available!**

### Testing
- **No test requirements for today**

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

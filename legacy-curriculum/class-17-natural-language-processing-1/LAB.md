# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 17: Natural Language Processing 1

## Find a data set and prepare it to create a model for Sentiment Classification

**This is a Solo assignment** Today you’ll use data set on Kaggle or elsewhere and use Tensorflow, Keras, Pandas, Numpy and Jupyter Labs to prepare it for training a Sentiment Classifier

## Setup
- Build on the concepts you have worked with the past few labs
- Create a sentiment-classifier repository on Github.
- Based on the size of the data set, determine if you should store it in your repository or import using the built ins
    - Remember that github’s limit is 100mb!
    - If you need to store data locally, and that is necessary for a user to download the set locally in order to run your classifier, please note as much in your readme.


## Features

- Identify a dataset suitable for sentiment classification - reviews with an even distribution are a good option.
    - There are pre-prepared data-sets available that have sentiments included, are split into a training set and a testing set, and have a perfectly even distribution. For this lab, please find and prepare your own even if it is not perfect.
- Access it either externally or from within your repository as appropriate.
- Based on the shape of your data, determine an appropriate spread for your positive[2], neutral[1], and negative[0] sentiments and add a column associating them with the appropriate reviews.
- Identify and normalize any issues in your dataset.
- Do the preprocessing work utilizing Keras and Tensorflow taking a One-Hot Vector approach.
- In your readme, discuss the data set you choose, the distribution of your sentiments, your training/testing split, and the preprocessing methods you choose.


## Stretch Goals
- Utilize the tools in Pandas and Numpy to visualize your data before classification.
- Find a complementary data set to train your model on and prepare it as well.


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

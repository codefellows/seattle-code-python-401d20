# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 18: Natural Language Processing 2

## Training a Sentiment Classifier

Using your prepared data, create a model, train your classifier, and save the trained model

**This is a Solo assignment** You will expand on your tokenized and one-hot sequenced data from yesterday by creating a model, training it with your one-hot matrix, predict and validate your model, and save it out to a JSON file for future use! 

## Setup
- Build on the concepts you have worked with the past few labs.
- Work in your sentiment-classifier repository on Github.


## Features

- Finish all steps from yesterday's lab.
- Utilizing a One-Hot Vector approach, create a Model that utilizes a Neural Network and has:
    - input layer
    - output layer
    - at least 2 Dropout/Dense layer pairs
    - Play with your activations to achieve the accuracy you would like, but discuss which ones you selected in your readme.
 - Train your Model!
    - Remember to use your gpu, if it will handle the load.
- Test your model with the validation set you put aside yesterday.
- Save your trained Model as Json to be used again.



## Stretch Goals
- Create a CLI that utilizes your trained model as a sentiment classifier
    - Hint: You might want to do this in a plain .py file
    
- Streamline your Sentiment Classifier with an Embedding layer


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

# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 19: Cryptography

## The Ceasar Cipher

Today we'll be tackling a crytographic classic - the Ceasar Cipher.

Your job will be to devise a method to encrypt a message that can then be decrypted when supplied with the corresponding key.

**This is a Solo assignment**

## Setup
- Create a new repository for today's lab assignment called `ceasar-cipher`
- In your `cipher-cipher` repository, create a well named branch for today's work


## Features

- Create an `encrypt` function that takes in a plain text phrase and a numeric key.
- Create a  `decrypt` method that takes in encrypted text and numeric key which will restore the encrypted text back to its original form **as long as correct key is supplied.**
- Break the code so that an encrypted message can be transformed into its original state **without** access to the key.
- Devise a method for the computer to determine if code was broken with minimal human guidance.
    - **NOTE:** In order to accomplish this task you'll need access to a `corpus` of English words.
    - A search on something like `python list of english words` should get you going.



## Stretch Goals
- Research the Vigenère cipher
- Find some examples of ROT13 encrypted punchlines, spoilers, etc.
- Break the code for a message written in language other than English.


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

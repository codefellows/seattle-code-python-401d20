# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 05: Linked Lists

## Implement a Singly Linked List

**This is a Solo assignment**
<!-- short description of project -->
Today you will be diving into the world of abstract data structures with an introduction to writing a Linked List in Python.

## Specifications
<!-- Write a spefication for the features required in this lab assignment -->

### Setup
- Create a new branch in your `data-structures-and-algorithms` repository called `linked-list`
- In your `data-structures-and-algorithms/data_structures/` director, create a `linked_list/` directory 
- In your `linked_list/` directory, create three files  
    1. `node.py`
    2. `linked_list.py`
    3. `test_linked_list.py`

### Features
- Create a Class for a `Node` which is aware of the value as `val` and next as `_next`
    - Ensure that you have a `__str__` method defined to return the value of the node when printed
- Create a Class for a `LinkedList` which creates an empty Linked List when instantiated.
    - This class should be aware of a default `None` value assigned to `head` when the list is created.
    - This class should be aware of the `len` of the list, which represents the count of Nodes in the list at any time
    - This class should have the ability to accept an iterable as an argument when instantiated, such as `[1, 2, 3, 4]`, and creates a new Node in the list for each value in the iterable.
    - Define any further magic methods such as `len` and `str` to support user functionality and informative responses.
    - Define a method called `insert` which takes any value as an argument and adds that value to the `head` of the list with an O(1) Time performance.
    - Define a method called `includes` which takes any value as an argument and returns `True` or `False` depending on whether that value exists as a Node value within the list.
- At no time should an exception or stack trace be show to the end user. Catch and handle any such exceptions and return a printed value or operation which cleanly represents the state and either Stops execution cleanly or provides the user with clear direction and output.

### Testing
- Every bit of functionality that you add should be tested.
- As a general rule at this time, you should have a test for valid, invalid, and edge case variants for every function that you define. There are exceptions. The exceptions are not the rule.


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

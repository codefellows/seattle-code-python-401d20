# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 10: Stacks & Queues

## Title

**This is a Solo assignment**
<!-- short description of project -->
Today you will be implementing two new data structures; Stacks and Queues.

## Specifications
<!-- Write a spefication for the features required in this lab assignment -->

### Setup
- Create a new branch in your `data-structures-and-algorithms` repository called `stack-queue`
- Create two separate directories: `stack` and `queue` respectively
- Each directory should have it's own `README.md` and any other necessary configuration that's specific to this module
- Create two files **in each** called `node.py` and `stack.py` / `queue.py` respectively

### Features
- In `node.py`:
    - Create a Class for a `Node` which is aware of the value as `val` and next as `_next`
        - Ensure that you have a `__repr__` method defined to return the value of the node when printed

- In `stack.py`:
    - Create a Class for a `Stack` which creates an empty Stack when instantiated
        - This class should be aware of a default `None` value assigned to `top` when the isntance is created
        - This class should be aware of the `len` of the stack, which represents the count of Nodes in the stack at any time
        - This class should have the ability to accept an iterable as an argument when instantiated, such as `[1, 2, 3, 4]`, and creates a new Node in the stack for each value in the iterable
        - Define any further magic methods such as `len` and `str` to support user functionality and informative responses
        - Define a method called `push` which takes any value as an argument and adds that value to the `top` of the stack with an O(1) Time performance
        - Define a method called `pop` which takes no arguments and removes / returns the Node at the top of the stack
        - Define a method called `peek` which takes no arguments and returns the Node at the top of the stack

- At no time should an exception or stack trace be show to the end user. Catch and handle any such exceptions and return a printed value or operation which cleanly represents the state and either Stops execution cleanly or provides the user with clear direction and output.
- Every bit of functionality that you have should be tested and documented. As a general standard, you should have three tests for each method or body of functionality in your API.

- In `queue.py`:
    - Create a Class for a `Queue` which creates an empty Queue when instantiated
        - This class should be aware of a default `None` value assigned to `front` when the isntance is created
        - This class should be aware of a default `None` value assigned to `back` when the isntance is created
        - This class should be aware of the `len` of the queue, which represents the count of Nodes in the queue at any time
        - This class should have the ability to accept an iterable as an argument when instantiated, such as `[1, 2, 3, 4]`, and creates a new Node in the queue for each value in the iterable
        - Define any further magic methods such as `len` and `str` to support user functionality and informative responses
        - Define a method called `enqueue` which takes any value as an argument and adds that value to the `back` of the queue with an O(1) Time performance
        - Define a method called `dequeue` which takes no arguments and removes / returns the Node at the `front` of the queue

- At no time should an exception or stack trace be show to the end user. Catch and handle any such exceptions and return a printed value or operation which cleanly represents the state and either Stops execution cleanly or provides the user with clear direction and output.

### Testing
- You are required to have 80% or better test coverage for each data structure.
- As a general standard, you should have at least three tests for each method or body of functionality that you create in your API.
    - For example, you defined `queue.enqueue(val)`
    - Write a test which validates that a valid `val` is added to the queue when `.enqueue` is called
    - Write a test which validates that an exception is thrown if an invalid or None-type value is passed as an argument to `.enqueue`
    - Write a test which validates that the `len` attribute of your class increments when a new Node is added to the queue


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

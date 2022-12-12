# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 15: Binary Trees

## Implement a Binary Tree

**This is a Solo assignment**
<!-- short description of project -->
Today you will be learning and implementing a new abstract data structure: Binary Trees.

## Specifications
<!-- Write a spefication for the features required in this lab assignment -->

### Setup
- Create a new branch in your `data-structures-and-algorithms` repository called `bst`.
- Create a new directory called `binary_search_tree/`, with all of your standard module configuration for each directory
    - `__init__.py`, `README.md`, etc.

### Features
- In `bst.py`:
    - Create a Class for a `Node` which is aware of the value as `val` and left and right children as `left` and `right` respectively
        - Ensure that you have a `__repr__` and `__str__` method defined to return appropriate representations of the node
    - Create a Class for a `BST`, which is aware of the root of the tree as `root`
        - Ensure that you have a `__repr__` and `__str__` method defined to return appropriate representations of the tree
        - This class should accept an iterable as an argument when initialized, such as `[20, 18, 12, 19, 11, 14, 40, 31, 22, 33]`, which creates a tree from that argument
        - This class should be aware of depth-first traversal methods for `in_order`, `pre_order`, and `post_order` traversals
        - This class should have the ability to `insert` a new node into the tree. Your insertion should follow an O(log n) search solution to find the correct place for inserting the new node.

### Testing
- You are required to maintain an 80% or better coverage benchmark in your test suite.
- Start by focusing on three different tests/assertions for each method that you create, including the initial class definition.
    - One assertion should validate successful functionality
    - One assertion should validate failure functionality
    - One assertion should validate an edge case

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

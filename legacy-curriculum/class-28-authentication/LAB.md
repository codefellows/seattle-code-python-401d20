# ![cf](http://i.imgur.com/7v5ASc8.png) Class 28: Authentication

## HMAC Registration in Django

**This is a Solo assignment**
<!-- short description of project -->
Today's lab will focus on implementing a single package to handle HMAC Registration in your Django application. We'll explore what the package provides for you by default, as well as the further configurations you can implement to adapt the package to suit your application's requirements.

## Specifications
<!-- Write a spefication for the features required in this lab assignment -->

### Setup
- Working in your `django_lender` repository, create a well named branch for today's work

### Features
- If you've not already created a navigation menu in your `base.html` template, do that today
- Using the provided [`templates/`](./assets/templates){:target="_blank"} directory, copy that directory and all of it's contents to the same `templates/` directory in your root application
    - Following the documentation, paying close attention to available context data in each view, configure each file to suit the needs of your application
    - You will also need a directory for your `base.html` and `home.html`
- Because the registration service involves sending emails, you will have to configure [email services for Django](https://docs.djangoproject.com/en/2.0/topics/email/){:target="_blank"}. However, you don’t want to send real emails when developing, so make sure that you configure the [Django console email backend](https://docs.djangoproject.com/en/2.0/topics/email/#configuring-email-for-development){:target="_blank"}. Then any emails you send while working will simply print to the console where Django is running


### Testing
- Continue to develop your unit test coverage within the application; focusing on writing at least three assertions for each model or controller that you define
- To test registration you will want to be aware of how [Django’s email services work in a test environment](https://docs.djangoproject.com/en/2.0/topics/testing/tools/#email-services){:target="_blank"}


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

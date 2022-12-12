# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 37: Django REST Framework III

## Permissions & Authentication

**This is a Solo  assignment**

<!-- short description of project -->
Protect your API with permissions and authentication. 

## Specifications
<!-- Write a spefication for the features required in this lab assignment -->
- Create a DRF API with a simple model (e.g. `Thing`) that has a `one-to-many` relationship with Django's `User` model.
- Add [permissions](https://www.django-rest-framework.org/api-guide/permissions/){:target="_blank"} to your API
	- Only authenticated user's should be allowed access to API
	- Editing or deleting a `Thing` should be restricted to the thing's creator.
- Add ability to access API with a JWT Token
	- Use [simple-jwt](https://github.com/davesque/django-rest-framework-simplejwt){:target="_blank"} library to handle authentication.
- use `httpie` to request and use a token
	- Request a token 
		- `http POST :8000/api/token/ username=jb password=pass`
	- Use a token to access proteced route
		- `http :8000/api/things/ 'Authorization: Bearer YOUR_ACCESS_TOKEN'`
	- Verify protected route is blocked for unauthenticated user
		- `http :8000/api/things/` with no token
- WARNING: httpie really needs everything just so. Double check example httpie calls above as needed.



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

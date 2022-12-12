# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 34: API Deployment

## Deploy your API

**This is a Solo assignment**
You will be deploying your application to a remote web host. Along the way you'll update yesterday's project to be web ready.

These instructions will presume you are deploying to Digital Ocean but you should research other options and choose for yourself.

## Specifications

- Make your site "web ready" and deploy it.

### Setup

- Refer to today's demo in course repo for Environment Variables and CORS additions.
- Sign up for Digital Ocean account
  - [Digital Ocean](https://www.digitalocean.com/?refcode=d8f211a4b4c2){:target="_blank"}
  - Check with instructor if payment is an issue.
- Generate a [Personal Access Token](https://www.digitalocean.com/docs/api/){:target="_blank"}
  - Make sure to save your token, you'll need it soon.

### Features

- Modify your application to store SECRET_KEY, ALLOWED_HOSTS, DEBUG and DATABASE information in `.env` file.
- Add CORS capabilities to your app and whitelist allowed origins.
- All the code changes will be in `settings.py` so check the demo code for CORS and Env related lines.
- Create account with Digital Ocean (or other host of your choosing.)
- Deploy application to Digital Ocean

### Testing

- Manually confirm API using Postman.
  - Remember to use deployed url for postman requests.

### Useful Terminal Commands

- `docker-compose up --build`
- `docker-compose down`
- `docker-compose run web ./manage.py migrate`
- `docker-compose run web ./manage.py collectstatic`

## Submission

1. Copy the link for your deployed project and paste it into the Canvas assignment for this day.
2. Leave any comments you may have about the assignment in the comments box. This includes any difficulties you may have had with the assignment.


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

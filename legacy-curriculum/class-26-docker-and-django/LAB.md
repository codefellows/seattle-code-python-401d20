# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 26: Docker & Django

## Set up a Docker container & Run your first Django Application!

**This is a Solo assignment**
<!-- short description of project -->
Today you'll be working in a slightly new development environment. We'll be introducing the concept of Docker and working within containers as a part of your developer workflow.

In addition to Docker, you will also be building your first Django web application.

## Specifications
<!-- Write a spefication for the features required in this lab assignment -->

### Setup
- Ensure that you've installed [Docker](https://www.docker.com/community-edition#/download){:target="_blank"} on your local machine
- Create a new project & repository called `django_lender`
- Add all of you standard config files
- Recreate the `Dockerfile` and `docker-compose.yml` that we configured in lecture, update each file if needed for this new project
- Recreate `entrypoint.sh` as was done in lecture.
    - change file properties with `chmod +x` if needed
- Install `django` and `psycopg2-binary` as a dependency for your project
- Run `pipenv run pip freeze > requirements.txt` to propogate dependencies to enviroments that don't use pipenv
- Create your Django project and configure the settings to utilize the necessary environment variables
    ```dotenv
    # Docker-specific
    DB_NAME=postgres
    
    # Docker-specific  
    DB_USER=postgres
    
    # Docker-specific
    DB_HOST=db 
    
    # This comes from Django when you start the project 
    SECRET_KEY=k_8j56=hm0m^sfxok)r_-hw6x2&dx)4$@o#x62kk4g3#-6@$b_ 
    
    # Turns on development mode and activates the built in debugging tools 
    DEBUG=True  
    
    # Tells Django while domains can contact the server (whitelist)
    ALLOWED_HOSTS=localhost 127.0.0.1 0.0.0.0  
    ```
- Update the `DATABASE` configuration in `settings.py` to address a PostgreSQL database using the following config:
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('DB_NAME'),
            'USER': os.environ.get('DB_USER'),
            'PASSWORD': os.environ.get('DB_PASSWORD'),
            'HOST': os.environ.get('DB_HOST'),
            'PORT': 5432,
            'TEST': {
                'NAME': 'lender_test'
            }
        }
    }
    ```
- Once your config is complete, you can run `docker-compose up --build` to start up your application, and open `127.0.0.1:8000` in the browser to validate that your application is running and functional
    - NOTE: if you get errors running `docker-compose up --build` from terminal then execute bash inside the container as described below and run from there.
- Other helpful Docker commands:
    - `docker exec -it <app_container_name_or_id> bash`  Starts a bash shell inside the Docker container running your web app
    - `docker exec -it <db_container_name_or_id> psql -U postgres`  Starts a postgres shell inside the Docker container running your Postgres database 
    - `docker-compose down --remove-orphans -v`  Disables your active Docker containers, removing volumes and eliminating orphaned containers
    - `docker system prune`  Cleans up and deletes containers, volumes and images that are currently unused or disabled (Run this regularly to help keep your system clean as you're learning Docker)

### Features
- Run your application and ensure that all things are as they should be!

### Testing
- No test requirements for today's lab. 

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

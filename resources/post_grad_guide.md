# Python Post-Grad Road Map

So it’s after week 10 and the Code Fellows 401: Python class is now over. You’ve turned off your Django Imager instances, slept for a few days straight or whatever your body called for, and now you’re up and ready to do something more. The frenzied pace that we’ve worked at for 2.5 months is gone, and the only pressure to perform is the pressure of unemployment. It’s terrifying, but it’s not as pressing when there isn’t a concrete deadline to hit.

The main danger of this point in time, between the end of class and the start of your careers, is the temptation to ease off on sharpening your skills. It’s easier to make excuses now; easier to let other priorities get in the way.

However, a muscle unused becomes atrophied and skillsets are no different. Consistent practice keeps you sharp and is good to make a habit of, but consistent practice is simply maintenance on the skills that you already have. True growth as a developer, and in general, comes from making the habit of adding new things to your repertoire.

What new tools should you add to your skillset? How much time should you allocate to practice vs exploration? When do you find time to stay on top of the job application process?

This Road Map will begin to answer those questions, but is not a hard-and-fast plan for everyone. Read it through and do what works best for you, modifying the contents with what fits your schedule, your finances, and your interests.

## Tips on Structuring Time and Accountability

The main thing missing from post-graduate, pre-employment life is structure and accountability. There’s nowhere to be at 9am, and nothing to get done by 5pm. There are no partners to keep up or communicate with unless you forge those relationships yourself.

So, create your own time schedule and find someone to keep you accountable. Here’s a guideline for separating your concerns throughout your day:

**Any Given Weekday...**

- 2 hours: interview prep
- 3 hours: job search
- 3 hours: personal project work
- Other Unclaimed Time: more personal project work
- Evening Hours: attend meetups

### Interview Prep (2 hours)

Interview preparation considers only the actual interview process; what happens when you get a call or an on-site interview. There are two main things to prepare for here: coding questions and behavioral questions.

For coding questions, questions are often asked about data structures and sorting algorithms. So, review the data structures and algorithms that we’ve done in this class. Here’s a listing of them:

1. Singly-Linked List
1. Stack
1. Queue
1. Binary Search Tree
1. K-ary Tree
1. Graph
1. Hash Table
1. Insertion Sort
1. Merge Sort
1. Quick Sort
1. Radix Sort

How to review them? **Write a blog post about each one!** In that blog post, write out the code for the Python implementation of these data structures and know them inside and out. If you decide to add the ability for the structure to be initialized with an iterable, say why. In fact, look up the specification for each structure on Wikipedia, and then write about every departure that you take from that specification. Used a generator? Why? Recursion instead of iteration? What motivated that?

Talk about time complexity. Talk about space complexity. Talk about the trade-offs between different implementations of the same data structure or algorithmic concept. Most importantly, why should a developer care about these differences? Digging this deeply into any concept will definitely solidify the functionality and purpose of that concept in your mind.

Being solid on the theory behind different abstract data structures is great, but they’re best used in practice. Hell, coding in general is best practiced and not read, so practice up using [Code Wars](https://codewars.com){:target="_blank"}, [Interview Cake](https://www.interviewcake.com/){:target="_blank"}, [LeetCode](https://leetcode.com){:target="_blank"} and [HackerRank](https://hackerrank.com){:target="_blank"}. There are tons of other sites like these too, so if you tire of any one of them, make Google your friend. There’s also the Cracking the Coding Interview book, which supplies a ton of questions that are often used on whiteboard interviews.

Finally, practice DOING those whiteboard questions on whiteboards! If you have one at home, practice handling the questions there. If you don’t, come in to the Code Fellows and use ours. Our campus is always open to alumni (though please respect the classes currently in session).

For **behavioral interview questions** practice will always make the master. These questions will ask less about what code you can write and instead seek to find out how you behave in a working environment. Examples are:

- Give me an example of a time when you set a goal and were able to meet it.
- Tell me about a time when you had too many things to do and you were required to prioritize your tasks
- Tell me about a time where you had to make a difficult decision
- Give me an example of a time when you failed to accomplish something that you worked hard on
- Find someone to bounce these questions off of. Trade roles as interviewer and interviewee. Polish your responses not so that they sound “perfect”, but so that you’re doing more than just answering the question. You’re showing with every response why you’re a good fit as a part of a larger team or organization. Show that you can keep goals beyond you in mind when you make decisions.

There are tons of resources for practicing answering these types of questions. A simple google search for “behavioral interview questions” returns these as the first few results:

- [Sample Behavioral Job Interview Questions](https://www.livecareer.com/quintessential/sample-behavioral){:target="_blank"}
- [Most Common Behavoral Interview Questions](https://www.themuse.com/advice/30-behavioral-interview-questions-you-should-be-ready-to-answer){:target="_blank"}
- [Behavioral Interview Questions](https://biginterview.com/blog/behavioral-interview-questions){:target="_blank"}
- [30 Behavioral Interview Questions you should be Ready to Answer](http://college.usatoday.com/2015/04/22/30-behavioral-interview-questions-you-should-be-ready-to-answer/){:target="_blank"}
- [Behavioral Interview Questions and Answers 101](http://theinterviewguys.com/behavioral-interview-questions-and-answers-101/){:target="_blank"}

### Job Search (3 hours)

This phase of your day consists of more than just archiving a set of links. The job search is a tedious part of your career, and will never be a pleasant experience. However, if you break this up into more digestible components, you can at least ease the pain a bit.

To start your job search, harvest links to companies that interest you. Then, before you even start tailoring your resume or writing the first character of your cover letter, **research the company**. Don’t just throw everything against the wall to see what sticks, look into what actually may interest you. What do they do? What clientele do they serve? What roles do developers serve at that organization? Is there anyone on LinkedIn from that organization that I can take out to coffee and get more information from? It’s far more obvious to spot a candidate with actual interest in the position vs a candidate just trying to pay rent.

**AFTER** you research, then as a part of the job search process send out applications, write or revise your resume, and write/revise your cover letters.

##### Common Divisions in Python Careers

It helps to have a heading when applying for jobs, and there’s so many titles thrown around that it can be tough to tell what to look for. Here are some common titles in the world of Python, along with some _VERY_ general summaries:

- **Software Developer/Development Engineer:** Someone that writes software and features for existing apps, or builds apps from scratch. Often will use Django, Flask, Pyramid, or other web framework. Every once in a while will be tasked with writing scripts to do things solely on the computer side.
- **Software Development Engineer in Testing (SDET):** A developer that’s fluent in the frameworks of the day, but doesn’t write code that increases the feature set. They only test code, both with automated test suites and with behavioral tests (click this thing and see if it breaks).
- **Backend Web Developer:** Often will still be tasked with writing Django code, but nothing that is displayed directly to the front-end. They will often build out the code that powers a site’s API. They may not even work on a web app at all, sticking only to writing utility scripts on the server-side.
- **Full-Stack Web Developer:** A web developer that knows how to serve the site, and also how to tailor the user experience on the front-end. You’re not going to fit this job well without a solid handle on HTML, CSS, and JS in addition to Python/Django. In this role you’ll have to have some type of eye for design, and be able to build a useful and intuitive user interface as well as the back-end that serves that interface.
- **Developer Operations (DevOps) Engineer:** An app-deployment specialist. The code that they write is used to package and serve the site instead of add features to it. This will require a ton of work with tools from the following stack (note: not a complete list): AWS, Google App Engine, Microsoft Azure, Ansible, Fabric, OpenStack, Docker, Jenkins.
- **Data Scientist/Machine Learning Engineer:** Data Scientists specialize in the data analysis and presentation process. They’re adept at drawing insights from a given data set, and will often work closely with the database they’re pulling data from. If you have a knack for numbers and condensing your insights into easily-digestible visualizations, this is a role you may want to pursue. It’s closely tied with the role of a Machine Learning Engineer, as both are concerned with generalizable models that are based on the data and can be used for prediction and explanation. The difference is that the Machine Learning Engineer is less concerned with problems like regression and descriptive statistics, focusing more on building the predictive models themselves and tuning them well to add business value. Oftentimes though, the titles are interchangeable and each will often cross over to the other.

### Personal Projects (3 hours)

At the end of the day, no matter how much experience you may have as a developer, all that anyone will care about is that they can tell you to do a thing, and you can actually do that thing. However, because you lack experience as a Python developer, you have to make up for the buffer you would have had from a career with a body of work that gives substance to your claims of proficiency. Out of all three of these sections, this is the most important. **Building personal projects shows that you can do the thing.**

Aim to produce at least one small serious project every 2-3 weeks. If you decide to make a larger, more involved project, aim for producing every 4-6 weeks. Whatever your other obligations may be, you should set a restriction on yourself to publish **no fewer than one project per month**, unless you absolutely need that extra time.

Every project that you build needs to show that you have some understanding of best practices. What this means is:

- **full documentation** of every script, function, class, and method.
- code adhering religiously to [PEP8 standards](https://www.python.org/dev/peps/pep-0008/){:target="_blank"}.
- at least one test for every function, class, or method **that you write**. If you extend an existing class (like Django’s `DetailView`), test your class extension.
- **THOROUGH** tests, meaning anticipating the ways in which your code should succeed, as well as how it should fail
- a verbose `README.md` file that details exactly how a completely new developer can get up and running with your codebase. Do they need a virtual environment? Do they need Python 2, Python 3, or can they use either? How can they run tests? If you made a web application, what are the routes? What are the models? If someone wants to contribute to your project, what’s the workflow that they should adhere to? What are the standards for your code base? Do they need to `pip install` your requirements file, or can they simply `pip install -e .` from the directory containing `setup.py`?
- at least 80% test coverage, with [Travis](https://codefellows.github.io/sea-python-401d7/readings/travis-ci.org){:target="_blank"} and [Coveralls](https://codefellows.github.io/sea-python-401d7/readings/coveralls.io){:target="_blank"} badges that show how dope of a developer you are.
- an up-to-date `requirements.pip` or `requirements.txt` file to go along with your codebase.
- no stale `git` branches for your repository (unless they’re feature branches or works in progress)

So, what projects should you work on? The first thing that you need to do is have a web presence. This means that you should have your own website (preferably with a custom email). Something like `http://www.myname.com`. Or, if you have a brand that you want to push forward or a name that applies to you, use that. Be clever and engaging with yours.

##### The Portfolio Site

Your portfolio site should tell a newcomer who you are, what your education is, and where your interests lie. For that last point, reinforce what your interests are through consistent blog posts. Figure out a schedule that works for you. Every day is likely entirely too frequent for most humans. How about every week? Or every other week? The interval isn’t what matters so much as the consistency, so choose a pace that you can be consistent with.

Aside from blog posts, there should be obvious links to your past and ongoing projects. See if you can even integrate an AJAX call to your github page that shows what repos you’ve worked on last!

Finally make it look good, because all the skill in the world won’t get you in the door if you present poorly. This means some decent HTML, CSS, and even JavaScript. If you’re angling for a job that doesn’t deal too heavily with the front-end then feel free to use [Zurb Foundation](http://foundation.zurb.com/){:target="_blank"}, [Bootstrap](https://startbootstrap.com/){:target="_blank"}, or any other pre-built themes. If you’re looking more toward front-end development, or true full-stack development, then at least for your portfolio site write your own HTML/CSS/JS.

### After the Portfolio Site

So you’ve built your portfolio site and need ideas for what to do next. Common from-the-ground-up projects are things like:

- To-Do Lists
- Facebook/Twitter/Tumblr/Instagram clones
- Person-to-person sales sites
- Chat/Facebook Messenger/Twitter bots
- Recipe sites
- Weather apps
- Friend finders
- Inventory trackers
- User-editable data repositories
- Restaurant/Bar/Hospital/Apartment finders

If you’re not really into building things from scratch, feel free to contribute to any one of thousands of active or stale open-source projects. **Open source projects** are a great way to get your name out there, and a great impetus for **presenting lightning talks** at meetups both local and distant. Make a fork, work on some code, write some test, update or add to documentation, and send a pull-request back.

GitHub keeps track of trending projects for every language. Here’s the listing of Python projects on Github [trending in open source](https://github.com/trending/python){:target="_blank"}. Here’s a few other resources you can look into:

- [Awesome First PR Opportunities](https://github.com/MunGell/awesome-for-beginners#python){:target="_blank"}
- [OpenHatch](https://openhatch.org/){:target="_blank"}
- [Python Projects](https://wiki.python.org/moin/PythonProjects){:target="_blank"}

### Meetups

By now you should already be familiar with the [PuPPy meetup group](https://codefellows.github.io/sea-python-401d7/readings/meetup.com/PSPPython/){:target="_blank"}. However, there are dozens of other meetup groups for Python and related subfields.

Have an interest in Natural Language Processing? Check out any one of [these Seattle NLP meetups](https://www.meetup.com/topics/natural-language-processing/us/wa/seattle/){:target="_blank"}.

Interested in data science more broadly? Attend an event by the [Seattle Data Geeks](https://www.meetup.com/seattle-data-geeks/){:target="_blank"} or [Seattle Data Science](https://www.meetup.com/Seattle-Data-Science/){:target="_blank"}.

Do you just want more Python? For that hunger, there’s [PyLadies](https://www.meetup.com/Seattle-PyLadies/){:target="_blank"}, and yes they do allow men to hang out too.

Half the battle is being known, so showing your face early and often at various meetups will help you along that line. You never know, you may end up sitting beside your next coworker!

And don’t simply go to meetups either, **speak at them!** There’s no reason why you can’t give a lightning talk about every personal project you complete outside of your portfolio site. In fact make that a goal: whenever you complete a project, build an 8-minute lightning talk about it and present at PuPPy.

### Accountability

These things are all great in theory, but if no one holds our feet to the fire then we find it much easier to make excuses and fall out of our good habits. Find someone to hold you accountable. Oftentimes this is easiest with friends or loved ones, however they aren’t always available. Luckily for you, you’ve got a whole set of classmates and other Code Fellows graduates to pull from to hold you accountable.

Make a pact with someone (or several people) to meet every week or every few days. Review each other’s code. Edit each other’s blog posts. Contribute to each other’s projects, or collaborate on the same project. Set goals together and celebrate together when you meet those goals. “Let’s each send out 10 applications this week!” “How about you write a blog post about AWS, I write one about Google App Engine, and we reference each other’s posts?” “You build out the scaffolding for this project and I’ll add this other app, since it’s something I’m working on for one of my other projects.”

Find someone that you work together well with and...work together! A solid collaboration can severely slash any project’s timeline, giving you more content to fill your resume, LinkedIn, and portfolio. And don’t limit yourself only to Python graduates. One of the great things about the larger programming world is that different languages can do different things well that Python cannot (or should not) do. Collaborate with a JavaScript grad so that you can build a back-end and they can build a front-end that accesses your API and displays data to the user. Work with an iOS developer and build yourself a solid mobile app. Bolster the diversity of your experiences with what time you have before you get locked into a career as one thing.

Podcasts and New Developer Resources

- [BaseCS](https://www.codenewbie.org/basecs){:target="_blank"}
- [Talk Python to Me](https://talkpython.fm/){:target="_blank"}

### Python Continuing Education

The world of Python is vast, and we’ve only covered a small fraction in this class. In order for you to grow as a developer, you need to be willing to dive deeper into the wider universe of Python tools, but it’s difficult to know which ones to hone in on. Here’s a listing of some commonly-cited tools and concepts from the wider world of Python:

- [Django React](https://github.com/Seedstars/django-react-redux-base){:target="_blank"}: A project using Django as the back-end and ReactJS as the front-end
- [Django Channels](https://channels.readthedocs.io/en/stable/){:target="_blank"}: A project nudging Django in the direction of being “event-oriented” rather than relying solely on the web request-response cycle; Here’s a good tutorial
- [Flask](http://flask.pocoo.org/){:target="_blank"}: A micro webframework for Python. Quick to set up and used often.
- [Tornado](http://www.tornadoweb.org/en/stable/){:target="_blank"}: A Python web framework that doesn’t rely on WSGI like Flask and Django. It supports WebSockets, which allow for a different mode of communication than strict HTTP.
- Pandas/NumPy/SciPy/Scikit-Learn/Matplotlib: The Python science and analysis stack
- [OpenCV](http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_tutorials.html){:target="_blank"}: An open source computer vision library. The most popular kind, and used often with large companies looking to automate image classification (or use things like facial recognition) for use in larger products.
- [itertools](https://docs.python.org/3/library/itertools.html){:target="_blank"}: Super-efficient looping and iterating
- Celery/Redis/RabbitMQ: Tools for running asynchronous tasks alongside your main app.
- [Oscar Commerce](http://oscarcommerce.com/){:target="_blank"}: an open-source ecommerce framework for Django
- [GeoDjango](https://docs.djangoproject.com/en/1.10/ref/contrib/gis/){:target="_blank"}: a web framework for building GIS (geographic information system)-enabled applications
- [Python Natural Language Toolkit](http://www.nltk.org/){:target="_blank"}: the premier Python platform for working with language data
- [Boto3](https://aws.amazon.com/sdk-for-python/){:target="_blank"}: A Python interface for Amazon Web Services
- [Cython](http://cython.org/){:target="_blank"}: A C-extension of Python that is compiled instead of interpreted, making execution super fast..
- Scrapy & BeautifulSoup

### Non-Python Continuing Education

The life of a developer always extends outside of their base language. It’s important that you allow yourself time to explore the world outside of Python, and the very next most important languages are JavaScript and Go. But, there’s a lot, and not every thing that you should dip into is even language-specific. Here’s a listing of tools that are commonly paired with Python, as well as other stuff that’s just good to learn. Not writing descriptions for these because there’s just too many:

- JavaScript MEAN stack (MongoDB, ExpressJS, AngularJS, NodeJS)
- JavaScript MERN stack (MongoDB, ExpressJS, ReactJS, NodeJS)
- Jest Test Running
- The greater AWS ecosystem, starting with S3
- Microsoft Azure
- Google App Engine
- C (because Python is based on it/written in it)
- Java (language)
- C# (language)
- R (language)
- Go (language)
- Jenkins CI
- Salt Stack/Fabric
- Hadoop/MapReduce
- Selenium Web Testing
- Docker
- Various SQL implementations (MySQL, Postgres, etc)
- OpenStack
- Low Level Processes (Memory, heap, stack, the nitty gritty that we don’t have time for.)
- Linux / Bash / Shell scripting
- Apache Cassandra
- D3.js Charting
- Development methodologies (Agile, SCRUM, Extreme Programming, etc.)
- Apache Spark
- Android SDK
- GIS, PostGIS
- GitLab, Bitbucket, and other remote git implementations
- Above all else, stay sharp, and learn more faster!

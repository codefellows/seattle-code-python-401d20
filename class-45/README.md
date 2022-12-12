# Final Projects

## High Level Requirements

- Use any, all, most, or none of what you learned ...
  - Make sure it works great.
  - Make sure it's covered in tests.
    - 80% coverage minimum. 
  - Authenticate your API.
  - Stretch yourself.
- Tell a great story!

### Deployment

- Deploy site(s) and Databases live.
  - Hosted anywhere except GitHub Pages. 

Tools At Your Disposal

- Command Line Interface tools
- Jupyter/Kaggle Notebooks
- Web Scraping (within [limits](https://www.scrapehero.com/how-to-prevent-getting-blacklisted-while-scraping/)){:target="_blank"}
- Remote APIs
  - Restful
  - Others
- Custom APIs
- ... or teach yourself something totally new this week!

## Workflow

- To manage Tasks ...
  - Agile / Kanban Workflow
  - Project Management System
    - [Trello](https://trello.com/b/2GAur1IN/open-shelf-a-book-wiki?menu=filter&filter=label:Lab%2014){:target="_blank"}
    - [Github Projects](https://help.github.com/articles/about-project-boards/){:target="_blank"}
    - [Jira](https://www.atlassian.com/software/jira)
    - [Azure Boards](https://azure.microsoft.com/en-us/services/devops/boards/){:target="_blank"}

- To Manage and Deploy Code
  - SCM: Use the strict [Git Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow){:target="_blank"}
  - Deployment:
    - Local dev/feature branches
      - One Branch Per Feature
    - Staging (Pre-Production) Branch
    - Main (Production) Branch
  - Developers work locally in feature branches
  - Must follow professional Git workflow
  - Check-in and merge PRs against `stage`
  - Once verified, PR stage against main and "deploy"
  - Protect `main` from direct check-ins
    - Ask TA/Instructor if not sure how to protect branch.
  - Merge from `stage` to `main` according to team agreement
  - Testing: Hook in GitHub Actions for live code testing
    - E.g. of this in your `data-structures-and-algorithms` repo.

## Development Schedule

### Class 45 (Kick Off)

- Complete Team Agreement
- Complete Project Pitch
  - Get Instructor Approval
- Create your GitHub organization
  - Back-End Repo
  - Front-End Repo
  - Other Repo's for supporting services
- Deploy a simple "Hello World" server through your full pipeline
  - Stage and Production of all apps
  - Tests hooked up and passing
- Get your project board setup with your initial stories
  - At this stage, its's probably just stories to write more stories...
- Setup documentation

### Class 46 (Project Start)

- Wireframes Complete
- User workflows finalized
- Initial design planned
- Code

### Class 47 (Core MVP)

- First MVP should be completed by EOD
- Your core functionality should be working end to end.
  - Databases (if applicable) hooked up and saving
  - User workflow works (navigation, actions)

### Class 48 (Final MVP)

- Adding Non-Breaking Features
- Final "MVP" should be complete
  - Whatever you have by EOD should be presentation ready
  - Anything you add from this point on is purely additive.

### Class 49 (Polish)

- Final (safe) tweaks
- Presentation Practice

### Class 50 (Presentation Day)

- Eat.
- Drink.
- Present.
- Win.

## Presentations

- Prepare a slide "deck" to present your project
- Why a deck? It's a helpful tool to keep you on time and on focus. Also, you will spend a lot of time in dev jobs speaking in front of a deck, so this is good practice for that. Know what's on screen behind you and prepare to speak in what appears to be an 'ad-hoc' fashion in front of it.

[Presentation Deck Template](https://docs.google.com/presentation/d/1NeXKKEpjK2DDme8EwlZBsJndUqIgGYzWrY6FAYtNTf0/edit#slide=id.g2accd1c413_3_31){:target="_blank"}

**NOTE:** Use the template as a baseline. It's completely fine to modify/enhance it. If you prefer another authoring tool then use it. But make sure it meets baseline requirements of Template.

## Tips and Tricks

- Solve a real business or community problem
- Deliver something desirable (make it rock!)
- Don't over-complicate. Sometimes, the simplest solution can be the most scalable and stable. Favor stability and tightness over wizardry

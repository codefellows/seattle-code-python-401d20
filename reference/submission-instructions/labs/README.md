# Python Lab Submission Instructions

## Creating Project

- > mkdir example-lab
- > cd example-lab
- > touch README.md

### Create virtual environment

- > python3 -m venv .venv
  - NOTE: Replace `python3` with more specific version as needed.

### Activate virtual environment

- > source .venv/bin/activate

### Create modules and scripts

- > mkdir example_lab
- > touch example_lab/example_script.py

**Note the underscore vs hyphen**

### Install packages

For example:

- > pip install favorite-library
- Record package dependencies
- > pip freeze > requirements.txt

Should result in this file tree:

```console
└── example-lab
    ├── README.md
    ├── requirements.txt
    └── example_lab
        └── example_script.py
```

## Tests

Many labs will have tests using PyTest

- > `pip install pytest` # or pytest-watch
- > `pip freeze > requirements.txt`
- > `touch tests/__init__.py` (Note: 2 underscores on both sides.)
- > `touch tests/test_example.py`

Should result in a file tree like this:

```sh
└── example-lab
    ├── README.md
    ├── requirements.txt
    ├── example_lab
    │   └── example_script.py
    └── tests
        ├── __init__.py
        └── test_example.py
```

## README

- Your project's README.md should match structure of [template README](./README-template.md){:target="_blank"}

## Git

### On Local System

Initialize local Git repository

- > git init
- > touch .gitignore
- Add `.venv` folder to `.gitignore`
- > git add .
- > git commit -m "first commit"

### On Github site

- create EMPTY repository `example-lab` on Github. **Do NOT** initialize with README, license or gitignore.
  - Those will be added soon
- The next screen will have a "Quick Setup" section with a url available to copy. Copy it ;)

### On local system (again)

```sh
git remote add origin the_url_you_copied_that_ends_with_git
git push -u origin main
```

Now everything is wired up between local machine and Github.

## Canvas Submission

- Submit a link to the README.md from your assignment branch in Canvas

## Resubmits

- Any commits made to submission branch will be updated in the PR
- In event of assignment resubmission, submit submission branch PR on canvas

## Github Actions

This step is **optional** early in course. Instructor will inform you when it is required.

Setup "Github Actions" so that your code can be properly tested in Github as you make new pushes to your branches and pull requests to master

- Include following yaml code

> Github will now run all of your automated tests and check formatting every time you push code to a branch or try to merge a pull request. In fact, it will block pull requests until your tests are all passing.

```yml
name: Run Python Tests
on:
  push:
    branches:
      - main
    paths:
      - 'python/**'
  pull_request:
    branches:
      - main
    paths:
      - 'python/**'

jobs:
  ci:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python 3.9
        uses: actions/setup-python@v2
        with:
          python-version: 3.9
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
        working-directory: ./python
      - name: Test with pytest
        run: pytest -vv
        working-directory: ./python
```

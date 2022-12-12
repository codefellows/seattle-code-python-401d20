# Python Development on Windows : Set up

While Python itself runs fine on Windows, many of the tools that a Python developer needs can behave unexpectedly on Windows.

The fact is that most Python development assumes you'll be working on a Unix based system.

The good news is that Windows has made it (relatively) easy to get such a Unix based system running right within Windows itself.

There is a tool called WSL (or Windows Subsytem for Linux) that will need to be installed so that all our supporting tools (Poetry, VS Code, multiple versions of Python) can play well together.

I tried to go with a Windows native solution and it worked on my machine. But, as several of found out the hard way, the native solution does NOT work always.

Listed below are the steps to get all set up on Windows. It takes a while to complete all the steps. But most of the time is spent waiting for things to install and build.

Please let me know if you have any issues.

**Note** Big thank you to Simon for confirming these instructions work!

## WSL

- [Install WSL](https://codefellows.github.io/code-201-prework/prework/windows/02_WSL_Ubuntu_setup.html)
  - Stop at end of page 1

## Pyenv

- [Pyenv Installer](https://github.com/pyenv/pyenv-installer)
  - Make sure to [install prerequisite](https://github.com/pyenv/pyenv/wiki/Common-build-problems) libraries following instructions for Ubuntu/Debian
  - Note **warning** at bottom of installer feedback in terminal regarding adding to .bashrc

## Installing Python

Now we can (finally) install Python

```> pyenv install 3.8.2```

This will take a while but when it's all done...

```> pyenv versions```

should show Python 3.8.2 available. Let's make it the default version

```> pyenv global 3.8.2```

check python version again

```> python —V```

Should now be 3.8.2

## Poetry

- [Install Poetry](https://python-poetry.org/docs/#installation)
  - Use **osx / linux / bashonwindows install instructions**
- ```> poetry -h```
- ```> poetry new python-fun```
- ```> cd python-fun```
- ```> poetry shell```
  - You may get an error here regarding permissions on .config folder.
    - If so ```> sudo chown your_unix_username /home/your_unix_username/.config```
- ```> poetry install```
- ```> pytest```
  - Should be all green

## VS Code - WSL Integration

- Install the [Remote - WSL Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl) on VS Code
  - This allows you to use WSL as your integrated development environment and will handle compatibility and pathing for you. Learn more.
- Restart VS Code
- Install [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
  - Takes a while to fully install, Check status in Extensions panel
  - Restart VS Code
- Open python file in editor
  - Notice wrong virtual environment
- Open VS Code settings
  - ctrl + ,
  - Search for Python: Venv Path
  - Add ```~/.cache/pypoetry/virtualenvs```
  - Alternately update settings.json to include ```“python.venvPath”: “~/.cache/pypoetry/virtualenvs"```
- Restart VS Code
- Select correct virtual environment from dropdown when you click on Python Interpreter
  - Usually at bottom left of screen
  - will have your folder name as part of it
- Next time you start VS Code should hold on to it

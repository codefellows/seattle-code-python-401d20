# Importer

Running scripts that import other modules can sometimes be a confusing experience.

For example, everything works fine when running PyTest but stops working when you execute a module directly.

There is a method behind the madness but it's tricky and the docs can be difficult to make sense of.

A couple good resources are [Python import, sys.path and PYTHONPATH tutorial](https://www.devdungeon.com/content/python-import-syspath-and-pythonpath-tutorial) and [How to Run Your Python Scripts](https://realpython.com/run-python-scripts/)

But sometimes it's best to just fire up Python and start poking things.

Activate virtual environment

Now execute root.py from the root folder of project.
> $ python root.py

You should see...

```console
I am root
I am module a in package a
I am module b in package a
I am module a in package b
I am module b in package b
```

If you don't see that then there are other issues that must be dealt with first.

The script located in root.py is able to successfully load imported modules from other folders/files in project.

Now try to execute `package_a/module_a_a.py` directly
> $ python package_a/module_a_a.py

You will now see something like...

```console
Traceback (most recent call last):
  File "package_a/module_a_a.py", line 1, in <module>
    import root
ModuleNotFoundError: No module named 'root'
```

What's going on? Can't we directly execute module_a_a?

The answer is yes but we need to give Python (aka the Python interpreter) one little bit of information because when the nested module is executed directly the paths to the other modules is lost.

Try this instead. **NOTE** Make sure the terminal's working directory is still at the root.

> $ PYTHONPATH='.' python package_a/module_a_a.py

Now you should see...

```console
I am module a in package a
I am root
I am module a in package a
I am module b in package a
I am module a in package b
I am module b in package b
```

That extra bit of information in the PYTHONPATH variable tells interpreter that even though the script being executed lives in a different location on filesysem we still want the current directory to be one of the locations the Python interpreter uses when loading modules.

Play around with this. Does this approach work for the other packages and modules? Can you change your terminal's working directory and still make it work? **HINT:** you can but will require adjusting PYTHONPATH

An alternate (and less wordy) way to safely execute script is to execute it as a module with `-m` flag.

E.g. `python -m package_a.module_a_a`

Note the missing .py extension and use of dots vs slashes.

This approach only works in root of project.

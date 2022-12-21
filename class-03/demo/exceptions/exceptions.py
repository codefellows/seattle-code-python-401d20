# Fun with Exceptions
# Exceptions handle errors that you can't know about until running the application
#
# They are different than errors that are known about in advance

print("let's do something totally wrong. See if you can spot me in the output!")
print("Too many parentheses"))


print("More wrongness. Do I get printed?")
print("Who has ever "messed up" quotations marks?")


# Notice how both failed to execute AND didn't show the initial print.
#
# That's what happens with syntax errors.
#
# But how about logical errors that ARE syntactically correct?

print("What happens now? Do you see me printed?")
value = 1/0

# Got a ZeroDivisionError at runtime
#
# Notice intial print DID display this time
#
# Check out the error
#
# Getting a descriptive error is good
#
# WAY better than getting a non-descriptive or even non-existent one
#
# So always pay attention to anything an error is telling you


# You can handle these errors in your code

try:
    print("Divide by zero again", 1 / 0)
except ZeroDivisionError:
    print("Don't divide by zero silly.")

print("handled the exception above, carrying on")


# Notice that we "caught" a specific exception. It is a best practice to only catch specific exceptions
#
# To put it another way it is a VERY BAD THING to catch generic exceptions Here is why that's considered an anti-pattern


try:
    print("Divide by zero again", 1 / "spam")
except:
    print("Don't divide by zero silly.")

print("Total lie!. The problem was not dividing by zero. It was a type error")


# variation on previous step

try:
    print("Divide by zero again", 1 / "spam")
except Exception:
    print("Don't divide by zero silly.")

print("Still wrong. Handling the base Exception is a 'catch all'")

# If you must handle every exception then make sure to retain the relevant error info.
#
# For example, you may have requirement that end user never sees a program error.
#
# In that case make sure to log/record the error details and then present something more palatable to end user


try:
    spam = "nonsense" / 42
except ZeroDivisionError:
    print("Don't divide by zero silly.")
except Exception as e:  # notice we can refer to the exception using 'as'
    # log the exception somewhere, probably including the stack trace
    print("So sorry end user. Something broke!")

# Python also allows you do a couple more things with exceptions
#
# One is an 'else' block which runs when there was NOT an exception This is not that commonly used but every now and then is helpful


print("Attempting to create message")
try:
    message = "nothing" + "wrong" + "here"
except TypeError:
    print("Unable to create message")
else:
    print("Message successfully created")

# The last piece is the 'finally' block which is run no matter what happened


print("prepare for breakage")

try:
    value = True + " nonsense"  # change to str(True) and see what happens
except TypeError as e:
    print(f"Something broke! Details: {e}")
else:
    print(f"smooth sailing. value is {value}")
finally:
    print("clean up mess as needed")

# you can raise exceptions intentionally as well
#
# If there's no better choice can use the Generic Exception
#
# It's a best practice to choose the most appropriate type of Error


age = -10

if age < 0:
    raise ValueError("Invalid age - must be greater than or equal to zero")


raise Exception("Something bad happened")

# You can also create your own Exception types.
#
# This will make more sense when we cover Classes next session
#
# but here's a sneak peek



class SocialDistanceError(Exception):
    def __init__(self, distance):
        super().__init__(f"Stay 6 feet away, not {distance}")


distance_feet = 4

if distance_feet < 6:
    raise SocialDistanceError(distance_feet)

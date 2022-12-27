# Why
# We're pretty good as humans at intuitively counting things, at least until the numbers get big.
#
# E.g. Look at a fruit basket and tell the most common fruit. We can usually do a decent job at that without spending too much time thinking about it.
#
# How can we tell a computer to do it?

fruit = ["apple", "banana", "orange", "apple", "banana", "apple"]

# Write code to determine fruit is most common?
# What about 2nd most?
# Least common?
# attempt #1
fruit_map = {}
for piece in fruit:
    current_count = fruit_map.get(piece, 0)
    fruit_map[piece] = current_count + 1

print(fruit_map)
{'apple': 3, 'banana': 2, 'orange': 1}

most_common_count = 0
most_common_fruit = None

for fruit_name in fruit_map:
    if fruit_map[fruit_name] > most_common_count:
        most_common_count = fruit_map[fruit_name]
        most_common_fruit = fruit_name

print(most_common_fruit)
# apple

# That works, at least for most common.
# Could probably do similar thing for least common
# Not sure what to do about frequencies in the middle
# And that took a fair amount of code.
# What
# It turns out that the Python Standard Library has a very handy module to help us out...
# How
# Since it's in Standard Library we don't need to install it
# Just import and use

from collections import Counter

fruit_counter = Counter(fruit)

print(fruit_counter)
# Counter({'apple': 3, 'banana': 2, 'orange': 1})

# Well look at that, we got a dictionary (or at least something dictionary like) for cheap.
# It gets better

most_common = fruit_counter.most_common()
print(most_common)
# [('apple', 3), ('banana', 2), ('orange', 1)]

# "You're welcome" - Python Standard Library

# Pro Tip: Great place to find out about Counter and more is Python Module of the Week
# https://pymotw.com/3/

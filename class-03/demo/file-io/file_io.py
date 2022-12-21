# Files in Python
file = open('assets/spam.txt')
print(file)
contents = file.read()
print(contents)

# Closing the file
# The file is still "open"
print('Is file closed?', file.closed)
# let's explicitly close it
file.close()
print('Is file closed?', file.closed)

# often you don't need to worry about closing the file since Python usually handles that.
# but words like 'often' and 'usually' are a programmers constant foe
# fortunately, there's an easy way to make sure that it always gets closed up properly
with open('assets/spam.txt') as file:
    print(file.read())

print('file is closed?', file.closed)


# That with key word there creates something called a context manager
# They are a more advanced topic, but you'll see them used a lot with files because they are so dang handy
# Quick documentation with help and dir
# You can see the attributes of file object easy enough
help(file)
dir(file)


# File modes
# When you open a file you supply a 'mode' - the default mode is 'r' for 'read'
# so open('somefile.txt') is the same as open('somefile.txt','r')
# You pretty much have to memorize the modes
# Luckilly there aren't that many. Here are the most popular
# r for read
# w for write
# a for append
help(open)

with open('assets/brain.jpg', 'rb') as f:
    contents = f.read()

for x in contents[:128]:
    print(type(contents))

with open('assets/brain.copy.jpg', 'wb') as f2:
    f2.write(contents)


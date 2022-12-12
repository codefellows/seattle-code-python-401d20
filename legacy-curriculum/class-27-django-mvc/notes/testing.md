# Django Testing
Testing in Django, including a bit on using Factory Boy to manage test data

By this point we should be moving forward on our models for our lender app. That means we should be testing these models - and that means we need to look at Django’s testing framework.

Up until this point, we’ve been using `py.test`. It is possible to use `py.test` with Django, but if we want to use Django’s testing methods, we need to be familiar with `unittest`. The biggest difference between `py.test` and `unittest` is that `unittest` is predicated on the idea of a TestCase class.

## Django and UnitTest
Let’s talk for a moment about how `unittest` operates. Unittest uses the TestCase class, and you subclass from the base TestCase class. When using Django, this comes from the Django testing module. When you generate an app, it builds a test file. It imports `TestCase` there:

_/lending_library/patron_profile/tests.py_
```python
from django.test import TestCase
```

This is Django’s version of TestCase, so it has some special attributes. The basic idea is that you create some class that inherits from Django’s TestCase:

_/lending_library/patron_profile/tests.py_
```python
class ProfileTestCase(TestCase):

    def test_foo(self):
        self.assertTrue(False)
```
Every method you write on that class that begins with test will be run by Django’s test runner. `TestCases` can only take self, and whatever code is inside will be executed as a test.

# setUp / teardown
_/lending_library/patron_profile/tests.py_
```python
class ProfileTestCase(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_foo(self):
        self.assertTrue(False)
```
These two setUp and tearDown methods are similar to `py.test` fixtures. They allow you to create a universe for your tests to run in. setUp and tearDown are test level fixtures. The code inside is executed for every single test.

There are also case level fixtures called `SetUpClass` and `TearDownClass`. These don’t generally get used. If you use them, be sure to decorate them with `@classmethod`, as they’re intended to be class methods that run once per `TestCase` instance.

Let’s set up a breakpoint to inspect this:

_/lending_library/patron_profile/tests.py_
```python
from django.test import TestCase


class ProfileTestCase(TestCase):

    def setUp(self):
        self.username = 'boo'

    def test_foo(self):
        import pdb; pdb.set_trace()
        self.assertTrue(False)
```
We can run our tests like so:
```bash
$ python manage.py test
Creating test database for alias 'default'...
> .../django_lender/lending_library/patron_profile/tests.py(11)test_foo()
-> self.assertTrue(False)
(Pdb) self
<patron_profile.tests.ProfileTestCase testMethod=test_foo>
```
Now at our breakpoint, we can inspect what self is. Currently that returns `<patron_profile.tests.ProfileTestCase testMethod=test_foo>` which an instance of the ProfileTestCase.


We can see our attributes from `setUp` are available:
```bash
(Pdb) self.username
'boo'
```
We can make assertions:
```bash
(Pdb) self.assertTrue(self.username == 'boo')
(Pdb)
```
Any time an assertion does not raise an error, we know our test passed. There are methods available that are useful to us:
```bash
(Pdb) assertions = [name for name in dir(self) if name.lower().startswith('assert')]
(Pdb) assertions
['assertAlmostEqual', 'assertAlmostEquals', 'assertContains', 'assertDictContainsSubset', 'assertDictEqual', 'assertEqual', 'assertEquals', 'assertFalse', 'assertFieldOutput', 'assertFormError', 'assertFormsetError', 'assertGreater', 'assertGreaterEqual', 'assertHTMLEqual', 'assertHTMLNotEqual', 'assertIn', 'assertInHTML', 'assertIs', 'assertIsInstance', 'assertIsNone', 'assertIsNot', 'assertIsNotNone', 'assertItemsEqual', 'assertJSONEqual', 'assertJSONNotEqual', 'assertLess', 'assertLessEqual', 'assertListEqual', 'assertMultiLineEqual', 'assertNotAlmostEqual', 'assertNotAlmostEquals', 'assertNotContains', 'assertNotEqual', 'assertNotEquals', 'assertNotIn', 'assertNotIsInstance', 'assertNotRegexpMatches', 'assertNumQueries', 'assertQuerysetEqual', 'assertRaises', 'assertRaisesMessage', 'assertRaisesRegexp', 'assertRedirects', 'assertRegexpMatches', 'assertSequenceEqual', 'assertSetEqual', 'assertTemplateNotUsed', 'assertTemplateUsed', 'assertTrue', 'assertTupleEqual', 'assertXMLEqual', 'assertXMLNotEqual', 'assert_']
```
So as you can see there are many assertions available. Some of the ones that are Django specific:

`assertTemplateUsed`, `assertTemplateNotUsed`
You can check that proper Django templates are being used or not used.
`assertInHTML`

## `self.client`
```bash
(Pdb) self.client
<django.test.client.Client object at 0x104d03dd0>
```
When we used `py.test` to create a browser-experience with Pyramid, we used a `webtest` object. Django in-turn has `.client`. It’s similar to calling a browser.

We can continue the test and see that it fails:
```bash
(Pdb) c
F
======================================================================
FAIL: test_foo (patron_profile.tests.ProfileTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/.../django_lender/lending_library/patron_profile/tests.py", line 11, in test_foo
    self.assertTrue(False)
AssertionError: False is not true

----------------------------------------------------------------------
Ran 1 test in 272.382s

FAILED (failures=1)
Destroying test database for alias 'default'...
```
Django gives us some information about the failed test: `AssertionError: False is not true`

## [Factory Boy](https://factoryboy.readthedocs.org/en/latest/index.html)
Let’s write some tests that cover the functionality of our models.

- We want to be able to use our model objects in our test.
- You _could_ use `initial_data` fixtures (that can be stored in JSON format) on your tests.
    - Fixtures can have problems:
        - Create a model
        - Dump it out into JSON Fixtures
        - You might make, for example, users - maybe one named Bob
        - Later you may make a rule that usernames need to be 5 characters minimum.
        - Now your fixture is out of date

Now you have a maintenance burden to make sure your data fixtures stay up to date. There are tools to help us with this.

Enter Factory Boy. It’s similar to ruby’s Factory Girl. The idea is to provide us with factories that will generate test objects that meet our expectations. We can assert that they work at that point.

The basic idea is that we can write a test with Factory Boy where we set up an order that is part of our tests, then we run the test. Let’s install Factory Boy.
```bash
$ pip install factory_boy
```
Now we can set up a class that inherits from factory and informs the factory what model we are going to use. We update our tests:

_/lending_library/patron_profile/tests.py_
```python
from django.contrib.auth.models import User
from django.test import TestCase
import factory


from patron_profile.models import PatronProfile

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
```
Now we have Factory Boy generate a user for us in our test setup:

_/lending_library/patron_profile/tests.py_
```python
...
class ProfileTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory.create()
...
```
Let’s look at this now:
```bash
$ python manage.py test
Creating test database for alias 'default'...
> /.../django_lender/lending_library/patron_profile/tests.py(19)test_foo()
-> self.assertTrue(False)
(Pdb) self.user
<User: >
Our self.user is actually a User. What are the values of its attributes?:

(Pdb) self.user.username
u''
(Pdb) self.user.email
u''
(Pdb) self.user.password
u''
```
Well, we haven’t actually set that up yet. For now they are empty strings.

## Factory Values
We can create a user and that user exists, but we might want to add more to it:

_/lending_library/patron_profile/tests.py_
```python
...
class ProfileTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory.create(username='bob', email='bob@example.com')
        self.user.set_password('secret')
...
```
Now when we run our tests and inspect our user at the breakpoint:
```bash
$ python manage.py test
Creating test database for alias 'default'...
> /.../lending_library/patron_profile/tests.py(20)test_foo()
-> self.assertTrue(False)
(Pdb) self.user
<User: bob>
(Pdb) self.user.username
'bob'
(Pdb) self.user.email
'bob@example.com'
```
We don’t actually need to set up our user this way. We can use the factory to generate users for us. Let’s say we want to create a username and email when we actually setup our user. We can create attributes of our factory that correspond to the values that we want. Let’s say all of our users should be named ‘bob’. We update our tests.py:

_/lending_library/patron_profile/tests.py_
```python
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.test import TestCase
import factory

from patron_profile.models import PatronProfile


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = 'bob'
    email = 'bob@example.com'


class ProfileTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory.create()
        self.user.set_password('secret')
        self.user.save()

    def test_foo(self):
        import pdb; pdb.set_trace()
        self.assertTrue(False)
```
Now when we run our tests and hit our breakpoint, our user has attributes that are provided by Factory Boy:
```bash
$ python manage.py test
Creating test database for alias 'default'...
> /.../patron_profile/tests.py(26)test_foo()
-> self.assertTrue(False)
(Pdb) self.user
<User: bob>
(Pdb) self.user.username
u'bob'
(Pdb) self.user.email
u'bob@example.com'
(Pdb)
```
But if you want to override a factory, that’s possible too:

_/lending_library/patron_profile/tests.py_
```python
...
class ProfileTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory.create(username="sally")
        self.user.set_password('secret')
        self.user.save()
...
```
```bash
(Pdb) self.user
<User: sally>
```

## Lazy Attributes
We don’t necessarily need to set static values for our tests. We can use “Lazy Attributes”. These can take functions as a way of generating something. We may want to set something up so that our email is created from the username.

_/lending_library/patron_profile/tests.py_
```python
...
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = 'bob'
    email = factory.LazyAttribute(
        lambda x: "{}@example.com".format(x.username)
    )


class ProfileTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory.create()
        self.user.set_password('secret')
        self.user.save()
....
```
```bash
(Pdb) self.user
<User: bob>
(Pdb) self.user.email
u'bob@example.com'
```
And if we redo our override:

_/lending_library/patron_profile/tests.py_
```python
...
class ProfileTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory.create(username="sally")
        self.user.set_password('secret')
        self.user.save()
...
```
```bash
(Pdb) self.user
<User: sally>
(Pdb) self.user.email
u'sally@example.com'
```
So it’s possible to use functions to generate the values you want. We could say perhaps we have a validation rule that usernames are at least 5 characters. Keep in mind that the `factory.LazyAttribute` receives one and only one argument which is the instance that’s about to be built along with the static attributes that belong to it already in place.

## [Sequences](https://factoryboy.readthedocs.org/en/latest/#sequences)
We can also set up sequences. `email = factory.Sequence(lambda n: 'person{0}@example.com'.format(n))`. This inserts a number that increments:

_/lending_library/patron_profile/tests.py_
```python
...
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: "user{}".format(n))
    email = factory.Sequence(
        lambda n: "user{}@example.com".format(n)
    )


class ProfileTestCase(TestCase):

    def setUp(self):
        self.users = []
        for i in range(5):
            user = UserFactory.create()
            user.save()
            self.users.append(user)
...
```
```bash
(Pdb) self.users
[<User: user0>, <User: user1>, <User: user2>, <User: user3>, <User: user4>]
(Pdb) [u.email for u in self.users]
[u'user0@example.com', u'user1@example.com', u'user2@example.com', u'user3@example.com', u'user4@example.com']
```
We can automatically create this data and then make assertions. For example, we want to make sure a profile gets created when we make a user...:

(Question in class happens here: `.create()` - does the UserFactory class, whatever it inherits from, have a create method? A: Yes.) Explanation below:

[Using Factories](https://factoryboy.readthedocs.org/en/latest/#using-factories) shows us our various build strategies.

- `.build()` - an instance that’s not saved
- `.create()` - an instance that is saved
- `.stub()` - makes a user, but it’s not connected to the database. What’s nice about this is you can use it for unit testing things, where you don’t actually depend on the database. Like maybe the `__str__` method of your user, you can test it without writing the user to the database. This can be faster, so it makes testing faster, which is always good.

It’s worth knowing that one of the most important differences between MySQL and PostgreSQL is that the layer of SQL queries that we call the data definition layer (things like CREATE or MODIFY table, DROP table, etc.), in Postgres, those kinds of queries can be executed inside a transaction, whereas in MySQL they cannot. In other words in MySQL when you do a query, it happens, it’s committed, and it’s done. In Postgres you can run the queries and then do a rollback. One of the deepest implications with this when you’re working with a system like Django is that Django will not actually destroy your database inside a test. Instead it will run the table generation schemes inside a transaction so that it can roll them back at the end. It means you get a speed gain when you run tests with PostgreSQL vs MySQL. This can have an impact on your development cycle.

## Testing Signaled Profile
Ok, back to demonstrating a test. First thing is we’ll take out the code that actually executes the handlers that sets up the event listeners that create a profile when you create a user:

_/lending_library/patron_profile/app.py_
```python
from django.apps import AppConfig


class PatronProfileAppConfig(AppConfig):
    name = "patron_profile"
    verbose_name = "Lending Library User Profile"

    # def ready(self):
    #     """code to run when the app is ready"""
    #     from patron_profile import handlers
```
Now we’ll write a new test:

_/lending_library/patron_profile/tests.py_
```python
...
class ProfileTestCase(TestCase):

    def setUp(self):
        pass

    def test_profile_is_created_when_user_is_saved(self):
        self.assertTrue(PatronProfile.objects.count() == 0)
...
```
First we want to build a user without saving it. Let’s make sure there is no PatronProfile. When the test starts to run, we assert there are no PatronProfile objects. This test passes.

Now let’s create ourself a user. We’ll assert that a PatronProfile is created at the same time. This test should fail because we disconnected the event listeners earlier:

_/lending_library/patron_profile/tests.py_
```python
...
class ProfileTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory.build()

    def test_profile_is_created_when_user_is_saved(self):
        self.assertTrue(PatronProfile.objects.count() == 0)
        self.user.save()
        self.assertTrue(PatronProfile.objects.count() == 1)
```
```bash
$ python manage.py test
Creating test database for alias 'default'...
F
======================================================================
FAIL: test_profile_is_created_when_user_is_saved (patron_profile.tests.ProfileTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/.../django_lender/lending_library/patron_profile/tests.py", line 27, in test_profile_is_created_when_user_is_saved
    self.assertTrue(PatronProfile.objects.count() == 1)
AssertionError: False is not true

----------------------------------------------------------------------
Ran 1 test in 0.007s

FAILED (failures=1)
Destroying test database for alias 'default'...
```

Now we can reconnect our event listeners by uncommenting out that code in app.py, and our test should pass. We’ve used a factory to demonstrate a reality about how our system is working.

When you test Django, there’s a rule of thumb. **Don’t bother testing things that are Django’s responsibility**. You don’t need to test that when you create a user that it’s an instance of the User class, because Django should take care of that for you.

You do want to test things that you’ve built that leverage Django’s systems. In this case, we’re leveraging Django’s signal system to create a secondary object when an existing object is created. We make a user and save it, the end result should be that a profile exists. That we want to test, because that’s functionality added to the system.

We also want to make sure that the PatronProfile is hooked up to the User in the ways that we expect it.

When we look at our user, it’s name should be dependent on the name of the user itself.
In our models, we have this `__str__()` method that returns the user’s full name or username if that doesn’t exist.
```python
def __str__(self):
    return self.user.get_full_name() or self.user.username
```

We’ll write a test that demonstrates that our profile’s `__str__()` representation is the same as the representation that we get when we look at the user. First we’ll comment out our `__str__()` method and have it return an empty string so we can see our test fail first.

_/lending_library/patron_profile/models.py_
```python
@python_2_unicode_compatible
class PatronProfile(models.Model):
...
    def __str__(self):
        return ''
        # return self.user.get_full_name() or self.user.username
...
```

_/lending_library/patron_profile/tests.py_
```python
class ProfileTestCase(TestCase):
...
    def test_profile_str_is_user_username(self):
        self.user.save()
        profile = PatronProfile.objects.get(user=self.user)
        self.assertEqual(str(profile), self.user.username)
```
```bash
$ python manage.py test
Creating test database for alias 'default'...
.F
======================================================================
FAIL: test_profile_str_is_user_username (patron_profile.tests.ProfileTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/.../django_lender/lending_library/patron_profile/tests.py", line 32, in test_profile_str_is_user_username
    self.assertEqual(str(profile), self.user.username)
AssertionError: '' != u'user1'

----------------------------------------------------------------------
Ran 2 tests in 0.021s

FAILED (failures=1)
Destroying test database for alias 'default'...
```

Here we have a factory that sets up a user for us. We’ll save() the user first. We’ll create a profile object who’s User object is the user we just created and saved. Then we want to assert that the str of our profile is equal to our user.username.

`AssertionError: '' != u'user1'`

Let’s go ahead and return to our model and un-comment the code that provides this functionality. Now our test should pass.

We could write another test that uses the `get_full_name()` method on the user if we wanted our users to have first and last names as well. We could do things like assert whether a user is active or inactive to test our `is_active()` method. We can begin to make assertions about the functionality as part of the API that is our universe in our app.

Factory Boy is going to let you control setting up the instances for your classes in a compelling way. There is good documentation about it. When it comes to using Factory Boy with ORMs, there is a lot of information about using Django itself directly. You’ll want to pay attention to that. https://factoryboy.readthedocs.org/en/latest/orms.html#django. They have Django model factories already set up for you.

## Incorporating the Faker Library
You can use this in conjunction with the Faker library that we used for our Pyramid apps. It will generate random data that should fit into a field:
```python
from faker import Faker
fake = Faker()

class RandomUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.User

    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
```
```bash
>>> UserFactory()
<User: Lucy Murray>
```

## Incorporating Test Coverage
Since we’re not using pytest anymore for testing our web app, we’ll need something else in order to not only test, but get coverage for our tests.

pip install coverage to take advantage of the coverage library. It acts more or less the same as pytest-cov, with a few syntactical differences and extra bells and whistles.

To actually run your tests, navigate to the level of manage.py and type the following in the command line:

```bash
$ coverage run manage.py test
```
To get the resulting coverage report
```bash
$ coverage report
```
And for missing lines
```bash
$ coverage report -m
```
Note that the coverage report needs to have been created before you can get it. You’ll need to run the tests first for every new report you wish to generate.

You’ll notice that coverage will cover all python files, including manage.py, every migration, and even your tests. You can tell coverage to ignore those with the --omit flag.
```bash
$ coverage run --omit=*/migrations/*,*/tests.py,manage.py,lending_library/wsgi.py manage.py test
```
All of this information can be a bit tedious to write out yourself. Instead of doing that, create a .coveragerc file at the same level of your manage.py. .coveragerc uses INI syntax much like tox.ini. Within .coveragerc add the following:
```yaml
[run]
omit =
    */migrations/*,
    */tests.py
    manage.py
    lending_library/wsgi.py

source =
    lending_library
    patron_profile

[report]
show_missing = True
```
The [run] heading contains options and flags that get applied at run time. The source key will point to which Django apps you want to run tests in.

The [report] heading contains flags that apply when you generate a coverage report. show_missing = True will show missing lines in your coverage by default. This way, your commands are simplified again.
```bash
$ coverage run manage.py test
$ coverage report
```
For slightly more information on incorporating coverage.py into your Django tests, check the Django docs. For more information on the coverage library, here are the coverage docs

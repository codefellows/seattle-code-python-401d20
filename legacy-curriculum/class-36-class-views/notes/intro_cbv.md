# First Steps into Class-Based Views

Thus far we’ve been using functional views to handle all of our requests and
return our responses. However, Django is largely moving toward [Class-Based Views](https://docs.djangoproject.com/en/2.0/ref/class-based-views/), so it’s
worth understanding how they work.

## The `TemplateView`

We can update the views in our `lending_library` app to use a class view.


```python
# in lending_library/lending_library/views.py

...
from django.views.generic import TemplateView
...
```

The purpose of every class-based view inheriting from
`django.views.generic.TemplateView` is to render a template.

All of the class-based views are going to provide us with simple ways of
performing common tasks. They also provide us with API methods to take care of
some of the things that go around those common tasks.

There is [good documentation](https://docs.djangoproject.com/en/2.0/ref/class-based-views/)
regarding the class-based views API. It has a list of all of the different
kinds of views that there are. Let’s click on [TemplateView](https://docs.djangoproject.com/en/2.0/ref/class-based-views/base/#templateview) and see what it contains.

A flowchart of methods:

  * a `dispatch()` method
  * `http_method_not_allowed()`
  * [`get_context_data()`](https://docs.djangoproject.com/en/2.0/ref/class-based-views/mixins-simple/#django.views.generic.base.ContextMixin.get_context_data): this method returns a dictionary that includes all of the items we want to pass in as part of the view’s context.

So let’s go back to our `views.py` and create for ourselves a class-based view
that uses the `get_context_data()` method to return a dictionary. We’ll also
insert a breakpoint so we can inspect the state of things when this method is
called:


```python
# lending_library/lending_library/views.py

...
class SampleView(TemplateView):
    template_name = "lending_library/home.html"

    def get_context_data(self):
        import pdb; pdb.set_trace()
        return {}
...
```

We also need to rewire our urls:


```python
# lending_library/lending_library/urls.py

...
from lending_library.views import SampleView
...

urlpatterns = [
    ...
    url(
        r"^(?P<num>\d+)/(?P<name>\w+)/$",
        SampleView.as_view(),
        name="testme"
    ),
    ...
]
```

The temptation will be to just drop the class in there like we had with
function-based views. That’s not gonna work. When you use a class-based view
in a `url` pattern, you need to call the `as_view()` method on it.

What’s the difference between calling the class itself and calling the method
of `as_view()`? The `as_view()` method is a `classmethod` (remember the
`@classmethod` decorator?). What’s the most common case of using a
`classmethod`? To provide you with an alternate constructor.

`as_view()` builds an instance of this view and hands it back to you. What
gets handed back to you is a callable, like the function-based views we had
used before.

What is the implication of this? As was mentioned before, the `urlpatterns`
are evaluated and then cached. The pointers to the view functions are
evaluated and then cached, so the view functions themselves end up as the
target to these url paths.

When we say `SampleView.as_view()` and that is evaluated, what does our route
point at? It points at **_one instance_** of the class, and that one instance
is _cached_ and held on to.

What this means is that **every request** that is received by your Django app
matching that url gets handed off to that instance, and that instance is the
only instance that exists. There is only ever one instance. What that means is
that if one of our methods we do something like:


```python
class SampleView(TemplateView):
    template_name = "lending_library/home.html"

    def get_context_data(self):
        import pdb; pdb.set_trace()
        self.flibbertygibbet = "horcrux"
        self.potato = True
        return {}
```

Now our `self.flibbertygibbet` attribute is set for every request that comes
after this until we restart Django. So _don’t mutate your class objects. Don’t
mutate your instances in views._ Try _REALLY_ hard not to hang too much state
on your class objects because _that state persists between requests_.

Flask and Pyramid create classes when the request comes in, and the state of
that class is local to a particular request. That is not the case in Django.
The state of a class-based view is _global to all requests_. So watch out for
that.

There will come a time when something unexpected happens to you. You make a
call to a view that you set up some sort of fancy switch on, and it works
perfectly. Then you’ll make a different call to it and it no longer works as
you expect. 9 times out of 10 this happens because you flip a switch in the
state of your view, and you didn’t flip it back. Again, be careful. Be aware
that the internal state of a Django class-based view is global to all
requests.

Let’s try our new class-based view:

`http://localhost:8000/123/pancakes/`

This drops into our debugger:


```
> .../lending_library/lending_library/views.py(22)get_context_data()
-> return {}
(Pdb) l
 17     class SampleView(TemplateView):
 18         template_name = 'home.html'
 19
 20         def get_context_data(self, num=0, name='balloons'):
 21             import pdb; pdb.set_trace()
 22             self.flibbertygibbet = "horcrux"
 23             self.potato = True
 24  ->         return {}
[EOF]
(Pdb) num
u'123'
(Pdb) name
u'pancakes'
(Pdb) c
[19/Jan/2016 08:06:32]"GET /123/pancakes/ HTTP/1.1" 200 136
```

Notice, we passed off a context that doesn’t have any of the values in it that
our template is expecting. Did our template break? No! This is a Django
_feature_.

If there is an error that happens when you render a template, Django will
swallow it silently unless you take extra measures to set up a template
debugger. This can be annoying when you try to debug, so remember there are
settings that can allow you to turn on template debugging.

Let’s actually return our context here, and remove our breakpoint:


```python
# lending_library/lending_library/views.py

class SampleView(TemplateView):
    template_name = "lending_library/home.html"

    def get_context_data(self, num=0, name="balloons"):
        return {"num": num, "name": name}
```

Reload our browser and we should see our “Hello pancakes!” message.

One last interesting thing: We set our `TemplateView` to have a `template_name
= "lending_library/home.html"`. If we take that away, we’ll get an error.
These kinds of attributes of class-based views can also be used as arguments
of the `as_view()` call. So in our `urlpatterns`:


```python
# lending_library/lending_library/urls.py
...
    url(
        r'^(?P<num>\d+)/(?P<name>\w+)/$',
        SampleView.as_view(template_name="lending_library/home.html"),
        name="testme"
    ),
...
```

What does this mean? There’s a reason these views are called “generic”. The
reason is because they have a certain number of attributes that control how
they work. Things like `template_name` need a template in order to render.
They provide a method by which all of those things can be passed in as
arguments to the `as_view()` call, because that means you can use this view
over and over and over again in different ways with different templates.

This is actually kind of cool. In fact, as an experiment, we can try to use
`TemplateView` without any view code at all, and it will still render:


```python
# lending_library/lending_library/urls.py
...
from django.views.generic import TemplateView
...
    url(
        r'^(?P<num>\d+)/(?P<name>\w+)/$',
        TemplateView.as_view(template_name="lending_library/home.html"),
        name="testme"
    ),
...
```

And now we reload our browser, and our `TemplateView` is able to render our
template automatically from the context of the url.

This is just the first, very-most generic Class-based view available. There
are of course, many others.


```
In [1]: from django.views import generic

In [2]: [item for item in dir(generic) if "View" in item]
['ArchiveIndexView',
 'CreateView', # <---- most likely to use
 'DateDetailView',
 'DayArchiveView',
 'DeleteView', # <---- most likely to use
 'DetailView', # <---- most likely to use
 'FormView', # <---- most likely to use
 'GenericViewError',
 'ListView', # <---- most likely to use
 'MonthArchiveView',
 'RedirectView',
 'TemplateView',
 'TodayArchiveView',
 'UpdateView', # <---- most likely to use
 'View',
 'WeekArchiveView',
 'YearArchiveView']
```

Like any toolkit, you choose the right tool for the right job. You can drive a
nail into a wall with a shoe, but that’s the _job_ of a hammer. Similarly, you
can get any data onto to the page with a _TemplateView_ , but the **ListView**
is specialized for listing instances of one model, **DetailView** for showing
the data for an individual model instance, and **CreateView** for adding a new
instance of a model to your web app.


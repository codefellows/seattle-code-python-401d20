# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 28: Django CRUD with Forms

## Create, Read, Update and Delete with Forms

Add CRUD functionality to Blog app.

**This is a Solo assignment**

## Setup

- Create `django-crud` repo

## Features

**NOTE: Replace `blog` and `Post` with names of your choosing.**

- Use starter blog `starter_project` as a starting point, replacing with your own app name and Model.
  - starter project is in course repo for today's class
- Create `BlogCreateView` that extends appropriate generic view
  - Add urls and templates to support the new view
- Create `BlogUpdateView` that extends appropriate generic view
  - Add urls and templates to support the new view
- Create `BlogDeleteView` that extends appropriate generic view
  - Add urls and templates to support the new view
- Add appropriate navigation links in header and/or content blocks to access added features.


## Additional Notes

### Get Absolute URL

In model define `get_absolute_url` method. E.g.

```python
def get_absolute_url(self):
  return reverse('post_detail',args=[str(self.id)])
```

This will enable Create and Update Views to navigate to correct location when form is submitted.

### Delete Template

Delete view will ask you to confirm deletion. See example below

{% raw %}
```python
{% extends 'base.html' %}

{% block content %}
    <h1>Delete post</h1>
    <form action="" method="post">
      {% csrf_token %}
      <p>Are you sure you want to delete "{{ post.title }}"?</p>
      <input type="submit" value="Confirm" />
    </form>
{% endblock content %}
```
{% endraw %}

### Delete View

Delete View needs to define a `success_url` to know where to go after the deletion.

Also, note the use of `reverse_lazy` which navigates away only after confirmation.

```python
from django.urls import reverse_lazy
...
class BlogDeleteView(DeleteView):
  model = Post
  template_name = 'post_delete.html'
  success_url = reverse_lazy('home')
```

## Stretch Goals

- add multiple models
- use an alternate test runner
- add more advanced fields to models, e.g. created time stamp

## Rubric

- 7pts: Program meets all requirements described in Lab directions.

	Points  | Reasoning |
	 ------------ | :-----------: |
	7       | Program runs as expected, no exceptions during execution |
	5       | Program meets all of the  functionality requirements described above (including tests) // Program runs/compiles, Program contains logic/process errors|
	4       | Program meets most of the functionality requirements described above (including tests)  // Program runs/compiles, but throws exceptions during execution |
	3       | Program missing most of the functionality requirements described above // Program runs/compiles |
	2       | Missing Readme Document // Readme Document does not meet standards |
	0       | Program does not compile/run. Build Errors // Required naming conventions not met |
	0       | No Submission |

- 3pts: Code meets industry standards
	- These points are only awardable if you score at minimum a 5/7 on above criteria

	Points  | Reasoning |
	 ------------ | :-----------: |
	3       | Code meets Industry Standards // method and variable names are appropriate // Selective and iterative statements are used appropriately, Fundamentals are properly executed // Clearly and cleanly commented // Frequent Commits |
	2       | syntax for naming conventions are not correct (camelCasing and PascalCasing are used appropriately) // slight errors in use of fundamentals // Missing some comments // minimal or no commits |
	1       | Inappropriate naming conventions, and/or inappropriate use of fundamentals // Code is not commented  |
	0       | No Submission or incomplete submission |

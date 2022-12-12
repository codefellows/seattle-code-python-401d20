# Visualizing Data with Matplotlib

Data is great, but it's difficult to interpret as raw numbers in a file.
Stuffing those numbers into an array is great, but even that's difficult to interpret as data sets grow in size from 5-10 rows up to thousands, millions, or billions of rows.
I assure you, you don't want to read through 20,000 rows of data in order to get an idea of the trends within.

Data scientists communicate with words and figures.
You already have words, let's make some figures.

There are a [wide variety](https://blog.modeanalytics.com/python-data-visualization-libraries/) of data visualization libraries out there.
They're all based in some way on [matplotlib](https://matplotlib.org/), so we'll go through that.

## To Start

As with any Python library, download `matplotlib` using `pip`

```
(ENV) $ pip install matplotlib
```

If you use `matplotlib` from your terminal instead of inside of a Juypter notebook, it'll stop your interpreter and pop open a new window whenever you want to produce a figure.
This is quite annoying and counter-productive.
Use a Jupyter notebook, where your figures will be rendered in the browser alongside your code.

`matplotlib` is a massive library that includes tools for regular 2d figures, 3d figures, mapping, and a host of other functionality.
We don't need all of that, only the `pyplot` functionality.
So, when you're using `matplotlib`, only import the `pyplot` module, and alias it as `plt` so you don't have to write its whole name every time you want to use one of its functions.

```python
>>> import numpy as np
>>> import matplotlib.pyplot as plt
```

We can visualize some data right away as a **scatter plot** using a small handful of commands.
Let's start with creating some data showing an exponential growth curve.

```python
>>> x = np.arange(0, 5, 0.1)  # range as a numpy array
>>> print(x)
[0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.  1.1 1.2 1.3 1.4 1.5 1.6 1.7
 1.8 1.9 2.  2.1 2.2 2.3 2.4 2.5 2.6 2.7 2.8 2.9 3.  3.1 3.2 3.3 3.4 3.5
 3.6 3.7 3.8 3.9 4.  4.1 4.2 4.3 4.4 4.5 4.6 4.7 4.8 4.9]

>>> y = np.exp(x)  # "e" to the power of every value in "x"
>>> print(y)
[  1.           1.10517092   1.22140276   1.34985881   1.4918247
   1.64872127   1.8221188    2.01375271   2.22554093   2.45960311
   2.71828183   3.00416602   3.32011692   3.66929667   4.05519997
   4.48168907   4.95303242   5.47394739   6.04964746   6.68589444
   7.3890561    8.16616991   9.0250135    9.97418245  11.02317638
  12.18249396  13.46373804  14.87973172  16.44464677  18.17414537
  20.08553692  22.19795128  24.5325302   27.11263892  29.96410005
  33.11545196  36.59823444  40.44730436  44.70118449  49.40244911
  54.59815003  60.3402876   66.68633104  73.6997937   81.45086866
  90.0171313   99.48431564 109.94717245 121.51041752 134.28977968]
```

Tons of numbers, great.
Let's see those numbers as points on a chart.

```python
>>> plt.scatter(x, y)
>>> plt.show()
```

![exponential growth curve as dots](../assets/exponential_growth_0.png)

`scatter()` is a function in the `pyplot` module that will draw a chart if one doesn't already exist and place x-y coordinates on that chart.

The first argument to `scatter()` will always be the horizontal values (typically the "x" values), and the second argument always be the vertical values (typically the "y" values).
**You do not need to call your variables "x" and "y" for this to work.**

In our example above, the `scatter()` function took our `x` array and our `y` array and plotted the coordinates:

```python
[(0.0, 1.0),
 (0.1, 1.1051709180756477),
 (0.2, 1.2214027581601699),
 (0.30000000000000004, 1.3498588075760032),
 (0.4, 1.4918246976412703),
 (0.5, 1.6487212707001282),
 ...]
```

If you would like lines instead of dots, you can just use the base `plot()` method.
The argument order is very much the same as with `scatter()`.

```python
>>> degrees = np.arange(0, 2, 0.1) * np.pi
>>> amplitude = 10 * np.sin(degrees) + 70
>>> plt.plot(degrees, amplitude)
>>> plt.show()
```

![simple sine curve](../assets/sine_curve.png)

## Customizing Your Figures

When making a scatter plot, there's at least 3 attributes that you'll want to concern yourself with:

- point size
- point color
- point _border_ color

You can control each of these using keyword arguments in `plt.scatter()`.
Let's alter this plot so such that our points are bigger, red, and have a black border:

```python
>>> plt.scatter(x, y, s=50, c="#FF0000", edgecolor="None")
>>> plt.show()
```

![exponential growth curve with bigger, red dots](../assets/exponential_growth_1.png)

You can also change the point shape by using the `marker` keyword argument.
The available markers are...

- `s`: Square
- `o`: Circle
- `D`: Diamond
- `.`: Point
- `^`, `v`, `>`, `<`: Triangles
- `*`: Star
- `p`: Pentagon
- `+`: Plus signs
- `x`: X’s
- `|`: Vertical Lines
- `_`: Horizontal Lines

### Control and Label Your Axes

Figures are meaningless without some description of what they're showing.
Every figure should have axis labels.
You can set those labels using the `plt.xlabel` and `plt.ylabel` functions.
You can also add a title to your figure with `plt.title`

```python
>>> plt.scatter(x, y, s=150, c="#FF0000", edgecolor="black")
>>> plt.title("This is a scatter plot")
>>> plt.xlabel("Number of Bottles [$x$]")
>>> plt.ylabel("Level of Drunkenness [$y = e^x$]")
>>> plt.show()
```

![exponential growth curve with labels](../assets/exponential_growth_2.png)

If you want to set limits on the range of each axis, you can use the `xlim()` or `ylim()` functions.

```python
>>> plt.scatter(x, y, s=150, c="#FF0000", edgecolor="black")
>>> plt.title("This is a scatter plot")
>>> plt.xlabel("Number of Bottles [$x$]")
>>> plt.ylabel("Level of Drunkenness [$y = e^x$]")
>>> plt.xlim(0, 10)
>>> plt.ylim(40, 100)
>>> plt.show()
```

![exponential growth curve with labels](../assets/exponential_growth_3.png)

You can combine two series of data onto one diagram by just adding a second line that would plot that data.
As long as it comes before `plt.show()` it'll all be in the same figure.

```python
>>> plt.scatter(x, y, s=150, c="#FF0000", edgecolor="black")
>>> plt.plot(degrees, amplitude)
>>> plt.title("This is a scatter plot")
>>> plt.xlabel("Number of Bottles [$x$]")
>>> plt.ylabel("Level of Drunkenness [$y = e^x$]")
>>> plt.xlim(0, 10)
>>> plt.ylim(40, 100)
>>> plt.show()
```

![exponential growth and sine](../assets/combined_figure.png)

Note that the order in which you call your plotting functions will determine which series of data shows up "on top" in your figure.

One last note, if you want to be able to save the figure you've made, use `plt.savefig()` before you call `plt.show()`.
You pass to `savefig()` the path (either absolute or relative) to the file that you intend to create or overwrite.
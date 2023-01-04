# Warm-Up Exercise

> Don’t Use Mutable Values for Default Arguments

What are the ingredients on `aThirdSandwich` ?

```python
def addIngredient(ingredient, sandwich=['bread', 'bread']):
    sandwich.insert(1, ingredient)
    return sandwich

mySandwich = ['bread', 'cheese', 'bread']
mySandwich = addIngredient('butter', mySandwich)
print(mySandwich)

anotherSandwich = addIngredient('turkey')
print(anotherSandwich)

aThirdSandwich = addIngredient('pesto')
print(aThirdSandwich)
```

## Attribution

[Common Python Gotchas](https://inventwithpython.com/beyond/chapter8.html)

# Warm-Up Exercise

> Summary: Let's Make a Blackjack Game!


```python
import random
suites = ( 'Hearts', 'Diamonds', 'Spades', 'Clubs')
card_names = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
```

## Feature Tasks

- Use the data from above:
  - Create a Card with a suit and "value" attribute.
  - Create a Deck Class
    - Instantiate all 52 cards and add them to a list
      - Consider something like:
        for suit in suits:
            for card in card_names:
    - Shuffle the Deck
    - Deal a single card


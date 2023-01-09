# Warm-Up Exercise

> Match the correct depth-first traversal with the output.

```text
      {A}
     /   \
  {B}     {C}
  / \    /  \
{D} {E}{F}  {G}
```

## Feature Tasks

Given the tree above, different traversals will print the node's value, traverse to one child, and traverse to the remaining child - in the order specified.

The traversal must be `in-order` (left-root-right),`pre-order` (root-left-right) or `post-order` (left-right-root).

Supply the traversal that would generate the following outputs...

- `D,E,B,F,G,C,A`
- `A,B,D,E,C,F,G`
- `D,B,E,A,F,C,G`

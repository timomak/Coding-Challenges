# Two-fer
[link](https://exercism.io/my/solutions/067fd8d897f141a8ae2c75a4e466e411)

Problem:
Two-fer or 2-fer is short for two for one. One for you and one for me.

```
"One for X, one for me."
When X is a name or "you".
```

If the given name is "Alice", the result should be "One for Alice, one for me." If no name is given, the result should be "One for you, one for me."

My Solution:
```Python
def two_fer(name=None):
    if name == None:
        return 'One for you, one for me.'
    else:
        return 'One for {}, one for me.'.format(name)
```

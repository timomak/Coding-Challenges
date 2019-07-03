# Bob from Exercism
from Exercism ([link](https://exercism.io/my/solutions/9ed68ce1a5e7474b8e1b8450f626929f))

Problem:
Make Bob.

Example:
```
Bob is a lackadaisical teenager. In conversation, his responses are very limited.

Bob answers 'Sure.' if you ask him a question.

He answers 'Whoa, chill out!' if you yell at him.

He answers 'Calm down, I know what I'm doing!' if you yell a question at him.

He says 'Fine. Be that way!' if you address him without actually saying anything.

He answers 'Whatever.' to anything else.
```

Refactor:
```Python
def response(hey_bob):
    # Check if he is said anything
    if len(hey_bob) <= 0:
        return 'Fine. Be that way!'

    if hey_bob[0] == " " or hey_bob == "":
        return 'Fine. Be that way!'

    if hey_bob[0].isalpha() == False:
        return 'Fine. Be that way!'

    # If he's being yelled at
    if hey_bob == hey_bob.upper() and hey_bob[-1] != "?":
            return 'Whoa, chill out!'

    # If someone yells a question
    elif hey_bob == hey_bob.upper() and hey_bob[-1] == "?":
            return 'Calm down, I know what I\'m doing!'

    # Question with whitespace
    if hey_bob[-1] != " ":
        while hey_bob[-1] == " ":
            hey_bob = hey_bob[:len(hey_bob)-1]

    # Just a question
    if hey_bob[-1] == "?":
        return 'Sure.'

    # Anything else
    else:
        return 'Whatever.'
```

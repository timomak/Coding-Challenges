def response(hey_bob):
    # Bob is a lackadaisical teenager. In conversation, his responses are very limited.
    #
    # Bob answers 'Sure.' if you ask him a question.
    #
    # He answers 'Whoa, chill out!' if you yell at him.
    #
    # He answers 'Calm down, I know what I'm doing!' if you yell a question at him.
    #
    # He says 'Fine. Be that way!' if you address him without actually saying anything.
    #
    # He answers 'Whatever.' to anything else.


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

    # # Stuff at the back
    # if hey_bob[-1] != "?" and hey_bob[-1] != "!" and hey_bob[-1].isalpha() == False and hey_bob[-1].isnumeric() == False:
    #     while hey_bob[-1].isalpha() !=  True or hey_bob[-1].isnumeric() != True or hey_bob[-1]!=  "?" or hey_bob[-1]!=  "!":
    #         hey_bob = hey_bob[:len(hey_bob)-1]

    # Just a question
    if hey_bob[-1] == "?":
        return 'Sure.'

    # Anything else
    else:
        return 'Whatever.'

print("\t\t\t\t\t\t\t\t\t\t".isalpha())

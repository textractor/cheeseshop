
def cheeseshop_ng():

    """Ask for a type of cheese, get an excuse.

    In this game, the customer is not king.
    Currently lacks a way for the player to change the chosen cheese
    except by restarting the game.
    """

    # For randomly choosing a cheese.
    from random import choice

    cheeses = {'cheddar': 'Careful not to cut yourself on it!',
               'cream': 'Whip it good!',
               'fontina': 'Puts the fon in fondue!',
               'swiss': 'Yodel-ay-hee-hoo!',
               'brie': 'Just because it rhymes with free doesn\'t mean it is!',
               'airedale': 'So good, they named a breed of dog after it!',
               'roquefort': 'There may very well be a fort there!',
               'camembert': 'You\'re almost there with ___!',
               'cotija': 'Un queso blanco de Mexico!',
               'chevre': 'Oh this one\'s a real goat!',
               'feta': 'It\'s Greek to me!',
               'mozzarella': 'Bufala Bill might have liked this!',
               'emmental': 'Some end it tal, some taler!',
               'gouda': 'Itsa very good a cheese!',
               'taleggio': 'It\'s not an Italian musical term!',
               'parmesan': 'Needs no introduction, it already has P-R!',
               'manchego': 'Don Quixote approved!',
               'monterey jack': 'You don\'t know jack!'
    }
    
    responses = ['Sorry, cat ate it.',
                 'Dried up into a brick. Mortared it into the wall there.',
                 'Not a shred.',
                 'Afraid it got very runny. Ran right out the door.',
                 'Delivery van broke down, should be in by tomorrow.',
                 'That comes in every other Wednesday if the month has a fifth Sunday.',
                 'Sold out this morning.',
                 'Blimey, is that really a cheese?!',
                 'Yes, sir, we had a wheel\'s worth! Couple of very large mice bought the lot not 30 minutes ago.',
                 'I believe there\'s a shortage due to the Swiss joining the war.'
    ]

    kind = 'wensleydale'
    # Why not use popitem() instead of choice? 
    # Then cheeses can't be repeated,
    # but then must handle {} situation that may eventually result.    
    bullseye = choice(cheeses.keys())
    print '\n' + ">>> Today's Cheese:   " + cheeses[bullseye] + ' <<<' + '\n' # print clue
    while kind != 'piss off':
        kind = raw_input('What kind of cheese would you like?' + '\n'
                "(enter the name of a cheese, in lower case, or enter 'piss off' to exit) ... )" + '\n')
        # print bullseye for debug
        if kind == bullseye:  # The right cheese ....
            print ('\n' + 'Why, yes, we\'ve got a bit in stock!' + '\n')
            bullseye = choice(cheeses.keys())  # Choose a new cheese (same cheese may be chosen ... see note above.)
            print ">>> Today's Cheese:   " + cheeses[bullseye] + ' <<<' + '\n' # print clue
        elif kind == 'wensleydale':
            print '\n' + 'Yes? ... Oh, good one, see my name\'s Wensleydale.' + '\n'
        elif kind == 'piss off':
                print '\n' + 'Very good.' + '\n'
        else:
                print '\n' + choice(responses) + '\n'


cheeseshop_ng()


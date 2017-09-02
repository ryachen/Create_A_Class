import random

#I edited the rock paper scissors program to randomly deal each player 2 cards, where whoever's cards have the greatest sum wins. 

CHOICES = ['2', '3', '4', '5', '6','7','8','9','10','J','Q','K','A']

class Action:
    def __init__(self, prompt):
        '''Create an action instance, either by randomly choosing the action or prompting the user.'''

        # if an action hasn't been named, choose it randomly
        if prompt is False:
            self.name = random.choice(CHOICES)
            self.card = random.choice(CHOICES)
        else:
            while True:
                self.name = random.choice(CHOICES)
                self.card = random.choice(CHOICES)

                print 'Your first card is {}.'.format(self.name)
                print 'Your second card is {}.'.format(self.card)

                break
        # get the position of the choice in the list

        self.cardsum = CHOICES.index(self.name) + CHOICES.index(self.card) + 4

        if prompt is True:

            print 'The sum of your cards are {}.'.format(self.cardsum)



    def compete(self, other_action):
        '''Compete against another action. Print out who won.'''

        if other_action.cardsum == self.cardsum:
            print 'The sum of my cards are {}'.format(self.cardsum)
            print 'Tie! We both got {}!'.format(self.cardsum)

        # each action is beaten by the action after it in the list
        # modulo makes it wrap around to the beginning of the list
        elif other_action.cardsum < self.cardsum:
            print 'The sum of my cards are {}'.format(self.cardsum)
            print '{} beats {}! I win!'.format(self.cardsum, other_action.cardsum)

        else:
            print 'The sum of my cards are {}'.format(self.cardsum)
            print '{} beats {}! You win!'.format(other_action.cardsum, self.cardsum)


# this is a standard Python thing: definitions go above, and any code that will actually
# run should go into the __main__ section. This way, if someone imports the file because
# they want to use the functions or classes you've defined, it won't start running your game
# automatically
if __name__ == '__main__':

        # Create actions for the two players, computer and user
        computer_action = Action(prompt=False)
        user_action = Action(prompt=True)

        # Have the actions play against one another
        computer_action.compete(user_action)

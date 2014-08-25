from points import points
from round import Round
from words import HasNextLength

class Game:
    """ Represents a Word Guess Game """
    
    def __init__(self, id):
        """ Initialize the Game """
        self.id = id
        self.currentRound = Round()
        self.points = 0
        
    def guess(self, guesses):
        """ Return the results of the guess against the current Round """
        results = self.currentRound.guess(guesses)
        self.awardPoints()
        return results
        
    def awardPoints(self):
        """ Award Poitns if the Round was finished """
        if self.currentRound.completed:
            self.points += points[self.currentRound.triesLeft]
            
    def hasNextRound(self):
        """ Return if there is a round to play after the current round """
        return HasNextLength(self.currentRound.wordLength)
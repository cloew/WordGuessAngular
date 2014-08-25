from points import points
from round import Round
from words import HasNextLength, GetNextLength

class Game:
    """ Represents a Word Guess Game """
    
    def __init__(self, id):
        """ Initialize the Game """
        self.id = id
        self.currentRound = Round()
        self.points = 0
        
    def guess(self, guesses):
        """ Return the results of the guess against the current Round """
        self.currentRound.guess(guesses)
        self.tryToAwardPoints()
        
    def startNextRound(self):
        """ Start the Next Round """
        nextWordLength = GetNextLength(self.currentRound.wordLength)
        self.currentRound = Round(wordLength=nextWordLength)
        
    def tryToAwardPoints(self):
        """ Award Poitns if the Round was finished """
        if self.currentRound.completed:
            self.points += points[self.currentRound.triesLeft]
            
    def hasNextRound(self):
        """ Return if there is a round to play after the current round """
        return HasNextLength(self.currentRound.wordLength)
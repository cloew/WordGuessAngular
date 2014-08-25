from round import Round

class Game:
    """ Represents a Word Guess Game """
    
    def __init__(self, id):
        """ Initialize the Game """
        self.id = id
        self.currentRound = Round(2)
        
    def guess(self, guesses):
        """ Return the results of the guess against the current Round """
        return self.currentRound.guess(guesses)
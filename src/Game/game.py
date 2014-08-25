from round import Round

class Game:
    """ Represents a Word Guess Game """
    
    def __init__(self, id):
        """ Initialize the Game """
        self.id = id
        self.currentRound = Round(2)
from games import games

class GameWrapper:
    """ A Wrapper for a Word Guess Game that handles its conversion to and from JSON """
    
    def __init__(self, game=None, id=None):
        """ Initialize the Game Wrapper """
        if id is not None:
            game = games[id]
        self.game = game
        
    def toJSON(self):
        """ Return the game as a JSON Dictionary """
        return {'game':{'id':self.game.id,
                        'wordlength':self.game.currentRound.wordLength,
                        'triesleft':self.game.currentRound.triesLeft,
                        'roundcomplete':self.game.currentRound.completed}}
from Game.game import Game

id = 1
games = {}

def StartNewGame():
    """ Start a New Game """
    global games
    global id
    
    game = Game()
    games[id] = game
    id += 1
    return {}
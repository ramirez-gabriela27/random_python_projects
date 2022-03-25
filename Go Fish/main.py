from game import GoFish

#main game loop 
def main():
    game = GoFish()
    game.setup(4)
    while game.playing:
        game.turns()
    winner = game.players[0]
    for player in game.players:
        if winner.score < player.score:
            winner = player
    print('The winner is {} with {} matches'.format(winner.name, winner.score))
    

if __name__ == "__main__":
    main()

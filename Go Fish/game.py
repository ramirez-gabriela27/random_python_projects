from deck import Deck
from player import Player
from os import system
from time import sleep

class GoFish:
    def __init__(self):
        self.deck = Deck()
        self.players = []
        self.playing = True
    
    def setup(self, num_players):
        self.deck = Deck()
        for player_num in range(num_players):
            self.players.append(Player("Player {}".format(player_num)))
            player = self.players[player_num]
            if num_players < 5:
                for card in range(7):
                    self.deck.deal_card(player)
            else:
                for card in range(5):
                    self.deck.deal_card(player)
    
    def turns(self):
        for player in self.players:
            print("{}'s turn".format(player.name))
            #print cards in hand
            player.print_hand()
            #get the rank and player to ask for a card 
            chosen_rank = int(input("For which rank are you asking? (1-13)"))
            while chosen_rank > 13 or chosen_rank < 1:
                chosen_rank = int(input("Please ask for a valid rank (1-13)"))
            #check that the asked player is valid
            player_num = int(input("Which player are you asking? (0-3)"))
            while player_num > 3 or player_num <0 or self.players[player_num] is player:
                player_num = int(input("Please ask for a valid player other than yourself (0-3)"))

            #check whether any card of the chosen rank was found, if so add it to the current player's hand, otherwise current player draws from deck.
            found_card = self.players[player_num].check_hand(chosen_rank)
            if found_card != "":
                print("Nice! You got a {}".format(chosen_rank))
                player.hand.append(found_card)
            else:
                print("Go fish!")
                self.deck.deal_card(player)
            #print player's new hand
            player.print_hand()
            sleep(2)
            #play any sets held by the current player 
            self.play_sets(player)
            #let the player see their new hand 
            sleep(2)
            system('clear')
    
    def play_sets(self, player):
        for rank in range(1, 14):
            matches = []
            for card in player.hand:
                if card.rank is rank:
                    matches.append(card)
            if(len(matches) > 3):
                print("Playing set of {}".format(rank))
                for card in matches:
                    player.hand.remove(card)
                player.score += 1
                if len(player.hand) == 0:
                    self.playing = False
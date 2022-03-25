from card import Card
import random

suits = ["Diamonds", "Clubs", "Hearts", "Spades"]
class Deck:
  #constructor for deck -- creates cards and adds them to deck
  def __init__(self):
    self.cards = []
    for suit in suits:
      for rank in range(1, 14):
        self.cards.append(Card(suit,rank))

  def print_deck(self):
    for card in self.cards:
      card.print_card()

  #shuffles the deck randomly  
  def shuffle(self):
    for index in range(len(self.cards)-1):
      num = random.randint(index+1, len(self.cards)-1)
      tmp = self.cards[index]
      self.cards[index] = self.cards[num]
      self.cards[num] = tmp
      
  #will deal cards to a player
  def deal_card(self,player):
    if len(self.cards) > 0:
      card = random.choice(self.cards)
      player.hand.append(card)  
      self.cards.remove(card)
    else:
      print("No cards left!")
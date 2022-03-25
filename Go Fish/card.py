class Card:
  #every card will hava a suit and a rank
  def __init__(self, Suit, Rank):
    self.suit = Suit
    self.rank = Rank

  def print_card(self):
    print("{} of {}".format(self.rank, self.suit))
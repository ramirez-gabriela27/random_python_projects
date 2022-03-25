class Player:
  def __init__(self, Name):
    self.hand = []
    self.score = 0
    self.name = Name

  def print_hand(self):
    for card in self.hand:
      card.print_card()

  #checking player hand for any cards of that rank
  def check_hand(self, rank):
    for card in self.hand:
      if card.rank == rank:
        self.hand.remove(card)
        return card
    return ""
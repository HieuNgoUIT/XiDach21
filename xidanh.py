import random
class Person():
    def __init__(self):
        self.person_cards = []
        
    def append_card(self, card):
        self.person_cards.append(card)

class Deck():
    def __init__(self):
        self.full_cards = self.create_deck()
        
    def create_deck(self):
        cards = [2,3,4,5,6,7,8,9,10, 'J', 'Q', 'K', 'A']
        full_cards = []
        for card in cards:
            for _ in range(4):
                full_cards.append(card)
        
        random.shuffle(full_cards)
        return full_cards

    def pop(self):
        return self.full_cards.pop()

class Game():
    def __init__(self, players, host_index, deck):
        self.host = players[host_index]
        self.players = players[0 : host_index] + players[host_index+1 :]
        self.deck = deck
    
    def get_two_card(self, deck):
        a = deck.pop()
        b = deck.pop()
        return a,b 

    def get_one_card(self, deck):
        return deck.pop()

    def start(self):
        for player in self.players:
            a, b = self.get_two_card(self.deck)
            player.append_card(a)
            player.append_card(b)

if __name__ == "__main__":
    my_deck = Deck()
    ps = []
    p1 = Person()
    p2 = Person()
    ps.append(p1)
    ps.append(p2)
    mydeck = Deck()
    mygame = Game(ps,1,my_deck)
    mygame.start()
    print(mygame.players[0].person_cards)
   

    

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
    
    def get_two_card(self):
        a = self.deck.pop()
        b = self.deck.pop()
        return a,b 

    def get_one_card(self):
        return self.deck.pop()

    def start(self):
        a, b = self.get_two_card()
        self.host.append_card(a)
        self.host.append_card(b)
        for player in self.players:
            a, b = self.get_two_card()
            player.append_card(a)
            player.append_card(b)

    def player_phase(self):
        for player in self.players:
            if (player.state = 'Withdrawl'):
                player.get_one_card()

    def host_phase(self):
        while(True):
            if('want to check'):
                check_and_result()
            else:
                self.host.get_one_card()

if __name__ == "__main__":
    ps = []
    p1 = Person()
    p2 = Person()
    p3 = Person()
    ps.append(p1)
    ps.append(p2)
    ps.append(p3)
    
    mydeck = Deck()
    
    mygame = Game(ps,1,mydeck)
    mygame.start() #chia bai`
    
    
    print(mygame.players[0].person_cards)
    print(mygame.players[1].person_cards)
    print(mygame.host.person_cards)

   

    

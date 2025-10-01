import random
from enum import IntEnum

class Rank(IntEnum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

def create_deck():
    redSuits = ["Hearts", "Diamonds"]
    blackSuits = ["Clubs", "Spades"]
    numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]
    faceCards = ["Jack", "Queen", "King", "Ace"]
    deck = []

    for suit in redSuits:
        for number in numbers:
            deck.append(number + " of " + suit)

    for suit in blackSuits:
        for number in numbers:
            deck.append(number + " of " + suit)
        for face in faceCards:
            deck.append(face + " of " + suit)

    random.shuffle(deck)
    return deck

def parse_card(card):
    rank_map = {
        '2': Rank.TWO,
        '3': Rank.THREE,
        '4': Rank.FOUR,
        '5': Rank.FIVE,
        '6': Rank.SIX,
        '7': Rank.SEVEN,
        '8': Rank.EIGHT,
        '9': Rank.NINE,
        '10': Rank.TEN,
        'Jack': Rank.JACK,
        'Queen': Rank.QUEEN,
        'King': Rank.KING,
        'Ace': Rank.ACE
    }
    return rank_map[card]

class Game:
    def __init__(self):
        self.deck = []
        self.hand = []
        self.deferred = False
        self.healed = False
        self.lastMonster = 15
        self.health = 20
        self.attack = 0
        self.game_end = False

    def reset_game(self):
        self.deck = []
        self.hand = []
        self.deferred = False
        self.healed = False
        self.lastMonster = 15
        self.health = 20
        self.attack = 0
        self.game_end = False

    def game_loop(self):
        self.deck = create_deck()
        print("Welcome to Scoundrel!")
        print("To exit the game, press 9 at any time!")
        self.draw()

        while not self.game_end:
            try:
                if self.health == 0:
                    print("You lost! Better luck next time!")
                    self.game_end = True
                    break
                if len(self.hand) == 0 and len(self.deck) == 0:
                    print(f"Congratulations, you won with {self.health} HP left!")
                    self.game_end = True
                    break
                if len(self.hand) == 1 and len(self.deck) > 0:
                    print("Next room!")
                    self.draw()
                print("Your hand:", self.hand)
                print("Your HP: ", self.health)
                print("Your Attack: ", self.attack.real)
                if self.lastMonster == 15:
                    print("Last enemy: none")
                else:
                    print("Last enemy: ", self.lastMonster.real)
                card = int(input("Choose a card (1, 2, 3 ,4) or choose to defer (0): "))
                if card == 0:
                    self.defer()
                elif 1 <= card <= len(self.hand):
                    self.play_card(card)
                elif card == 9:
                    print("See you next time!")
                    break
                else:
                    print("Please enter a valid number!")
            except ValueError:
                print("Please enter a number!")

        new_game = input("Do you want to play again? (y/n): ")
        if new_game == "y":
            self.reset_game()
            self.game_loop()

    def draw(self):
        while len(self.hand) < 4 and len(self.deck) > 0:
            self.hand.append(self.deck.pop())
        self.deferred = False
        self.healed = False
        print("Cards left in deck: ", len(self.deck))

    def defer(self):
        if len(self.hand) == 4 and not self.deferred:
            while len(self.hand) > 0:
                self.deck.insert(0, self.hand.pop())
            self.draw()
            self.deferred = True
        elif len(self.hand) < 4:
            print("You can't defer if you already played a card!")
        else:
            print("You already deferred your last hand!")

    def heal(self, value):
        if not self.healed:
            self.health += value
            self.healed = True
            print(f"Healed by {value} HP!")
            if self.health > 20: self.health = 20
            print(f"You have {self.health} HP left!")
        else:
            print("You already healed in this room!")

    def battle(self, value):
        if self.attack == 0:
            self.health -= value
            if self.health <= 0: self.health = 0
            print(f"Took {value} damage! You have {self.health} HP left!")
        else:
            if self.lastMonster <= value:
                self.health -= value
                if self.health <= 0: self.health = 0
                print(f"Took {value} damage! You have {self.health} HP left!")
            else:
                damage = value - self.attack
                if damage < 0: damage = 0
                self.health -= damage
                self.lastMonster = value
                if self.health <= 0: self.health = 0
                print(f"Took {damage} damage! You have {self.health} HP left!")

    def equip(self, value):
        self.attack = value
        self.lastMonster = 15
        print(f"Your attack is now {self.attack}!")

    def play_card(self, index):
        card = self.hand[index-1].split()
        card.remove("of")
        self.hand.remove(self.hand[index-1])
        if "Hearts" in card:
            card.remove("Hearts")
            self.heal(parse_card(card[0]))
        elif "Diamonds" in card:
            card.remove("Diamonds")
            self.equip(parse_card(card[0]))
        elif "Clubs" in card:
            card.remove("Clubs")
            self.battle(parse_card(card[0]))
        elif "Spades" in card:
            card.remove("Spades")
            self.battle(parse_card(card[0]))
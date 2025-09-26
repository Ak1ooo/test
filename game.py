class Game:
    def __init__(self, deck):
        self.deck = deck
        self.hand = []
        self.deferred = False
        self.healed = False
        self.health = 20
        self.attack = 0

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


    def draw(current_hand, deck):
        while len(current_hand) < 4:
            current_hand.append(deck.pop())
        deferred = True
        return deferred

    def defer(current_hand, deferred, deck):
        if len(current_hand) == 4 and not deferred:
            while len(current_hand) > 0:
                deck.append(current_hand.pop())
            return True
        else:
            print("You already deferred your last hand!")

    def heal(value):
        if not healed:
            health += value
            healed = True
        if health > 20: health = 20
        return health

    def battle(value):


    def equip(value):


    def play_card(current_hand, index):
        card = current_hand[index].split()
        card.remove("of")
        current_hand.remove(current_hand[index])
        if card.contains("Hearts"):
            heal(int(card[0]))
        elif card.contains("Diamonds"):
            equip(int(card[0]))
        elif card.contains("Spades" or "Clubs"):
            battle(current_hand[index])
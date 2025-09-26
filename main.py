import random
import game

if __name__ == '__main__':
    random.shuffle(game.deck)
    print("Welcome to Scoundrel!")

    game.draw(game.hand, game.deck)
    print("Your hand:", game.hand)
    print("Choose a card (1, 2, 3 ,4):")
    print("Or choose to defer (0):")

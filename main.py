import os
import random
from arts import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def points(cards):
    tsum = 0
    for c in cards:
        tsum += c
    return tsum


def scoreDisplay():
    print(f"    Your cards: {playerCards}, current score: {points(playerCards)}")
    print(f"    Computer's first card: {dealerCards[0]}")


def cardInput():
    while True:
        if points(playerCards) > 21 and 11 not in playerCards:
            print(f"    Your final hand: {playerCards}, final score: {points(playerCards)}")
            print(f"    Computer's final hand: {dealerCards}, final score: {points(playerCards)}")
            print(f"You went over. It's a bust. You lose!")
            return
        if points(playerCards) > 21 and 11 in playerCards:
            playerCards[playerCards.index(11)] = 1
        if points(playerCards) < 21:
            scoreDisplay()
            take = ''
            while take != 'y' and take != 'n':
                take = input("Type 'y' to get another card, type 'n' to pass: ")
                if take == 'y':
                    playerCards.append(random.choice(cards))
                elif take == 'n':
                    print(f"    Your final hand: {playerCards}, final score: {points(playerCards)}")
                    print(f"    Computer's final hand: {dealerCards}, final score: {points(dealerCards)}")
                    if points(playerCards) > points(dealerCards):
                        print("You win!")
                        return
                    elif points(playerCards) < points(dealerCards) and points(dealerCards)<=21:
                        print("You lose!")
                        return
                    elif points(playerCards) < points(dealerCards) and points(dealerCards)>21:
                        print("The dealer busts. You win!")
                        return
                    else:
                        print("It's a draw!")
                        return
                else:
                    print("Invalid input! Try again.")

clear_screen()
play = input("Do you want to play a game of blackjack? Type 'y' on 'n': ").lower()
while play == 'y':
    print(logo)
    playerCards = []
    dealerCards = []
    playerCards.append(random.choice(cards))
    dealerCards.append(random.choice(cards))
    playerCards.append(random.choice(cards))
    dealerCards.append(random.choice(cards))

    while points(dealerCards) < 17:
        dealerCards.append((random.choice(cards)))
        if points(dealerCards) > 21 and 11 in playerCards:
            playerCards[playerCards.index(11)] = 1

    cardInput()
    play = input("Do you want to play another game of blackjack? Type 'y' on 'n': ").lower()
    clear_screen()




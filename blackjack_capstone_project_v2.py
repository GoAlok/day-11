import random
from art import logo
import os

def new_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(player_score, computer_score):
    if player_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You lose. Opponent has BlackJack."
    elif player_score == 0:
        return "You win. You have BlackJack."
    elif player_score > 21:
        return "You went over. You lose."
    elif computer_score > 21:
        return "You win. Opponent went over."
    elif player_score > computer_score:
        return "You win."
    else:
        return "You lose."

def play():
    print(logo)

    player_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        player_cards.append(new_card())
        computer_cards.append(new_card())

    while not is_game_over:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)
        print(f" -- Player's cards: {player_cards}, Player score: {player_score} ")
        print(f" -- Computer's cards: {computer_cards[0]}")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            player_should_deal = input("Do you want to deal: 'Y'/'N': ").capitalize()
            if player_should_deal == "Y":
                player_cards.append(new_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(new_card())
        computer_score = calculate_score(computer_cards)
    print(f" -- Player final hand: {player_cards}, final score: {player_score} ")
    print(f" -- Computer's final hand: {computer_cards}, final score: {computer_score} ")
    print(compare(player_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    os.system('cls')
    play()
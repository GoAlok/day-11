############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


# --------------- Your code here ---------------

import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

computer_cards = []
player_cards = []

# -------------- LOGO --------------
print(logo)
# --------- Deal ---------
def new_deal():
    random_cards = random.choice(cards)
    return random_cards
#  ----------- 2-random cards -----------
def random_2_cards():
    computer_cards.append(new_deal())
    computer_cards.append(new_deal())
    player_cards.append(new_deal())
    player_cards.append(new_deal())
    return computer_cards, player_cards
random_2_cards()

def calc_computer_scores():
    computer_card_score = 0
    for card in range(len(computer_cards)):
        computer_card_score = computer_card_score + computer_cards[card]
    return computer_card_score

def calc_player_scores():
    player_card_score = 0
    for card in range(len(player_cards)):
        player_card_score = player_card_score + player_cards[card]
    return player_card_score

computer_score = calc_computer_scores()
player_score = calc_player_scores()

should_blackjack = True
if computer_score == 21:
    should_blackjack = True
    print("**** BLACKJACK **** Computer wins")
elif player_score == 21:
    should_blackjack = True
    print(" **** BLACKJACK **** Player wins")
else:
    print(f"Computer: {computer_cards[0]} 'X', Player: {player_cards} ")
    should_blackjack = False

if player_score > 21:
    for n_card in range(len(player_cards)):
        if player_cards[n_card] == 11:
            player_cards[n_card] = 1
player_score = calc_player_scores() #Updating player score
print(f"Player Score: {player_score}")

if should_blackjack == False:
    should_player_new_card = True
    while should_player_new_card:
        if player_score < 21:
            another_card = input('Do you want another card? "Y" / "N": ').lower()
            if another_card == 'y':
                player_cards.append(new_deal())
                print("player: ",player_cards)
            else:
                should_player_new_card = False
                print("Player Cards: ",player_cards)
            player_score = calc_player_scores()
            print("Player Score: ",player_score)
        else:
            should_player_new_card = False

    if player_score <= 21:
        should_computer_new_card = True
        while should_computer_new_card:
            if computer_score < 17:
                computer_cards.append(new_deal())
                computer_score = calc_computer_scores()
            else:
                should_computer_new_card = False

        if computer_score > 21 and player_score <= 21:
            print("Computer cards: ",computer_cards, "Computer Score: ",computer_score)
            print("Player Wins!!!")
            

        elif (player_score > computer_score) and player_score <= 21:
            print("Computer cards: ",computer_cards, "Computer Score: ",computer_score)
            print("Player Win")
            
        elif player_score == computer_score:
            print("Computer cards: ",computer_cards, "Computer Score: ",computer_score)
            print("Draw")

        else:
            print("Computer cards: ",computer_cards, "Computer Score: ",computer_score)
            print("Player lost!!!")
            
    else:
        print("Computer cards: ",computer_cards, "Computer Score: ",computer_score)
        print("Player Lost")
        
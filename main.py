import random
import os
import art


# Function for Random Cards
def card_selector():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    card_pick1 = (random.randint(0, len(cards) - 1))

    return cards[card_pick1]


# Function for Current Random Hand
def blackjack(player):
    if player == "user":
        user = [(card_selector()), (card_selector())]
        return user

    elif player == "dealer":
        dealer = [(card_selector()), (card_selector())]
        return dealer


# Score Tracker
def card_score(deck):
    deck_score = 0
    if deck == "dealer":
        for card in dealer_cards:
            deck_score += int(card)
            if deck_score == 21:
                deck_score = 0
            if deck_score > 21:
                for n, i in enumerate(dealer_cards):
                    if i == 11:
                        dealer_cards[n] = 1
        return deck_score

    elif deck == "user":
        for card in user_cards:
            deck_score += int(card)
            if deck_score == 21:
                deck_score = 0

            if deck_score > 21:
                for n, i in enumerate(user_cards):
                    if i == 11:
                        user_cards[n] = 1

        return deck_score


def draw_card(player):
    if player == "user":
        user_cards.append(card_selector())
    elif player == "dealer":
        dealer_cards.append(card_selector())


dealer_cards = blackjack("dealer")
user_cards = blackjack("user")

# Cards Drawn
blackjack("user")
blackjack("dealer")

# Current Score
card_score("dealer")
card_score("user")


# The actual BlackJack Game Function
def blackjack_game():
    print(art.logo)
    flag = True
    while flag:
        print(f"Dealer Drew: [{dealer_cards[0]}, _ ]")
        print(f'You Drew: {user_cards}, Current Score: {card_score("user")}')

        if card_score("dealer") == 21:
            print(f"Your final hand: {user_cards}, Final Score: {card_score('user')}")
            print("Dealer Wins with BlackJack.")
            print(f"Dealer Final Hand: {dealer_cards}, Final Score: {card_score('dealer')}")

        user_choice = input("Type 'y' to draw another card, type 'n' to call: ").lower().strip()

        if user_choice == "n":
            print(f"Your final hand: {user_cards}, Final Score: {card_score('user')}")
            while card_score("dealer") <= 16:
                draw_card("dealer")
            print(f"Dealer Final Hand: {dealer_cards}, Final Score: {card_score('dealer')}")
            if card_score("user") == 0:
                if card_score("dealer") == 0:
                    print("Dealer Wins with BlackJack.")
                    flag = False

                else:
                    print("You win with BlackJack.")
                    flag = False

            elif card_score("user") == card_score("dealer"):
                print("Game ends in a Tie.")
                flag = False

            elif card_score("user") > card_score("dealer"):
                if card_score("user") > 21:
                    print(f"Player Bust. You Lose!\nYour Score went over: {card_score('user')}")
                    flag = False

                else:
                    print("You win with the highest score!")
                    flag = False

            elif card_score("user") < card_score("dealer"):
                if card_score("dealer") > 21:
                    print("Dealer Bust. You Win!")
                    flag = False

                else:
                    print("You Lose. Dealer has higher score.")
                    flag = False

        if user_choice == "y":
            draw_card("user")
            if card_score("user") > 21:
                print("Player Bust. You Lose!\nYour Score went over: {card_score('user')}")
                flag = False

            # else:
                # print(f"Your current hand: {user_cards}, Current Score: {card_score('user')}")

    retry_game = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower().strip()
    if retry_game == "n":
        flag = False
        quit()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        blackjack_game()


# Intro to the Game Below
start_game = input("Do you want to play a Game of BlackJack? Type 'y' or 'n'. ").lower().strip()
if start_game == "y":
    blackjack_game()
else:
    print("Thank you for visiting. Have a good day.")
    quit()